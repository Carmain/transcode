import Vue from "vue";
import router from "../main";
import config from "../config.js";

export default {
  user: {
    authenticated: false,
    username: "",
    email: ""
  },
  state: {
    checked: false
  },

  login(credentials, redirect) {
    let promise = Vue.http.post(config.LOGIN_URL, credentials).then((res) => {
      localStorage.setItem("jwt", res.data.token);
      this.user.authenticated = true;
      this.setVueHeader();
      return this.loadUserInformations();
    });

    promise.then((user) => {
      this.user.username = user.username;
      this.user.email = user.email;
      let fileUploaded = sessionStorage.getItem("fileUUID");

      // if the user upload a file but doesn't connect
      if(fileUploaded) {
        router.go('payment');
        return;
      }

      if (redirect) {
        router.go(redirect);
      }
    });

    return promise;
  },

  loadUserInformations() {
    if (!this.user.authenticated) {
      return Promise.resolve(false);
    }

    return new Promise ((resolve, reject) => {
      Vue.http.get(config.PROFILE_URL).then((res) => {
        resolve(res.data);
      });
    });
  },

  refreshTokenJob() {
    let promise = this.refreshToken();

    promise.then(() => {
      setTimeout(() => {
        this.refreshTokenJob();
      }, (config.TOKEN_EXPIRATION - 60) * 1000);
    });

    return promise;
  },

  refreshToken() {
    return new Promise ((resolve, reject) => {
      Vue.http.post(config.REFRESH_URL, {token: this.getToken()}).then((res) => {
        if (res.data.token) {
          localStorage.setItem("jwt", res.data.token);
          resolve();
        }
      }).catch(reject);
    });
  },

  logout() {
    localStorage.removeItem("jwt");
    this.user.authenticated = false;
    this.user.username = "";
  },

  checkAuth() {
    let jwt = localStorage.getItem("jwt");

    if (!jwt) {
      this.user.authenticated = false;
      this.state.checked = true;
      return;
    }
    this.user.authenticated = true;
    this.setVueHeader();
    this.refreshTokenJob().then(() => {
      return this.loadUserInformations();
    }).then((user) => {
      this.state.checked = true;
      this.user.username = user.username;
      this.user.email = user.email;
    });
  },

  getAuthHeader() {
    return "JWT " + this.getToken();
  },

  getToken () {
    return localStorage.getItem("jwt");
  },

  setVueHeader () {
    if (!this.user.authenticated) {
      return;
    }

    Vue.http.headers.common["Authorization"] = this.getAuthHeader();
  }
};
