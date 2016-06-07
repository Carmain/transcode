<template>
  <div class="col-sm-6">
    <h2>Your stockage</h2>
    <memory width="400" height="350"></memory>
  </div>
  <div class="col-sm-6">
    <h2>Your last converted files</h2>
    <template v-for="file in last_files">
      <div class="row">
        <div class="col-sm-3 col-xs-3 text-center">
          <template v-if="isFileMusic(file)">
            <span class="glyphicon glyphicon-music gl-x3" aria-hidden="true"></span>
          </template>
          <template v-else>
            <span class="glyphicon glyphicon-film gl-x3" aria-hidden="true"></span>
          </template>
        </div>
        <div class="col-sm-9 col-xs-9">
          <h3>{{ file.transcode_file.name }}</h3>
          <p>Converted to : <b>{{ file.fileType }}</b></p>
        </div>
      </div>
      <hr />
    </template>
  </div>
</template>

<script>
import Memory from './Memory';
import config from "../../config.js";

export default {
  components: {
    Memory
  },
  data () {
    return {
      last_files: []
    };
  },
  ready () {
    this.$http.get(config.CONVERTED_FILES + '4/').then((res) => {
      console.log(res.data);
      this.last_files = res.data;
    });
  },
  methods: {
    isFileMusic: function (file) {
      return file.transcode_file.media_type !== 'video';
    }
  }
};
</script>
