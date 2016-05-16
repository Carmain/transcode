import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from './Home'
import Connect from './Connect'
import Register from './Register'

Vue.use(VueRouter)

var App = Vue.extend({})
var router = new VueRouter({
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
  }
})

router.start(App, '#app')
