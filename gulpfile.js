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

gulp.task('default', ['less']);
