<template>
  <div class ="container">
    <h1>Connection</h1>
    <form role="form">
      <div class="form-group">
        <label class="control-label" for="username">Username</label>
        <input class="form-control" id="username" type="text" v-model="credentials.username">
      </div>
      <div class="form-group">
        <label class="control-label" for="password">Password</label>
        <input class="form-control" id="password" type="password" v-model="credentials.password">
      </div>
      <button type="button" class="btn btn-primary pull-right" @click="submit()">Submit</button>
    </form>

    <div class="error-handler">
      <message v-for="sentence in login_errors" tag="danger" title="Waning" v-bind:message="sentence"></message>
    </div>
  </div>
</template>

<style scoped>
  .error-handler {
    margin-top: 60px;
  }
</style>

<script>
import auth from '../auth';
import Message from './pieces/Message';

export default {
  components: {
    Message
  },
  data () {
    return {
      login_errors: [],
      credentials: {
        username: '',
        password: ''
      }
    };
  },
  methods: {
    submit () {
      auth.login(this.credentials, '/').catch(
        e => {
          this.login_errors.push("Wrong credentials");
        }
      );
    }
  },
  route: {
    canActivate() {
      return !auth.user.authenticated;
    }
  }
};
</script>
