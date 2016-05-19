import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from './components/Home'
import Connect from './components/Connect'
import Register from './components/Register'
import Convert from './components/Convert'
import auth from "./auth";

Vue.use(VueRouter)

auth.checkAuth();

Vue.http.headers.common["Authorization"] = auth.getAuthHeader();
let App = Vue.extend({})
let router = new VueRouter({
  history: true
})

router.map({
  '/': {
    name: 'home',
    component: Home
  },
  '/connect': {
    name: 'connect',
    component: Connect
  },
  '/register': {
    name: 'register',
    component: Register
  },
  '/convert': {
    name: 'convert',
    component: Convert
  }
})

router.start(App, '#app')
