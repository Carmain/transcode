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
    <hr />
    <h2>Your bill</h2>
    <p>
      you'll be debited from <b>{{ roundedPrice(amount) }} €</b> after this transaction.
    </p>
    <div class="paypal-button" id="paypal-container"></div>
    <form v-show="payment_succeed">
      <div class="form-group">
        <label class="control-label" for="convert-type">I want my file converted into</label>
        <select class="form-control" id="convert-type" v-model="selected">
          <option v-for="extension in formatArray" value="{{$index}}">{{ extension[0] }}</option>
        </select>
      </div>

      <button class="btn btn-primary btn-block" type="button" @click="convertFiles()">CONVERT MY FILES NOW</button>
    </form>
    <template v-for="sentence in messages_content">
      <message tag="danger" title="Waning" v-bind:message="sentence"></message>
    </template>
  </div>
</template>

<script>
import braintree from 'braintree-web';
import Message from './pieces/Message';
import config from "../config.js";
import auth from '../auth';

export default {
  components: {
    Message
  },
  data () {
    return {
      payment_succeed: false,
      error_handler: false,
      amount : '',
      messages_content: [],
      formatArray: [],
      selected: 0,
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
        }
      ]
    };
  },
  ready () {
    let that = this;
    let price = sessionStorage.getItem("price");
    this.formatArray = JSON.parse(sessionStorage.getItem("encoding"));
    console.log(this.formatArray);

    this.amount = price;
    this.$http.get(config.PAYPAL_TOKEN).then((res) => {
      let paypalToken = res.data.token;
      braintree.setup(paypalToken, "custom", {
        paypal: {
          container: "paypal-container",
          singleUse: true,
          amount: price,
          currency: 'USD',
          locale: 'en_us'
        },
        onPaymentMethodReceived: (obj) => {
          that.$http.post(config.PAYPAL_CHECKOUT,
            {
              "payment_method_nonce": obj.nonce,
              "fileUUID": sessionStorage.getItem("fileUUID")
            }).then((res) => {
            that.error_handler = false;

            if(res.data.success) {
              that.payment_succeed = true;
            } else {
              let error_message = res.data.message;
              if (error_message) {
                that.messages_content.push(res.data.message);
              } else {
                that.messages_content.push("Something went wrong with paypal");
              }
            }
          });
        }
      });
    });
  },
  methods: {
    roundedPrice: function(price) {
      console.log(price);
      return parseFloat(price).toFixed(2);
    },

    convertFiles: function() {
      let uuid = sessionStorage.getItem("fileUUID");

      let jsonObject = {
        file: uuid,
        format: this.formatArray[this.selected][0],
        codec: this.formatArray[this.selected][1]
      };

      this.$http.post(config.CONVERT_URL, jsonObject).then((res) => {
        if(res.data.success) {
          this.$route.router.go({ name: 'success', params: { fileUUID: uuid }});
        } else {
          console.log("error");
          let error_message = res.data.message;
          if (error_message) {
            that.messages_content.push(res.data.message);
          } else {
            that.messages_content.push("Something went wrong with the conversion");
          }
        }

      });
    }
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
  .error-handler {
    margin-top: 50px;
  }

  .paypal-button {
    margin-bottom: 30px;
  }
</style>
