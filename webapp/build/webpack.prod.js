var configuration = require('./webpack.base');
var webpack = require('webpack');

configuration.plugins = configuration.plugins.concat([
  new webpack.optimize.UglifyJsPlugin({
    comments: false
  })
]);

module.exports = configuration;
