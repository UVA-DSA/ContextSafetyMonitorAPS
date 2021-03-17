var fs = require('fs');
var index = JSON.parse(fs.readFileSync('algo_input.json', 'utf8'));
var my_index = index.index;
console.log(my_index);
