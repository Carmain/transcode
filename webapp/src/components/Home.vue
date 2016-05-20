<template>
  <div id="app">
    <template v-if="user.authenticated">
      <home-logged></home-logged>
    </template>
    <template v-else>
      <home-guest></home-guest>
    </template>
</template>

<script>
import Welcome from './pieces/Home_Guest'
import Homepage from './pieces/Home_logged'
import auth from '../auth'

export default {
  data () {
    return {
      user: auth.user
    }
  },
  components: {
    Welcome,
    Homepage
  }
}
</script>
