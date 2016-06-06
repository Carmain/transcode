<template>
  <div class="col-sm-6 text-center">
    <span class="glyphicon glyphicon-floppy-saved gl-x12" aria-hidden="true"></span>
    <h2><b>{{ converted_files }}</b> converted files all around the world</h2>
  </div>
  <div class="col-sm-6 text-center">
    <span class="glyphicon glyphicon-globe gl-x12" aria-hidden="true"></span>
    <h2><b>{{ registered_users }}</b> users trust the power of transcode</h2>
  </div>
</template>

<script>
import config from "../../config.js";

export default {
  data () {
    return {
      converted_files: '',
      registered_users: ''
    };
  },
  ready () {
    this.$http.get(config.STATISTICS).then((res) => {
      this.converted_files = res.data.converted_files;
      this.registered_users = res.data.users;
    });
  },
};
</script>
