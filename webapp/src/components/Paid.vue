<template>
  <div class="container">
    <h1>Proceed to paiement</h1>
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
      return auth.user.authenticated;
    }
  }
};
</script>

<style scoped>

</style>
