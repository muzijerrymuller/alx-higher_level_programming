#!/usr/bin/node
// 
// this code writes a string to a file
//
const fs = require('fs');
const file = process.argc[2];
const write_ = process.argv[3];

fs.writefile(file, write_, 'utf-8', function (error)){
	if (error){
		console.log(error);
	}
});
