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
            <button type="button" class="btn btn-danger btn-xs" @click="remove()">
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
    this.$http.get(config.CONVERTED_FILES).then((res) => {
      console.log(res.data);
      this.files = res.data;
    });
  },
  methods: {
    isFileMusic: function (file) {
      return file.transcode_file.media_type !== 'video';
    },

    formattedDate(date) {
      return moment(date).format('LLL');
    },

    remove: function () {
      alert("Remove");
    }
  }
};
</script>
