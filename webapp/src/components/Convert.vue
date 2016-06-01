<template>
  <div class ="container">
    <h1>Convert</h1>
    <form enctype="multipart/form-data">

      <div class="row">
        <div class="form-group col-md-6 col-sm-6">
          <label class="control-label" for="url">Provide us an URL</label>
          <input class="form-control" id="url" type="text">
        </div>
        <div class="form-group col-md-6 col-sm-6">
          <label class="control-label" for="upload">Or upload your file here</label>
          <input type="file" id="upload">
        </div>
      </div>

      <div class="form-group">
        <label class="control-label" for="convert-type">I want my file converted into</label>
        <select class="form-control" id="convert-type">
          <optgroup label="Audio">
            <template v-for="extension in audio">
              <option v-bind:value="extension">{{ extension }}</option>
            </template>
          </optgroup>
          <optgroup label="Video">
            <template v-for="extension in video">
              <option v-bind:value="extension">{{ extension }}</option>
            </template>
          </optgroup>
        </select>
      </div>

      <button type="button" class="btn btn-primary pull-right" @click="uploadFile()">Submit</button>
    </form>

    <div class="row margin-top">
      <template v-if="user.authenticated">
        <convert-logged></convert-logged>
      </template>
      <template v-else>
        <convert-guest></convert-guest>
      </template>
    </div>
  </div>
</template>

<script>
import ConvertGuest from './pieces/Convert_guest';
import ConvertLogged from './pieces/Convert_logged';
import auth from '../auth';

export default {
  components: {
    ConvertGuest,
    ConvertLogged
  },
  data () {
    return {
      user: auth.user,
      audio: ['MP3', 'MPEG4', 'WAV'],
      video: ['VID', 'YOLO', 'HUHU']
    };
  },
  methods: {
    uploadFile: function() {

    }
  }
};
</script>

<style>

  hr {
    margin-bottom: 10px;
  }

  .margin-top {
    margin-top: 30px;
  }

  .gl-x3 {
    font-size: 4em;
    padding-top: 20px;
  }

  .gl-x12 {
    font-size: 12em;
  }
</style>
