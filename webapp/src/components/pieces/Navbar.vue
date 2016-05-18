<template>
  <nav class="navbar navbar-default navbar-static-top">
    <div class="container-fluid">
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
          <li><a v-link="'connect'">Connect</a></li>
          <li><a v-link="'register'">Register</a></li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<style scope>
  .navbar-default {
    background-color: #3f51b5;
    border-color: #3649b4;
  }
  .navbar-default .navbar-brand {
    color: #ecf0f1;
  }
  .navbar-default .navbar-brand:hover,
  .navbar-default .navbar-brand:focus {
    color: #cbd0ec;
  }
  .navbar-default .navbar-text {
    color: #ecf0f1;
  }
  .navbar-default .navbar-nav > li > a {
    color: #ecf0f1;
  }
  .navbar-default .navbar-nav > li > a:hover,
  .navbar-default .navbar-nav > li > a:focus {
    color: #cbd0ec;
  }
  .navbar-default .navbar-nav > .active > a,
  .navbar-default .navbar-nav > .active > a:hover,
  .navbar-default .navbar-nav > .active > a:focus {
    color: #cbd0ec;
    background-color: #3649b4;
  }
  .navbar-default .navbar-nav > .open > a,
  .navbar-default .navbar-nav > .open > a:hover,
  .navbar-default .navbar-nav > .open > a:focus {
    color: #cbd0ec;
    background-color: #3649b4;
  }
  .navbar-default .navbar-toggle {
    border-color: #3649b4;
  }
  .navbar-default .navbar-toggle:hover,
  .navbar-default .navbar-toggle:focus {
    background-color: #3649b4;
  }
  .navbar-default .navbar-toggle .icon-bar {
    background-color: #ecf0f1;
  }
  .navbar-default .navbar-collapse,
  .navbar-default .navbar-form {
    border-color: #ecf0f1;
  }
  .navbar-default .navbar-link {
    color: #ecf0f1;
  }
  .navbar-default .navbar-link:hover {
    color: #cbd0ec;
  }

  @media (max-width: 767px) {
    .navbar-default .navbar-nav .open .dropdown-menu > li > a {
      color: #ecf0f1;
    }
    .navbar-default .navbar-nav .open .dropdown-menu > li > a:hover,
    .navbar-default .navbar-nav .open .dropdown-menu > li > a:focus {
      color: #cbd0ec;
    }
    .navbar-default .navbar-nav .open .dropdown-menu > .active > a,
    .navbar-default .navbar-nav .open .dropdown-menu > .active > a:hover,
    .navbar-default .navbar-nav .open .dropdown-menu > .active > a:focus {
      color: #cbd0ec;
      background-color: #3649b4;
    }
  }
</style>
