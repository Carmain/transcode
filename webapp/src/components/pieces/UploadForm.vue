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

    <div class="form-group">
      <label class="control-label" for="convert-type">I want my file converted into</label>
      <select class="form-control" id="convert-type">
        <optgroup label="Audio">
          <template v-for="extension in format.audio">
            <option v-bind:value="extension">{{ extension }}</option>
          </template>
        </optgroup>
        <optgroup label="Video">
          <template v-for="extension in format.video">
            <option v-bind:value="extension">{{ extension }}</option>
          </template>
        </optgroup>
      </select>
    </div>

    <button type="button" class="btn btn-primary pull-right" @click="uploadStart()">Submit</button>
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
      format: {
        audio: ['MP3', 'MPEG4', 'WAV'],
        video: ['VID', 'YOLO', 'HUHU']
      },
      sentBytes: 0,
      totalBytes: 0
    };
  },
  methods: {
    uploadStart: function () {
      this.$http.post(config.UPLOAD_START_URL, {fileSize: this.file.size}).then((res) => {
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
            this.$dispatch("errorUpload");
            return;
          }

          if (res.data.remains != (remainingBytes - fileArray.byteLength)) {
            // Bytes sent & bytes received are not equals
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
          this.$dispatch("end");
        }
      });
    },

    progress: function () {
      let percentage = Math.round((this.sentBytes / this.totalBytes) * 100);
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
