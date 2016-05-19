import Vue from 'vue'
import VueRouter from 'vue-router'
import VueResource from 'vue-resource'

import App from './App'
import auth from './auth';
import Home from './components/Home'
import Connect from './components/Connect'
import Register from './components/Register'
import Convert from './components/Convert'
import NotFound from './components/NotFound'

Vue.use(VueRouter)
Vue.use(VueResource)
auth.checkAuth()

Vue.http.headers.common['Authorization'] = auth.getAuthHeader()

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
  },
  '/404': {
    name: '404',
    component: NotFound
  }
})

router.redirect({
  '*': '404'
})

router.start(App, '#app')
export default router;
