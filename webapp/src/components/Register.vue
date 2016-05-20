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
            <input class="form-control" id="email" type="email" v-model="credentials.email" @change="getGravatar()">
          </div>
        </div>
        <div class="col-md-2 col-sm-3 col-xs-4">
          <a href="https://gravatar.com" title="Gravatar" target="_blank">
            <img v-bind:src="gravatar" class="img-responsive center-block"/>
          </a>
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
      <button type="submit" class="btn btn-raised btn-primary pull-right">Submit</button>
    </form>
  </div>
</template>

<script>
import md5 from 'blueimp-md5'

  export default {
    data () {
      return {
        gravatar_url: 'http://www.gravatar.com/avatar/',
        credentials: {
          username: '',
          email: '',
          first_name: '',
          last_name: '',
          birthdate: '',
          password: '',
          password_confirmation: ''
        }
      }
    },
    computed: {
      gravatar: function() {
        return this.gravatar_url + '?s=130'
      }
    },
    methods: {
      getGravatar () {
        let email = this.credentials.email;
        if (email != '') {
          let hash = md5(email);
          this.gravatar_url = 'http://www.gravatar.com/avatar/' + hash;
        }
      }
    }
  };
</script>
