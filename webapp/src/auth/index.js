import Vue from "vue";
import router from "../main";

const API_URL = "/api";
const LOGIN_URL = API_URL + "/auth/";
const PROFILE_URL = API_URL + "/me/";
const REFRESH_URL = API_URL + "/refresh-jwt/";
const TOKEN_EXPIRATION  = 300;

export default {
  user: {
    authenticated: false,
    username: ""
  },
  state: {
    checked: false
  },

  login(credentials, redirect) {
    Vue.http.post(LOGIN_URL, credentials).then((res) => {
      localStorage.setItem("jwt", res.data.token);

      return this.loadUserInformations();
    }).then((user) => {
      this.user.username = user.username;
      this.user.authenticated = true;

      if (redirect) {
        router.go(redirect);
      }
    }).catch(e => console.log(e));
  },

  loadUserInformations() {
    if (!this.user.authenticated) {
      return Promise.resolve(false);
    }

    return new Promise ((resolve, reject) => {
      Vue.http.get(PROFILE_URL).then((res) => {
        resolve(res.data);
      });
    });
  },

  refreshTokenJob() {
    let promise = this.refreshToken();

    promise.then(() => {
      setTimeout(() => {
        this.refreshTokenJob();
      }, (TOKEN_EXPIRATION - 60) * 1000);
    });

    return promise;
  },

  refreshToken() {
    return new Promise ((resolve, reject) => {
      Vue.http.post(REFRESH_URL, {token: this.getToken()}).then((res) => {
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

    this.refreshTokenJob().then(() => {
      return this.loadUserInformations();
    }).then((res) => {
      this.state.checked = true;
    });
  },

  getAuthHeader() {
    return "JWT " + this.getToken();
  },

  getToken () {
    return localStorage.getItem("jwt");
  }
}
