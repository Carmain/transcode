<template>
  <div class="col-sm-6">
    <h2>Your stockage</h2>
    <memory width="400" height="350"></memory>
  </div>
  <div class="col-sm-6">
    <h2>Your last converted files</h2>
    <template v-for="file in last_files">
      <div class="row">
        <div class="col-sm-3 col-xs-3 text-center">
          <template v-if="isFileMusic(file)">
            <span class="glyphicon glyphicon-music gl-x3" aria-hidden="true"></span>
          </template>
          <template v-else>
            <span class="glyphicon glyphicon-film gl-x3" aria-hidden="true"></span>
          </template>
        </div>
        <div class="col-sm-9 col-xs-9">
          <h3>{{ file.name }}</h3>
          <p>Converted to : <b>{{ file.convert_to }}</b></p>
        </div>
      </div>
      <hr />
    </template>
  </div>
</template>

<script>
import Memory from './Memory';

export default {
  components: {
    Memory
  },
  data () {
    return {
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
    };
  },
  methods: {
    isFileMusic: function (file) {
      return file.type !== 'video';
    }
  }
};
</script>
