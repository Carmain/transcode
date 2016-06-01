<template>
  <div class ="container">
    <h1>Convert</h1>
    <upload-form></upload-form>
    <div class="row margin-top">
      <template v-if="user.authenticated">
        <convert-logged></convert-logged>
      </template>
      <template v-else>
        <convert-guest></convert-guest>
      </template>
    </div>
  </div>
</template>

<script>
import ConvertGuest from './pieces/ConvertGuest';
import ConvertLogged from './pieces/ConvertLogged';
import UploadForm from './pieces/UploadForm';
import auth from '../auth';

export default {
  components: {
    ConvertGuest,
    ConvertLogged,
    UploadForm
  },
  data () {
    return {
      user: auth.user,
    };
  },
  methods: {
    uploadFile: function() {

    }
  }
};
</script>

<style>

  hr {
    margin-bottom: 10px;
  }

  .margin-top {
    margin-top: 30px;
  }

  .upload-choice {
    height: 60px;
  }

  .gl-x3 {
    font-size: 4em;
    padding-top: 20px;
  }

  .gl-x12 {
    font-size: 12em;
  }
</style>
