<template>
  <div class="navbar navbar-default">
    <div class="navbar-header">
      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-responsive-collapse">
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand" v-link="{ path:'/'}">Home</a>
    </div>
    <div class="navbar-collapse collapse navbar-right navbar-responsive-collapse">
      <ul class="nav navbar-nav">
        <li><a v-link="{ path:'/connect'}">Connect</a></li>
        <li><a v-link="{ path:'/register'}">Register</a></li>
        <li><a v-link="'connect'">Connect</a></li>
        <li><a v-link="'register'">Register</a></li>
      </ul>
    </div>
  </div>
</template>
