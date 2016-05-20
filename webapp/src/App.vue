<template>
  <div id="app">
    <navbar></navbar>
    <template v-if='authState.checked'>
      <router-view></router-view>
    </template>
  </div>
</template>

<script>
import Navbar from './components/pieces/Navbar'
import auth from './auth';

export default {
  components: {
    Navbar
  },
  data() {
    return {
      authState: auth.state
    };
  }
}
</script>
