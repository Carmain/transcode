<template>
  <div id="app">
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
        <div class="checkbox">
          <label>
            <input type="checkbox"> Remember me
          </label>
        </div>
        <button type="button" class="btn btn-raised btn-primary pull-right" @click="submit()">Submit</button>
      </form>
    </div>
  </div>
</template>

<script>
import auth from '../auth'

export default {
  data () {
    return {
      credentials: {
        username: '',
        password: ''
      }
    }
  },
  methods: {
    submit () {
      auth.login(this.credentials, '/')
    }
  }
}
</script>
