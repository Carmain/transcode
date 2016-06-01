<template>
  <div class ="container">
    <h1>Registration</h1>
    <form role="form">
      <div class="row">
        <div class="col-md-10 col-sm-9 col-xs-8">
          <div class="form-group">
            <label class="control-label" for="username">Username</label>
            <input class="form-control" id="username" type="text" v-model="credentials.username">
          </div>
          <div class="form-group">
            <label class="control-label" for="email">Email address</label>
            <input class="form-control" id="email" type="email" v-model="credentials.email">
          </div>
        </div>
        <div class="col-md-2 col-sm-3 col-xs-4">
          <gravatar size='130' v-bind:email='credentials.email'></gravatar>
        </div>
      </div>
      <div class="row">
        <div class="form-group col-md-6 col-sm-6">
          <label class="control-label" for="first-name">First name</label>
          <input class="form-control" id="first-name" type="text" v-model="credentials.first_name">
        </div>
        <div class="form-group col-md-6 col-sm-6">
          <label class="control-label" for="last-name">Last name</label>
          <input class="form-control" id="last-name" type="text" v-model="credentials.last_name">
        </div>
      </div>
      <div class="form-group">
        <label class="control-label" for="birthdate">Birthdate</label>
        <input class="form-control" id="birthdate" type="date" v-model="credentials.birthdate">
      </div>
      <hr />
      <div class="form-group">
        <label class="control-label" for="password">Password</label>
        <input class="form-control" id="password" type="password" v-model="credentials.password">
      </div>
      <div class="form-group">
        <label class="control-label" for="password-confirm">Confirm password</label>
        <input class="form-control" id="password-confirm" type="password" v-model="credentials.password_confirmation">
      </div>

      <vue-recaptcha v-bind:key="recaptcha_pub_key" @verify="onVerify"></vue-recaptcha>
      <button type="button" class="btn btn-primary pull-right" @click="register()">Submit</button>
    </form>

    <div class="error-handler">
      <template v-for="sentence in messages_content">
        <message tag="danger" title="Waning" v-bind:message="sentence"></message>
      </template>
    </div>
  </div>
</template>

<style scoped>
  .error-handler {
    margin-top: 50px;
  }
</style>

<script>
import VueRecaptcha from 'vue-recaptcha';
import Gravatar from './pieces/Gravatar';
import Message from './pieces/Message';
import config from "../config.js";
import auth from '../auth';

export default {
  components: {
    Gravatar,
    VueRecaptcha,
    Message
  },
  data () {
    return {
      credentials: {
        username: '',
        email: '',
        first_name: '',
        last_name: '',
        birthdate: '',
        password: '',
        password_confirmation: '',
        recaptcha_verify: ''
      },
      messages_content: [],
      recaptcha_pub_key : config.RECAPTCHA_PUBLIC_KEY
    };
  },
  methods: {
    register: function() {
      let register_url = config.REGISTER_URL;
      this.$http.post(register_url, this.credentials).then(
        function (response) {
          auth.login(this.credentials, '/');
        },
        function (response) {
          this.messages_content = response.data.error_messages;
        }
      );
    },
    onVerify: function(response) {
      this.credentials.recaptcha_verify = response;
    }
  }
};
</script>
