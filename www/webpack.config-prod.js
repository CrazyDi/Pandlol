const path = require('path')
const { merge } = require('webpack-merge')
const config = require('./webpack.config')

module.exports = merge(config, {
    mode: 'production',
    output: {
        clean: true,
        path: path.resolve(__dirname, 'public')
    },
    optimization: {
        minimize: true
    }
})
