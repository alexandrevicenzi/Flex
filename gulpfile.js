var gulp = require('gulp'),
    less = require('gulp-less'),
    rename = require('gulp-rename'),
    minify = require('gulp-cssnano');

gulp.task('less', function () {
    return gulp.src('./static/stylesheet/style.less')
        .pipe(less())
        .pipe(minify())
        .pipe(rename({
            extname: '.min.css'
        }))
        .pipe(gulp.dest('./static/stylesheet'));
});

gulp.task('cp', function () {
    return gulp.src('./node_modules/font-awesome/**/*.{min.css,otf,eot,svg,ttf,woff,woff2}')
        .pipe(gulp.dest('./static/font-awesome'));
});

gulp.task('default', ['less', 'cp']);
