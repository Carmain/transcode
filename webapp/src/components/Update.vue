<template>
  <div class ="container">
    <h1>Update my profile</h1>
    <ul class="nav nav-tabs">
      <li class="active"><a data-toggle="tab" href="#personal-data">Your profile</a></li>
      <li><a data-toggle="tab" href="#password">Security</a></li>
    </ul>

    <div class="tab-content">
      <div id="personal-data" class="tab-pane fade in active">
        <h2>Update my profile</h2>
        <form role="form">
          <div class="row">
            <div class="col-md-10 col-sm-9 col-xs-8">
              <div class="form-group">
                <label class="control-label" for="email">Email</label>
                <input class="form-control" id="email" type="email" v-model="user.email">
              </div>
              <div class="form-group">
                <label class="control-label" for="birthdate">Birthdate</label>
                <input class="form-control" id="birthdate" type="date" v-model="user.birthdate">
              </div>
            </div>
            <div class="col-md-2 col-sm-3 col-xs-4">
              <gravatar size='130' v-bind:email='user.email'></gravatar>
            </div>
          </div>
          <div class="row">
            <div class="form-group col-md-6 col-sm-6">
              <label class="control-label" for="first-name">First name</label>
              <input class="form-control" id="first-name" type="text" v-model="user.first_name">
            </div>
            <div class="form-group col-md-6 col-sm-6">
              <label class="control-label" for="last-name">Last name</label>
              <input class="form-control" id="last-name" type="text" v-model="user.last_name">
            </div>
          </div>
          <button type="button" class="btn btn-raised btn-primary pull-right" @click="updateProfile()">Submit my modifications</button>
        </form>
      </div>
      <div id="password" class="tab-pane fade">
        <h2>Security</h2>

        <fieldset>
          <legend>
            <h3>Change my password</h3>
          </legend>
          <form>
            <div class="form-group">
              <label class="control-label" for="password">Password</label>
              <input class="form-control" id="password" type="password" v-model="password.oldPassword">
            </div>
            <hr />
            <div class="form-group">
              <label class="control-label" for="new-password">New password</label>
              <input class="form-control" id="new-password" type="password" v-model="password.newPassword">
            </div>
            <button type="button" class="btn btn-raised btn-primary pull-right" @click="updatePassword()">Submit</button>
          </form>
        </fieldset>
      </div>
    </div>

    <div class="message-handler">
      <message v-for="sentence in messages" v-bind:tag="tag" v-bind:title="title" v-bind:message="sentence"></message>
    </div>
  </div>
</template>

<style scoped>
  .message-handler {
    margin-top: 60px;
  }
</style>

<script>
import auth from '../auth';
import config from '../config';
import Gravatar from './pieces/Gravatar';
import Message from './pieces/Message';
import moment from "moment";

export default {
  components: {
    Gravatar,
    Message
  },
  data () {
    return {
      tag: '',
      title: '',
      messages: [],
      user: {
        email: '',
        first_name: '',
        last_name: '',
        birthdate: ''
      },

      password: {
        oldPassword: '',
        newPassword: ''
      }
    };
  },
  ready () {
    this.$http.get(config.PROFILE_URL).then((res) => {
      this.user.email = res.data.email;
      this.user.first_name = res.data.first_name;
      this.user.last_name = res.data.last_name;
      this.user.birthdate = moment(res.data.birthdate).format('YYYY-MM-DD');
    });
  },
  methods: {
    updateProfile: function() {
      this.messages = [];
      this.$http.post(config.UPDATE_PROFILE_URL, this.password).then((res) => {
        if(res.data.success) {
          this.tag = "success";
          this.title = "Success";
          this.messages.push("Your profile has been updated !");
        } else {
          this.tag = "danger";
          this.title = "Warning";
          this.messages.push("An error occured with the update of the profile.");
        }
      });
    },

    updatePassword: function() {
      this.messages = [];
      this.$http.post(config.UPDATE_PASSWORD_URL, this.password).then((res) => {
        if(res.data.success) {
          this.tag = "success";
          this.title = "Success";
          this.messages.push("Your password has been updated !");
        } else {
          this.tag = "danger";
          this.title = "Warning";
          this.messages.push("An error occured with the update of the password.");
        }
      });
    }
  },
  route: {
    canActivate() {
      return auth.user.authenticated;
    }
  }
};

</script>
