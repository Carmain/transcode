<template>
  <div id="app">
    <template v-if="user.authenticated">
      <homepage></homepage>
    </template>
    <template v-else>
      <hello></hello>
    </template>
</template>

<script>
import Hello from './pieces/Hello'
import Homepage from './pieces/Homepage'
import auth from '../auth'

export default {
  data () {
    return {
      user: auth.user
    }
  },
  components: {
    Hello,
    Homepage
  }
}
</script>
