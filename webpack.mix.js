let mix = require('laravel-mix');

/*
 |--------------------------------------------------------------------------
 | Mix Asset Management
 |--------------------------------------------------------------------------
 |
 | Mix provides a clean, fluent API for defining some Webpack build steps
 | for your Laravel application. By default, we are compiling the Sass
 | file for your application, as well as bundling up your JS files.
 |
 */
mix.webpackConfig({ resolve: { modules: [__dirname, 'node_modules', 'resources/js'] } })

mix.js('resources/js/app.js', 'app/static/js/app.js')
  .sass('resources/scss/main.scss', 'app/static/css/app.css');

mix.copyDirectory('resources/js/dealer/', 'app/static/js/dealer/')