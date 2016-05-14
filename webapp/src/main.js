import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from './Home'
import Connect from './Connect'
import Register from './Register'

Vue.use(VueRouter)

var App = Vue.extend({})
var router = new VueRouter()

router.map({
  '/': {
    component: Home
  },
  '/connect': {
    component: Connect
  },
  '/register': {
    component: Register
  }
})

router.start(App, '#app')

/* eslint-disable no-new */
// new Vue({
//   el: 'body',
//   components: { Home }
// })
