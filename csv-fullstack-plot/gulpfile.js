// include gulp
var gulp = require('gulp');

// include libs
var bowerMainFiles = require('main-bower-files');
var concatJs = require('gulp-concat');
var stripDebug = require('gulp-strip-debug');
var uglify = require('gulp-uglify');
var inject = require('gulp-inject');
var sass = require('gulp-sass');

// srcs
var src = {
    custom_dev: {
        js: [
        './ui/ui-app.js',
        '!./ui/vendor/bower_components/**/*.js',
        '!./ui/vendor/**/*.js',
        '!./ui/build/javascripts.js',
        './ui/states/**/*.js',
        './ui/common/**/*.js'
        ],
        css: [
            './ui/build/application.css',
            './ui/common/charts/**/*.css',
            './ui/common/map_component/*.css',
            './ui/common/panel_component/*.css',
            './ui/common/info_component/*.css',
        ]
    },
    custom_prod: {
        js: ['./ui/build/application.js'],
        css: ['./ui/build/application.css']
    },
    vendor: [
    '!./ui/vendor/bower_components/**/*.js',
    '!./ui/vendor/bower_components/**/*.css',
    './ui/vendor/**/*.js',
    './ui/vendor/**/*.css'
    ]
};

// compile sass task
gulp.task('compile-css', function () {
  return gulp.src('./ui/stylesheets/application.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest('./ui/build'));
});

// concatenate javascript task
gulp.task('concat-js', function() {
  return gulp.src(bowerMainFiles({ paths : { bowerDirectory: './ui/vendor/bower_components' }}))
    .pipe(concatJs('application.js'))
    .pipe(gulp.dest('./ui/build/'));
});

// minify javascript task
gulp.task('minify-js', ['concat-js'], function() {
  return gulp.src('./ui/build/application.js')
    .pipe(uglify())
    .pipe(gulp.dest('./ui/build'));
});

// inject javascript and css references into index (development build)
gulp.task('inject-references-dev',['compile-css'], function () {
    return gulp.src('./ui/common/main_page/index.ejs')
    .pipe(inject(
        gulp.src(bowerMainFiles({ paths : { bowerDirectory: './ui/vendor/bower_components' }})),
        { name: 'bower', relative: false }))
    .pipe(inject(
        gulp.src(src.custom_dev.js, { read: false }),
        { name: 'custom', relative: false }))
    .pipe(inject(
        gulp.src(src.custom_dev.css, { read: false }),
        { name: 'custom', relative: false }))
    .pipe(inject(
        gulp.src(src.vendor, { read: false }),
        { name: 'vendor', relative: false }))
    .pipe(gulp.dest('./ui/common/main_page'));
});

gulp.task('index', function () {
    return gulp.src('./www/index.html')
        .pipe(inject(gulp.src(mainBowerFiles(), {read: false}, {relative: true}), {name: 'bower'}))
        .pipe(gulp.dest('./www'));
});

// inject javascript and css references into index (development build)
gulp.task('inject-references-prod', ['minify-js'], function () {
    return gulp.src('./ui/common/main_page/index.ejs')
        .pipe(inject(
            gulp.src(bowerMainFiles({ paths : { bowerDirectory: './ui/vendor/bower_components' }})),
            { name: 'bower', relative: false }))
        .pipe(inject(
            gulp.src(src.custom_prod.js, { read: false }),
            { name: 'custom', relative: false }))
        .pipe(inject(
            gulp.src(src.custom_prod.css, { read: false }),
            { name: 'custom', relative: false }))
        .pipe(inject(
            gulp.src(src.vendor, { read: false }),
            { name: 'vendor', relative: false }))
        .pipe(gulp.dest('./ui/common/main_page'));
});

// development build
gulp.task('development', ['compile-css', 'inject-references-dev'], function() {
});

// production build (includes JS concatenation and minification, CS concatenation)
gulp.task('production', ['compile-css', 'inject-references-prod'], function() {
});
