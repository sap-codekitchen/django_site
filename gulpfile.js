var gulp        = require('gulp'),
    gutil       = require('gulp-util'),
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

gulp.task('watch', function(){
	gulp.watch(lessFiles, ['less']);
});

// Default Task
gulp.task('default', ['less', 'watch']);
gulp.task('build', ['less']);



