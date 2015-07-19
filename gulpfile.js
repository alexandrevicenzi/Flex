var gulp = require('gulp'),
    less = require('gulp-less'),
    rename = require('gulp-rename'),
    minify = require('gulp-minify-css');

gulp.task('minify', function () {
  return gulp.src('./static/css/style.css')
    .pipe(minify())
    .pipe(rename({
        extname: '.min.css'
    }))
    .pipe(gulp.dest('./static/css'));
});

gulp.task('less', function () {
    return gulp.src('./static/css/style.less')
        .pipe(less())
        .pipe(gulp.dest('./static/css'));
});

gulp.task('default', ['less', 'minify']);
