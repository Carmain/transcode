<template>
  <div id="app">
    <navbar></navbar>
    <hello></hello>
</template>

<script>
import Navbar from './components/Navbar'
import Hello from './components/Hello'

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
