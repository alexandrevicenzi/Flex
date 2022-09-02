var gulp = require('gulp'),
    less = require('gulp-less'),
    rename = require('gulp-rename'),
    cssnano = require('gulp-cssnano'),
    uglify = require('gulp-uglify');

gulp.task('less', function () {
    return gulp.src([
            './static/stylesheet/dark-theme.less',
            './static/stylesheet/style.less',
        ])
        .pipe(less())
        .pipe(cssnano())
        .pipe(rename({
            extname: '.min.css'
        }))
        .pipe(gulp.dest('./static/stylesheet'));
});

gulp.task('uglify', function () {
    return gulp.src('./static/dark-theme/dark-theme.js')
        .pipe(uglify())
        .pipe(rename({
            extname: '.min.js'
        }))
        .pipe(gulp.dest('./static/dark-theme'));
});

gulp.task('cp', function () {
    return gulp.src('./node_modules/font-awesome/**/*.{min.css,otf,eot,svg,ttf,woff,woff2}')
        .pipe(gulp.dest('./static/font-awesome'));
});

gulp.task('pygments', function () {
    return gulp.src(['./static/pygments/*.css', '!./static/pygments/*min.css'])
        .pipe(cssnano())
        .pipe(rename({
            extname: '.min.css'
        }))
        .pipe(gulp.dest('./static/pygments'));
});

gulp.task('watch-less', function () {
    return gulp.watch('static/stylesheet/*.less', gulp.task('less'));
});

gulp.task('watch-js', function () {
    return gulp.watch('static/dark-theme/!(*.min).js', gulp.task('uglify'));
})

gulp.task('default', gulp.series(['less', 'uglify', 'cp', 'pygments']));

gulp.task('watch', gulp.series('default', gulp.parallel('watch-less', 'watch-js')));
