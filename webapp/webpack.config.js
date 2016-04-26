var path = require('path');
var root = path.resolve(__dirname);
var webpack = require('webpack');

module.exports = {
  entry: './index',
  output: {
    path: path.resolve(__dirname, 'dist/'),
    filename: 'bundle.js'
  },
  devtool: 'source-map',
  module: {
    loaders: [
      {
        test: /\.js$/,
        loader: 'babel',
	exclude: /node_modules/,
	include: root
      },
    ]
  },
  plugins: [
    new webpack.optimize.UglifyJsPlugin({
      comments: false
    })
  ]
};
