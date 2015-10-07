var gulp = require('gulp'),
    less = require('gulp-less'),
    rename = require('gulp-rename'),
    minify = require('gulp-minify-css');

gulp.task('less', function () {
    return gulp.src('./static/css/style.less')
        .pipe(less())
        .pipe(minify())
        .pipe(rename({
            extname: '.min.css'
        }))
        .pipe(gulp.dest('./static/css'));
});

gulp.task('default', ['less']);
