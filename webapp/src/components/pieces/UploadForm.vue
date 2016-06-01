<template>
  <input type="file" @change="loadFile($event.target.files)">
  <button type="button" @click="uploadStart()">Submit</button>
</template>

<script>
import config from "../../config.js";

let md5Buffer = new SparkMD5.ArrayBuffer();
let uploadSessionID;
let chunkSize;

export default {
  data() {
    return {
      file: "",
      sentBytes: 0,
      totalBytes: 0
    };
  },
  methods: {
    uploadStart: function () {
      this.$http.get(config.UPLOAD_START_URL).then((res) => {
        if (res.success) {
          uploadSessionID = res.uuid;
          chunkSize = res.chunkSize;
        }

        this.$dispatch("start");
        this.uploadNextChunk();
      });
    },
    uploadNextChunk: function () {
      let remainingBytes = this.totalBytes - this.sentBytes;
      let buffer = this.file.slice(this.sentBytes, Math.min(remainingBytes, chunkSize));

      this.$ttp.post(
        `${config.UPLOAD_CHUNK_URL}${uploadSessionID}/`,
        buffer,
        {
          headers: {
            "Content-Type": "application/octet-stream"
          }
        }
      )
      .then((res) => {
        if (!res.success) {
          // Something went wrong
          return;
        }

        if (res.remains != (remainingBytes -  chunkSize)) {
          // Bytes sent & bytes received are not equals
          return;
        }

        md5Buffer.append(buffer);
        this.sentBytes +=  buffer.length;
        this.progress();

        if (res.remains === 0) {
          this.uploadEnd();
        } else {
          this.uploadNextChunk();
        }
      });
    },
    uploadEnd: function () {
      let hash = md5Buffer.end();

      this.$ttp.post(`${config.UPLOAD_CHUNK_URL}${uploadSessionID}/`, {md5: hash}).then((res) => {
        if (res.success) {
          this.$dispatch("end");
        }
      });
    },
    progress: function () {
      let percentage = Math.round((this.totalBytes / this.sentBytes) * 100);
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
