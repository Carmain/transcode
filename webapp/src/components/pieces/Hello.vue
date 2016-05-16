<template>
  <div class="hello">
    <div class="intro row text-center">
      <h1 class="title">Transcode</h1>
      <div id="carousel" class="carousel slide" data-ride="carousel">
        <div class="row">
          <div class="col-md-4 col-md-offset-4 col-sm-10 col-sm-offset-1">
            <div class="carousel-inner pitch">
              <div v-for="quote in quotes" v-bind:class="quote.css_class">
                <div class="carousel-page">
                    <p>{{ quote.message}}</p>
                    <small><cite>-- {{quote.author}}</cite></small>
                </div>
              </div>
            </div>
          </div>
        </div>
      <div class="row">
        <ol class="carousel-indicators">
          <li data-target="#carousel" data-slide-to="0" class="active"></li>
          <li data-target="#carousel" data-slide-to="1"></li>
          <li data-target="#carousel" data-slide-to="2"></li>
        </ol>
      </div>
    </div>
    </div>
  </div>

  <div class="square-container text-center">
    <div class="row">

      <div v-for="square in squares" class="col-md-3 col-sm-6 square">
        <span v-bind:class="square.glyphicon" aria-hidden="true"></span>
        <div class="caption">
            <h2>{{ square.title }}</h2>
        </div>
        <p> {{ square.text }}</p>
      </div>
    </div>
  </div>

  <div class="row">
    <div class="col-md-4 col-md-offset-4 col-sm-10 col-sm-offset-1">
      <a v-link="'convert'" class="btn btn-info btn-raised btn-block" role="button">CONVERT MY FILES NOW !</a>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      quotes: [
        {
          message: 'Transcode always be faster than me !',
          author: 'Flash',
          css_class: 'item active'
        },
        {
          message: 'Please stop using my name in your quotes !',
          author: 'Barack Obama',
          css_class: 'item'
        },
        {
          message: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
          author: 'Your favorite web designer',
          css_class: 'item'
        }
      ],
      squares: [
        {
          title: 'Lightning Fast!',
          text: 'Your files are converted as fast as possible.',
          glyphicon: 'glyphicon glyphicon-time icon'
        },
        {
          title: 'Never lose anymore your files!',
          text: 'We give you 10Gb to store your files for ever.',
          glyphicon: 'glyphicon glyphicon-folder-open icon'
        },
        {
          title: 'Don\'t lose your time!',
          text: 'Not the time to wait? You will be notified once the conversion is ready.',
          glyphicon: 'glyphicon glyphicon-envelope icon'
        },
        {
          title: 'Clever enouth!',
          text: 'Don\'t be embraced by unreadable files',
          glyphicon: 'glyphicon glyphicon-sunglasses icon'
        }
      ]
    }
  }
}
</script>

<style scoped>
  .intro {
    background-color: #333;
  }

  .title {
    font-size: 120px;
    color: #EEEEEE;
  }

  .pitch {
    font-size: 20px;
    color: #EEEEEE;
  }

  .carousel-page {
  width:100%;
  height:150px;
  }

  .square-container {
    padding-top: 80px;
    margin: 20px;
  }

  .square {
    margin-top: 20px;
  }

  .icon {
    font-size: 100px;
  }

  .btn {
    margin: 40px;
    font-size: 30px;
  }
</style>
