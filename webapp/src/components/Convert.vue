<template>
  <div id="app">
    <div class ="container">
      <h1>Convert</h1>

      <div class="form-group">
        <label class="control-label" for="upload">Upload your file here</label>
        <input type="file" id="upload">
      </div>

      <div class="form-group">
        <label class="control-label" for="url">Or provide us an URL</label>
        <input class="form-control" id="url" type="text">
      </div>

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
import ConvertGuest from './pieces/Convert_guest'
import ConvertLogged from './pieces/Convert_logged'
import auth from '../auth'

export default {
  components: {
    ConvertGuest,
    ConvertLogged
  },
  data () {
    return {
      user: auth.user
    }
  }
}
</script>

<style>

  hr {
    margin-bottom: 10px;
  }

  .margin-top {
    margin-top: 30px;
  }

  .gl-x3 {
    font-size: 4em;
    padding-top: 20px;
  }

  .gl-x12 {
    font-size: 12em;
  }
</style>
