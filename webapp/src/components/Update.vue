<template>
  <div class ="container">
    <h1>Update my profile</h1>
    <ul class="nav nav-tabs">
      <li class="active"><a data-toggle="tab" href="#personal-data">Your profile</a></li>
      <li><a data-toggle="tab" href="#password">Security</a></li>
    </ul>

    <div class="tab-content">
      <div id="personal-data" class="tab-pane fade in active">
        <h2>Update my profile</h2>
        <form role="form">
          <div class="row">
            <div class="col-md-10 col-sm-9 col-xs-8">
              <div class="form-group">
                <label class="control-label" for="email">Email</label>
                <input class="form-control" id="email" type="email" v-model="user.old_email">
              </div>
              <div class="form-group">
                <label class="control-label" for="new-email">New email</label>
                <input class="form-control" id="new-email" type="email" v-model="user.new_email">
              </div>
            </div>
            <div class="col-md-2 col-sm-3 col-xs-4">
              <gravatar size='130' v-bind:email='user.new_email'></gravatar>
            </div>
          </div>
          <div class="row">
            <div class="form-group col-md-6 col-sm-6">
              <label class="control-label" for="first-name">First name</label>
              <input class="form-control" id="first-name" type="text" v-model="user.firstname">
            </div>
            <div class="form-group col-md-6 col-sm-6">
              <label class="control-label" for="last-name">Last name</label>
              <input class="form-control" id="last-name" type="text" v-model="user.last_name">
            </div>
          </div>
          <div class="form-group">
            <label class="control-label" for="birthdate">Birthdate</label>
            <input class="form-control" id="birthdate" type="date" v-model="user.birthdate">
          </div>
          <button type="submit" class="btn btn-raised btn-primary pull-right">Submit my modifications</button>
        </form>
      </div>
      <div id="password" class="tab-pane fade">
        <h2>Security</h2>

        <fieldset>
          <legend>
            <h3>Change my password</h3>
          </legend>
          <form>
            <div class="form-group">
              <label class="control-label" for="password">Password</label>
              <input class="form-control" id="password" type="password" v-model="password.old">
            </div>
            <hr />
            <div class="form-group">
              <label class="control-label" for="new-password">New password</label>
              <input class="form-control" id="new-password" type="password" v-model="password.new_password">
            </div>
            <div class="form-group">
              <label class="control-label" for="new-password-confirm">Confirm password</label>
              <input class="form-control" id="new-password-confirm" type="password" v-model="password.confirmation">
            </div>
            <button type="submit" class="btn btn-raised btn-primary pull-right">Submit</button>
          </form>
        </fieldset>

        <fieldset>
          <legend>
            <h3>Remove my account</h3>
          </legend>
          <p>Your about to delete your account. Are you shure to want to de that ?</p>
        </fieldset>
      </div>
    </div>
  </div>
</template>

<script>
import auth from '../auth'
import Gravatar from './pieces/Gravatar'

export default {
  components: {
    Gravatar
  },
  data () {
    return {
      user: {
        old_email: '',
        new_email: '',
        firstname: '',
        last_name: '',
        birthdate: ''
      },

      password: {
        old: '',
        new_password: '',
        confirmation: ''
      }
    }
  },
  route: {
    canActivate() {
      return auth.user.authenticated;
    }
  }
}

</script>
