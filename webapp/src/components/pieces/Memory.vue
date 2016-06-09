<template>
  <canvas id="pieChart" v-bind:width="width" v-bind:height="height"></canvas>
</template>

<script>
import config from '../../config';
import Chart from 'chart.js';

export default {
  props: [
    "width",
    "height"
  ],
  data () {
    return {
      memory: []
    };
  },
  ready () {
    this.$http.get(config.PROFILE_URL).then((res) => {
      this.memory = [res.data.used_space, res.data.free_space];

      this.displayChart();
    });
  },
  methods: {
    displayChart: function () {
      var ctx = document.getElementById('pieChart').getContext('2d');
      var myChart = new Chart(ctx, {
        type: 'pie',
        data: {
          labels: ['Used', 'Free'],
          datasets: [{
            backgroundColor: [
              '#36A2EB',
              '#FFCE56'
            ],
            label: 'Used memory',
            data: this.memory
          }]
        }
      });
    }
  }
};
</script>

<style scoped>

</style>
