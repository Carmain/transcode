<template>
  <div class="col-sm-6 text-center">
    <span class="glyphicon glyphicon-floppy-saved gl-x12" aria-hidden="true"></span>
    <h2><b>{{ converted_files }}</b> converted files all around the world</h2>
  </div>
  <div class="col-sm-6 text-center">
    <span class="glyphicon glyphicon-globe gl-x12" aria-hidden="true"></span>
    <h2><b>{{ registered_users }}</b> user trust the power of transcode</h2>
  </div>
</template>

<script>
export default {
  data () {
    return {
      converted_files: 654654,
      registered_users: 89764,
    };
  }
};
</script>
