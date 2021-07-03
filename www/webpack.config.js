const path = require('path')
const HtmlWebpackPlugin = require('html-webpack-plugin')
const CopyWebpackPlugin = require('copy-webpack-plugin')

module.exports = {
    target: 'web',
    name: 'app',
    entry: {
        app: './src/index.tsx'
    },
    output: {
        filename: 'assets/[name].[fullhash].js',
        publicPath: '/'
    },
    performance: {
        maxEntrypointSize: 2 * 1024 * 1024,
        maxAssetSize: 2 * 1024 * 1024
    },
    resolve: {
        extensions: ['.ts', '.tsx', '.js', '.jsx'],
        alias: {
            controls: path.resolve(__dirname, 'controls'),
            app: path.resolve(__dirname, 'src/app'),
            assets: path.resolve(__dirname, 'src/assets')
        }
    },
    module: {
        rules: [
            {
                test: /\.(png|jpg|svg)$/,
                use: ['file-loader']
            },
            {
                test: /\.(ttf|woff|woff2|eot)$/,
                use: ['file-loader']
            },
            {
                test: /\.(ts|tsx|js|jsx)$/,
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: [
                            '@babel/preset-env',
                            '@babel/preset-react',
                            '@babel/preset-typescript'
                        ]
                    }
                }
            }
        ]
    },
    plugins: [
        new HtmlWebpackPlugin({
            template: './src/index.html'
        }),
        new CopyWebpackPlugin({
            patterns: [
                {
                    from: path.resolve(__dirname, './src/assets'),
                    to: 'assets/'
                }
            ]
        })
    ]
}
