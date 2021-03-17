var url = 'http://localhost:3000/dose';
var postdata = { "dose":0.0, "dt": 5, "index": 0, "time": 1080, "events": {"bolus": [{"amt": 10.0, "start": 0}], "basal": [{"amt": 1.3, "start": 0, "length": 600}], "carb": [{"amt": 10.0, "start":0, "length": 90}]} };
//var res3 = request('POST', url, {json: postdata});
var request = require("sync-request");
//var ID=[];//units of microU/min
var res3 = request('POST', url, {json: postdata});

var response = JSON.parse(res3.getBody());
console.log(response.bg);
