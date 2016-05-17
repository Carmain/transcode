<template>
  <div class="hello">
    <div class="intro text-center">
      <h1 class="title">Transcode</h1>
      <div id="carousel" class="carousel slide" data-ride="carousel">
        <div class="container">
          <div class="row">
            <ol class="carousel-indicators col-md-10 col-md-offset-1 col-xs-10 col-xs-offset-1">
              <li data-target="#carousel" data-slide-to="0" class="active"></li>
              <li data-target="#carousel" data-slide-to="1"></li>
              <li data-target="#carousel" data-slide-to="2"></li>
            </ol>
          </div>

          <div class="row">
            <div class="col-md-10 col-md-offset-1 col-xs-10 col-xs-offset-1">
              <div class="carousel-inner pitch">
                <div v-for="quote in quotes" v-bind:class="quote.css_class">
                  <p>{{ quote.message}}</p>
                  <small><cite> {{quote.author}}</cite></small>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="container-fluid">
      <div class="row square-container text-center">
        <div v-for="square in squares" class="col-md-3 col-sm-6 square">
          <!-- FIXME: The big icon set a margin on the right when we reduce the page -->
          <span v-bind:class="square.glyphicon" aria-hidden="true"></span>
          <div class="caption">
              <h2>{{ square.title }}</h2>
          </div>
          <p> {{ square.text }}</p>
        </div>
      </div>

      <div class="row">
        <div class="col-md-6 col-md-offset-3 col-xs-10 col-xs-offset-1">
          <a v-link="'convert'" class="btn btn-info btn-raised btn-block" role="button">CONVERT MY FILES NOW !</a>
        </div>
      </div>
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
          css_class: 'carousel-page item active'
        },
        {
          message: 'Please stop using my name in your quotes !',
          author: 'Barack Obama',
          css_class: 'carousel-page item'
        },
        {
          message: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
          author: 'Your favorite web designer',
          css_class: 'carousel-page item'
        }
      ],
      squares: [
        {
          title: 'Lightning Fast!',
          text: 'Your files are converted as fast as possible.',
          glyphicon: 'glyphicon glyphicon-time'
        },
        {
          title: 'Never lose anymore your files!',
          text: 'We give you 10Gb to store your files for ever.',
          glyphicon: 'glyphicon glyphicon-folder-open'
        },
        {
          title: 'Don\'t lose your time!',
          text: 'Not the time to wait? You will be notified once the conversion is ready.',
          glyphicon: 'glyphicon glyphicon-envelope'
        },
        {
          title: 'Clever enouth!',
          text: 'Don\'t be embraced by unreadable files',
          glyphicon: 'glyphicon glyphicon-sunglasses'
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
    margin-top: 0px;
    font-size: 120px;
    color: #EEEEEE;
  }

  .pitch {
    font-size: 20px;
    color: #EEEEEE;
  }

  .carousel-page {
  height: 180px;
  }

  .square-container {
    padding-top: 80px;
    margin: 20px;
  }

  .square {
    margin-top: 20px;
  }

  .glyphicon {
    font-size: 80px;
  }

  .btn {
    font-size: 30px;
  }
</style>
