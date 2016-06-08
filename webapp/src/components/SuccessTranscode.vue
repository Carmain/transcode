<template>
  <div class="forofor">
    <div class ="container">
      <div class="text-center white">
        <h1 class="title-error">Success !</h1>
        <h2>The uploaded file is being processed. <b>We will send you a message when the conversion is complete.</b></h2>
      </div>
    </div>
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

<style scoped>
  .white {
    color: white;
  }

  .title-error {
    font-size: 200px;
    font-weight: bold;
    margin-top: 150px;
  }

  .forofor {
    position: fixed;
    width: 100%;
    height: 100%;
    left: 0;
    top: 0;
    background-image: url("../assets/dance_drake.gif");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
  }
</style>
