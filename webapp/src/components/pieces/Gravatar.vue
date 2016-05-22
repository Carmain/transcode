<template>
  <a href="https://gravatar.com" title="Gravatar" target="_blank">
    <img v-bind:src="gravatar" class="img-responsive center-block"/>
  </a>
</template>

<script>
import md5 from 'blueimp-md5'

export default {
  props: [
    'email',
    'size'
  ],
  data () {
    return {
      gravatar_url: 'http://www.gravatar.com/avatar/',
    }
  },
  computed: {
    gravatar: function() {
      let email = this.email;
      let url = this.gravatar_url;
      if (email != '') {
        let hash = md5(email);
        url = 'http://www.gravatar.com/avatar/' + hash;
      }

      return url + '?s=' + this.size;
    }
  }
}
</script>
