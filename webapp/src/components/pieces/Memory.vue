<template>
  <canvas id="pieChart" v-bind:width="width" v-bind:height="height"></canvas>
</template>

<script>
import Chart from 'chart.js';

export default {
  props: [
    "width",
    "height",
    "memory"
  ],
  ready () {
    this.displayChart();
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
