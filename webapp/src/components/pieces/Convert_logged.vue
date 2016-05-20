<template>
  <div class="col-sm-6">
    <h2>Your stockage</h2>
    <canvas id="pieChart" width="400" height="350"></canvas>
  </div>
  <div class="col-sm-6">
    <h2>Your last converted files</h2>
    <template v-for="file in last_files">
      <div class="row">
        <div class="col-sm-3 col-xs-3 text-center">
          <template v-if="isFileMusic(file)">
            <span class="glyphicon glyphicon-music gl-x3" aria-hidden="true"></span>
          </template>
          <template v-else>
            <span class="glyphicon glyphicon-film gl-x3" aria-hidden="true"></span>
          </template>
        </div>
        <div class="col-sm-9 col-xs-9">
          <h3>{{ file.name }}</h3>
          <p>Converted to : <b>{{ file.convert_to }}</b></p>
        </div>
      </div>
      <hr />
    </template>
  </div>
</template>

<script>
import Chart from 'chart.js'

export default {
  data () {
    return {
      memory: [1654, 16819],
      last_files: [
        {
          name: 'yolo.mp3',
          convert_to: 'wav',
          type: 'music'
        },
        {
          name: 'do_the_barrel_roll.mp4',
          convert_to: 'mp3',
          type: 'music'
        },
        {
          name: 'hello.m4v',
          convert_to: 'wmv',
          type: 'video'
        },
        {
          name: 'creep.wma',
          convert_to: 'mp3',
          type: 'music'
        },
        {
          name: 'lolilol.m4v',
          convert_to: 'wmv',
          type: 'video'
        }
      ]
    }
  },
  ready () {
    this.displayChart()
  },
  methods: {
    isFileMusic: function (file) {
      return file.type !== 'video'
    },
    displayChart: function () {
      var ctx = document.getElementById('pieChart').getContext('2d')
      var myChart = new Chart(ctx, { // eslint-disable-line
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
      })
    }
  }
}
</script>

<style scoped>

</style>
