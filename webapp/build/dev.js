var webpack = require('webpack');
var config = require('./webpack.dev.js');
var webpackDevServer = require('webpack-dev-server');
var port = 8080;

var server = new webpackDevServer(webpack(config), {
  contentBase: './',
  quiet: false,
  noInfo: false,
  publicPath: config.output.publicPath,
  stats: {colors: true}
});

server.listen(port, function(err) {
  if(err) {
    console.log(err);
  } else {
    console.log("Listen on the port " + port);
  }
});
