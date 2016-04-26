var path = require('path');
var root = path.resolve(__dirname, '../');
var webpack = require('webpack');

module.exports = {
  entry: './index',
  output: {
    path: path.resolve(__dirname, '../dist/'),
    filename: 'bundle.js'
  },
  devtool: 'source-map',
  module: {
    preLoaders: [
      {
        test: /\.js$/,
        loader: 'eslint',
        exclude: /node_modules/,
      }
    ],
    loaders: [
      {
        test: /\.js$/,
        loader: 'babel',
        exclude: /node_modules/,
        include: root
      },
      {
        // url-loader
        test: /\.(png|jpg|gif|svg|woff2?|eot|ttf)$/,
        loader: 'url',
        query: {
          limit: 10000,
          name: '[name]-[hash:7].[ext]'
        }
      }
    ]
  },
  plugins: [],
  eslint: {
    configfile: path.resolve(root, './.eslintrc'),
    formatter: require('eslint-friendly-formatter')
  }
};
