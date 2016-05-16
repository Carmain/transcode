<template>
  <div id="app">
    <navbar></navbar>
    <div class ="container">
      <h1>Convert</h1>
      <div class="form-group">
        <label class="control-label" for="inputFile2">Your file here</label>
        <input type="file" id="inputFile2" multiple="">
        <input type="text" readonly="" class="form-control" placeholder="Please give us the file you want to convert...">
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
