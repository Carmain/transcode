<template>
  <div class="hello">
    <div class="intro row text-center">
      <h1 class="title">Transcode</h1>
      <div id="carousel" class="carousel slide" data-ride="carousel">
        <div class="row">
          <div class="col-md-4 col-md-offset-4 col-sm-10 col-sm-offset-1">
            <div class="carousel-inner pitch">
              <div class="item active">
                <div class="carousel-page">
                    <p>Transcode always be faster than me !</p>
                    <small><cite>-- Flash</cite></small>
                </div>
              </div>

              <div class="item">
                <div class="carousel-page">
                  <p>Please stop using my name in your quotes !</p>
                  <small><cite>-- Barack Obama</cite></small>
                </div>
              </div>

              <div class="item">
                <div class="carousel-page">
                    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
                    <small><cite>-- Your favorite web designer</cite></small>
                  <p></p>
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
      <div class="col-md-3 col-sm-6 square">
        <span class="glyphicon glyphicon-time icon" aria-hidden="true"></span>
        <div class="caption">
            <h2>Lightning Fast!</h2>
        </div>
        <p>Your files are converted as fast as possible.</p>
      </div>
      <div class="col-md-3 col-sm-6 square">
        <span class="glyphicon glyphicon-folder-open icon" aria-hidden="true"></span>
        <div class="caption">
            <h2>Never lose anymore your files!</h2>
        </div>
        <p>We give you 10Gb to store your files for ever.</p>
      </div>
      <div class="col-md-3 col-sm-6 square">
        <span class="glyphicon glyphicon-envelope icon" aria-hidden="true"></span>
        <div class="caption">
            <h2>Don't lose your time!</h2>
        </div>
        <p>Not the time to wait? You will be notified once the conversion is ready.</p>
      </div>
      <div class="col-md-3 col-sm-6 square">
        <span class="glyphicon glyphicon-user icon" aria-hidden="true"></span>
        <div class="caption">
            <h2>Trust is the key!</h2>
        </div>
        <p>{{ user_registered }} people trust us. And you ?</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      converted_files: 168276,
      user_registered: 16616
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
</style>
