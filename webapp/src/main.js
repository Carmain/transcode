import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from './Home'

Vue.use(VueRouter)

var App = Vue.extend({})
var router = new VueRouter()

router.map({
  '/': {
    component: Home
  }
})

router.start(App, '#app')

/* eslint-disable no-new */
// new Vue({
//   el: 'body',
//   components: { Home }
// })
