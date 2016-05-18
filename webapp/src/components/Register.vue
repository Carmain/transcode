<template>
  <div id="app">
    <navbar></navbar>
    <div class ="container">
      <h1>Registration</h1>
      <form role="form">
        <div class="form-group">
          <label class="control-label" for="first-name">First name</label>
          <input class="form-control" id="first-name" type="text">
        </div>
        <div class="form-group">
          <label class="control-label" for="last-name">Last name</label>
          <input class="form-control" id="last-name" type="text">
        </div>
        <div class="form-group">
          <label class="control-label" for="email">Email address</label>
          <input class="form-control" id="email" type="email">
        </div>
        <hr />
        <div class="form-group">
          <label class="control-label" for="password">Password</label>
          <input class="form-control" id="password" type="password">
        </div>
        <div class="form-group">
          <label class="control-label" for="password-confirm">Confirm password</label>
          <input class="form-control" id="password-confirm" type="password">
        </div>
        <div class="checkbox">
          <label>
            <input type="checkbox"> Remember me
          </label>
        </div>
        <button type="submit" class="btn btn-raised btn-primary pull-right">Submit</button>
      </form>
    </div>
  </div>
</template>

<script>
import Navbar from './pieces/Navbar'

export default {
  components: {
    Navbar
  }
}
</script>
