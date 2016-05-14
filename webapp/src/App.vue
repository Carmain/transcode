<template>
  <div id="app">
    <navbar></navbar>
    <div class ="container">
      <hello></hello>
    </div>
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
