<template>
  <div id="app">
    <navbar></navbar>
    <hello></hello>
</template>

<script>
import Navbar from './pieces/Navbar'
import Hello from './pieces/Hello'

export default {
  components: {
    Navbar,
    Hello
  }
}
</script>

<style scope>
  .navbar {
    margin-bottom: 0px;
  }
</style>
