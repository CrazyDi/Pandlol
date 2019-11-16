const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const CleanWebpackPlugin = require('clean-webpack-plugin');

module.exports = {
    mode: 'production',
    entry: {
        main: './src/index.js'
    },
    output: {
        path: path.resolve(__dirname, 'public'),
        filename: 'js/[hash].js'
    },
    module: {
        rules: [
            {
                test: /\.(js)$/,
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: [
                            '@babel/preset-env',
                            '@babel/preset-react'
                        ],
                        plugins: [
                            '@babel/plugin-transform-arrow-functions',
                            '@babel/plugin-proposal-class-properties'
                        ]
                    }
                }
            },
            {
                test: /\.scss$/,
                use: [MiniCssExtractPlugin.loader, 'css-loader', 'sass-loader']
            },
            {
                test: /\.(jpg|gif)$/i,
                use: [
                    {
                        loader: 'url-loader',
                        options: {
                            limit: 8192,
                            name: '/[path][name].[ext]',
                            outputPath: '../',
                            publicPath: (url) => {
                                return `${url}`;
                            }
                        }
                    }
                ]
            },

            {
                test: /\.(png|svg)$/,
                use: [{
                    loader: 'file-loader',
                    options: {
                        name: '/[path][name].[ext]',
                        outputPath: '../',
                        publicPath: (url) => {
                            return `${url}`;
                        }
                    }
                }]
            },

            {
                test: /\.(woff|woff2|eot|ttf|otf)$/,
                use: [{
                    loader: 'file-loader',
                    options: {
                        name: '/[path][name].[ext]',
                        outputPath: '../',
                        publicPath: (url) => {
                            return `${url}`;
                        }
                    }
                }]
            }
        ]
    },
    plugins: [
        new HtmlWebpackPlugin({
            template: './src/index.html'
        }),
        new MiniCssExtractPlugin({
            filename: 'css/[hash].css'
        }),
        new CleanWebpackPlugin()
    ],
    resolve: {
        extensions: ['*', '.js'],
        alias: {
            app: path.resolve(__dirname, 'src/app/')
        }
    }
};
