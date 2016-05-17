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
      <div class="row margin-top">
        <template v-if="logged">
          <div class="col-sm-6">
            <h2>Your stockage</h2>
          </div>
          <div class="col-sm-6">
            <template v-for="file in last_files">
              <div class="row">
                <div class="col-sm-3 text-center">
                  <template v-if="isFileMusic(file)">
                    <span class="glyphicon glyphicon-music gl-x3" aria-hidden="true"></span>
                  </template>
                  <template v-else>
                    <span class="glyphicon glyphicon-film gl-x3" aria-hidden="true"></span>
                  </template>
                </div>
                <div class="col-sm-9">
                  <h3>{{ file.name }}</h3>
                  <p>Converted to : <b>{{ file.convert_to }}</b></p>
                </div>
              </div>
            </template>
          </div>
        </template>
        <template v-else>
          <div class="col-sm-6 text-center">
            <span class="glyphicon glyphicon-floppy-saved gl-x6" aria-hidden="true"></span>
            <h2><b>{{ converted_files }}</b> converted files all around the world</h2>
          </div>
          <div class="col-sm-6 text-center">
            <span class="glyphicon glyphicon-globe gl-x6" aria-hidden="true"></span>
            <h2><b>{{ registered_users }}</b> user trust the power of transcode</h2>
          </div>
        </template>
      </div>
    </div>
</template>

<script>
import Navbar from './pieces/Navbar'

export default {
  components: {
    Navbar
  },
  data () {
    return {
      logged: true,
      converted_files: 654654,
      registered_users: 89764,

      last_files: [
        {
          name: 'yolo.mp3',
          convert_to: 'wav',
          type: 'music'
        },
        {
          name: 'do_the_barrel_roll.mp4',
          convert_to: 'mp3',
          type: 'music'
        },
        {
          name: 'hello.m4v',
          convert_to: 'wmv',
          type: 'video'
        },
        {
          name: 'creep.wma',
          convert_to: 'mp3',
          type: 'music'
        },
        {
          name: 'lolilol.m4v',
          convert_to: 'wmv',
          type: 'video'
        }
      ]
    }
  },
  methods: {
    isFileMusic: function (file) {
      return file.type !== 'video'
    }
  }
}
</script>

<style>
  .margin-top {
    margin-top: 80px;
  }

  .gl-x3 {
    font-size: 4em;
    margin-top: 20px;
  }

  .gl-x6 {
    font-size: 6em;
  }
</style>
