<template>
  <div id="app">
    <navbar></navbar>
    <div class ="container">
      <h1>Connection</h1>
      <form role="form">
        <div class="form-group label-floating">
          <label class="control-label" for="email">Email address</label>
          <input class="form-control" id="email" type="email">
          <p class="help-block">You should really write something here</p>
        </div>
        <div class="form-group label-floating">
          <label class="control-label" for="password">Password</label>
          <input class="form-control" id="password" type="password">
          <p class="help-block">You should really write something here</p>
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
