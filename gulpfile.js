var gulp        = require('gulp'),
    concat      = require('gulp-concat'),
    gutil       = require('gulp-util'),
    jshint      = require('gulp-jshint'),
    browserify  =  require('browserify'),
    source      =  require('vinyl-source-stream'),
    less        = require('gulp-less');

// Include Our Plugins
// var jshint = require('gulp-jshint');


var lessFiles = [ './front/less/**/*.less' ];
var lessEntryFiles = [ './front/less/**/*-entry.less' ];

// LESS CSS preprocessor
gulp.task('less', function(){
	return gulp.src(lessEntryFiles)
		.pipe(less())
			.on('error', gutil.log)
		.pipe(gulp.dest('./static/css/'))
});


var vendorEntryFiles = [
				'./node_modules/jquery/dist/jquery.min.js',
				'./node_modules/bootstrap/dist/js/bootstrap.min.js',
				]

// Bootstrap and any other js libraries
gulp.task('vendor', function(){
	return gulp.src(vendorEntryFiles)
		.pipe(concat('vendor.js'))
		.pipe(gulp.dest('./static/js/'));
});

gulp.task('glyphicons', function(){
	return gulp.src('./node_modules/bootstrap/fonts/*')
		.pipe(gulp.dest('./static/fonts/'));
});


gulp.task('watch', function(){
	gulp.watch(lessFiles, ['less']);
});


// Default Task
gulp.task('build', ['less', 'vendor', 'glyphicons']);
gulp.task('default', ['build', 'watch']);



