<template>
  <h1 class="title">Welcome</h1>
  <table class="table table-striped">
    <thead>
      <tr>
        <th></th>
        <th>File name</th>
        <th>Converted into</th>
        <th>Date</th>
      </tr>
    </thead>
    <tbody>
      <template v-for="file in files">
        <tr>
          <td>
            <template v-if="isFileMusic(file)">
              <span class="glyphicon glyphicon-music" aria-hidden="true"></span>
            </template>
            <template v-else>
              <span class="glyphicon glyphicon-film" aria-hidden="true"></span>
            </template>
          </td>
          <td>{{ file.name }}</td>
          <td>{{ file.convert_to }}</td>
          <td>{{ file.date }}</td>
        </tr>
      </template>
    </tbody>
  </table>
</template>

<script>
  export default {
    data () {
      return {
        files: [
          {
            name: 'yolo.mp3',
            convert_to: 'wav',
            date: '17/05/2016',
            type: 'music'
          },
          {
            name: 'do_the_barrel_roll.mp4',
            convert_to: 'mp3',
            date: '4/05/2016',
            type: 'music'
          },
          {
            name: 'hello.m4v',
            convert_to: 'wmv',
            date: '17/03/2016',
            type: 'video'
          },
          {
            name: 'creep.wma',
            convert_to: 'mp3',
            date: '22/03/2016',
            type: 'music'
          },
          {
            name: 'lolilol.m4v',
            convert_to: 'wmv',
            date: '24/12/2015',
            type: 'video'
          }
        ]
      }
    },
    methods: {
      isFileMusic: function (file) {
        return file.type !== 'video'
      }
    }
  }
</script>
