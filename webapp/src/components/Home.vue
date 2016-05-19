<template>
  <div id="app">
    <navbar></navbar>
    <hello></hello>
</template>

<script>
import Hello from './pieces/Hello'

export default {
  components: {
    Hello
  }
}
</script>

<style scope>
  .navbar {
    margin-bottom: 0px;
  }
</style>
