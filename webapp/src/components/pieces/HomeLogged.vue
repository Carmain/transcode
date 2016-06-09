<template>
  <h1 class="title">Welcome</h1>
  <table class="table table-striped">
    <thead>
      <tr>
        <th></th>
        <th>File name</th>
        <th>Converted into</th>
        <th>Date</th>
        <th></th>
      </tr>
    </thead>
    <tbody>
      <template v-for="file in files">
        <tr>
          <td>
            <template v-if="isFileMusic(file)">
              <span class="glyphicon glyphicon-music" aria-hidden="true"></span>
            </template>
            <template v-else>
              <span class="glyphicon glyphicon-film" aria-hidden="true"></span>
            </template>
          </td>
          <td>{{ file.transcode_file.name }}</td>
          <td>{{ file.fileType }}</td>
          <td>{{ formattedDate(file.date) }}</td>
          <td>
            <button type="button" class="btn btn-info btn-xs" @click="download(file.file_uuid)">
              Download
            </button>
            <button type="button" class="btn btn-danger btn-xs" @click="remove(file.transcode_file.uuid)">
              Remove
            </button>
          </td>
        </tr>
      </template>
    </tbody>
  </table>
</template>

<script>
import config from "../../config.js";
import moment from "moment";

export default {
  data () {
    return {
      files: []
    };
  },
  ready () {
    this.getAllTheConvertedFiles();
  },
  methods: {
    getAllTheConvertedFiles: function() {
      this.$http.get(config.CONVERTED_FILES).then((res) => {
        this.files = res.data;
      });
    },

    isFileMusic: function (file) {
      return file.transcode_file.media_type !== 'video';
    },

    formattedDate(date) {
      return moment(date).format('LLL');
    },

    download: function(uuid) {
      window.location = config.DOWNLOAD_CONVERTED_FILE + uuid + "/";
    },

    downloadLink: function(uuid) {
      return config.DOWNLOAD_CONVERTED_FILE + uuid + "/";
    },

    remove: function (uuid) {
      this.$http.delete(config.DELETE_CONVERTED_FILE + uuid + "/").then((res) => {
        if (res.data.success) {
          this.getAllTheConvertedFiles();
        }
      });
    }
  }
};
</script>
