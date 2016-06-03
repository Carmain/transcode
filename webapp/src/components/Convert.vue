<template>
  <div class ="container">
    <h1>Convert</h1>
    <upload-form></upload-form>
    <div class="row margin-top">

      <template v-if="uploadStarted">
        <h3>The upload started</h3>
        <div class="progress">
          <!-- TODO: style="width:{{progress}}%" doesn't work with internet explorer -->
          <div class="progress-bar" role="progressbar" aria-valuenow="{{progress}}" aria-valuemin="0" aria-valuemax="100" style="width:{{progress}}%">
            {{progress}}%
          </div>
        </div>
      </template>
      <template v-else>
        <template v-if="user.authenticated">
          <convert-logged></convert-logged>
        </template>
        <template v-else>
          <convert-guest></convert-guest>
        </template>
      </template>

      <template v-if="uploadEnded">
        <template v-if="!user.authenticated">
          <h2>Upload succeed !</h2>
          <p>
            The file was uploaded successfully. If you want to convert it, you need to log in.
          </p>
          <a v-link="'connect'" class="btn btn-default" role="button">Login</a>
          <a v-link="'register'" class="btn btn-primary" role="button">Register</a>
        </template>
      </template>
    </div>
    <template v-for="sentence in messages_content">
      <message tag="danger" title="Waning" v-bind:message="sentence"></message>
    </template>
  </div>
</template>

<script>
import ConvertGuest from './pieces/ConvertGuest';
import ConvertLogged from './pieces/ConvertLogged';
import UploadForm from './pieces/UploadForm';
import Message from './pieces/Message';
import auth from '../auth';

export default {
  components: {
    ConvertGuest,
    ConvertLogged,
    UploadForm,
    Message
  },
  data () {
    return {
      user: auth.user,
      uploadStarted: false,
      uploadEnded: false,
      progress: 0,
      messages_content: []
    };
  },
  events: {
    'start': 'uploadStarted',
    'errorUpload': 'displayError',
    'bytesNotEquals': 'displayError',
    'progress': 'getProgression',
    'end': 'uploadEnd'
  },
  methods: {
    uploadStarted: function() {
      this.uploadStarted = true;
    },
    displayError: function() {
      this.messages_content.push("Something Went wrong with the upload");
    },
    getProgression: function(percentage) {
      this.progress = percentage;
    },
    uploadEnd: function() {
      this.uploadEnded = true;
      if(this.user.authenticated) {
        this.$route.router.go('payment');
      }
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
