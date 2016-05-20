<template>
    <template v-if="user.authenticated">
      <div class="container">
        <homepage></homepage>
      </div>
    </template>
    <template v-else>
      <welcome></welcome>
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
