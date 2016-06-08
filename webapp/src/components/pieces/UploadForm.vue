<template>
  <form>
    <div class="radio-inline">
      <label><input type="radio" name="upload" value="file" checked="checked" v-model="uploadType">Upload a file</label>
    </div>
    <div class="radio-inline">
      <label><input type="radio" name="upload" value="url" v-model="uploadType">Provide an URL</label>
    </div>

    <div class="form-group" v-if="uploadType === 'file'">
      <label class="control-label" for="upload">Upload your file here</label>
      <input type="file" @change="loadFile($event.target.files)">
    </div>
    <div class="form-group" v-if="uploadType === 'url'">
      <label class="control-label" for="url">Or provide us an URL</label>
      <input class="form-control" id="url" type="text" v-model="url">
    </div>
    <hr />
    <button v-show="!uploadError" type="button" class="btn btn-primary pull-right" @click="uploadStart()">Submit</button>
  </form>
</template>

<script>
import config from "../../config.js";
import SparkMD5 from 'spark-md5';

let md5Buffer = new SparkMD5.ArrayBuffer();
let uploadSessionID;
let chunkSize;

export default {
  data() {
    return {
      file: '',
      url: '',
      uploadType: '',
      sentBytes: 0,
      totalBytes: 0,
      uploadError: false,
    };
  },
  methods: {
    uploadStart: function () {
      let jsonObject = {
        fileSize: this.file.size,
        fileName: this.file.name
      };

      this.$http.post(config.UPLOAD_START_URL, jsonObject).then((res) => {
        if (res.data.success) {
          uploadSessionID = res.data.uuid;
          chunkSize = res.data.chunkSize;
        }

        // Trigger a "start" event. I'm surprized !
        this.$dispatch("start");
        this.uploadNextChunk();
      });
    },

    uploadNextChunk: function () {
      let remainingBytes = this.totalBytes - this.sentBytes;
      let bufferSize = Math.min(remainingBytes, chunkSize, this.file.size);
      let buffer = this.file.slice(this.sentBytes, this.sentBytes + bufferSize);
      let reader = new FileReader();

      reader.addEventListener("loadend", () => {
        let fileArray = reader.result;
        this.$http.post(
          `${config.UPLOAD_CHUNK_URL}${uploadSessionID}/`, fileArray,
          {
            headers: {
              "Content-Type": "application/octet-stream"
            }
          }
        ).then((res) => {
          if (!res.data.success) {
            // Something went wrong
            this.uploadError = true;
            this.$dispatch("errorUpload");
            return;
          }

          if (res.data.remains != (remainingBytes - fileArray.byteLength)) {
            // Bytes sent & bytes received are not equals
            this.uploadError = true;
            this.$dispatch("bytesNotEquals");
            return;
          }

          md5Buffer.append(fileArray);
          this.sentBytes +=  fileArray.byteLength;
          this.progress();

          if (res.data.remains === 0) {
            this.uploadEnd();
          } else {
            this.uploadNextChunk();
          }
        });
      });

      reader.readAsArrayBuffer(buffer);
    },

    uploadEnd: function () {
      let hash = md5Buffer.end();
      this.$http.post(`${config.UPLOAD_END_URL}${uploadSessionID}/`, {md5: hash}).then((res) => {
        if (res.data.success) {
          sessionStorage.setItem("fileUUID", res.data.file_uuid);
          sessionStorage.setItem("price", res.data.price);
          this.$dispatch("end");
        } else {
          this.uploadError = true;
          this.$dispatch("errorUploadEnd", response.data.message);
        }
      });
    },

    progress: function () {
      let percentage = Math.round((this.sentBytes / this.totalBytes) * 100);
      this.$dispatch("errorUpload");
      this.$dispatch("progress", percentage);
    },

    loadFile: function (file) {
      file = file[0];
      this.file = file;
      this.totalBytes = this.file.size;
    }
  }
};
</script>
