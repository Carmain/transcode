<template>
  <div class="container">
    <h1>Proceed to payment</h1>
    <h2>Informations</h2>
    <p>
      Before to convert the file, you must paid !
      <b>The price is fixed to one USD to process one hour of video or sound.</b><br />
    </p>
    <p>
      The following table gave you an ID of the prices :
    </p>

    <table class="table table-striped">
      <thead>
        <tr>
          <th>Duration</th>
          <th>Price</th>
        </tr>
      </thead>
      <tbody>
        <template v-for="calculation in ranges">
          <tr>
            <td>{{ calculation.duration }}</td>
            <td>{{ calculation.price }} USD</td>
          </tr>
        </template>
      </tbody>
    </table>
    <h2>Your bill</h2>
    <div id="paypal-container"></div>
  </div>
</template>

<script>
import braintree from 'braintree-web';
import config from "../config.js";
import auth from '../auth';

export default {
  data () {
    return {
      ranges: [
        {
          duration: '1:00:00',
          price: '1'
        },
        {
          duration: '30:00',
          price: '0.50'
        },
        {
          duration: '00:15:00',
          price: '0.25'
        },
        {
          duration: '00:10:00',
          price: '0.17'
        },
        {
          duration: '00:05:00',
          price: '0.08'
        },
        {
          duration: '00:01:00',
          price: '0.01'
        }
      ]
    };
  },
  ready () {
    let that = this;
    this.$http.get(config.PAYPAL_TOKEN).then((res) => {
      let paypalToken = res.data.token;


      braintree.setup(paypalToken, "custom", {
        paypal: {
          container: "paypal-container",
          singleUse: true,
          amount: 1.00,
          currency: 'USD',
          locale: 'en_us'
        },
        onPaymentMethodReceived: (obj) => {
          that.$http.post(config.PAYPAL_CHECKOUT,
            {
              "payment_method_nonce": obj.nonce
            }).then((res) => {
            console.log(res);
          });
        }
      });
    });
  },
  route: {
    canActivate() {
      if (sessionStorage.getItem("fileUUID") && auth.user.authenticated) {
        return true;
      }

      return false;
    }
  }
};
</script>

<style scoped>

</style>
