<template>
  <div class ="container">
    <h1>Success !</h1>
  </div>
</template>

<script>
import auth from '../auth';

export default {
  data () {
    return {

    };
  },
  ready () {
    sessionStorage.removeItem("fileUUID");
    sessionStorage.removeItem("price");
  },
  route: {
    canActivate(transition) {
      let uuid = sessionStorage.getItem("fileUUID");
      let paramUUID = transition.to.params.fileUUID;
      return auth.user.authenticated && (paramUUID == uuid);
    }
  }
};
</script>
