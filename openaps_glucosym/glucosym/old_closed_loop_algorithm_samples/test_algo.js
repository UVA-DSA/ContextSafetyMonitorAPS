var url = 'http://localhost:3000/dose';
var request = require("sync-request");
postdata = { "dose": 0.0, "dt": 5, "index": 0, "time": 1080, "events": {"bolus": [{"amt":0.0 , "start": 60}], "basal": [{"amt": 8, "start": 0, "length": 600}], "carb": [{"amt": 0.0, "start": 600, "length": 90}]} };


//postdata = {"events": {"bolus": [{"amt": 0.0, "start": 60}], "basal": [{"amt": 0, "start": 0, "length": 600}], "carb": [{"amt": 0.0, "start": 600, "length": 90}]} };
//for(var i=0; i<10; i++){
//postdata.index += 5;
request('POST', url, {json: postdata});

var res3 = request('POST', url, {json: postdata});
var response = JSON.parse(res3.getBody());
console.log(response.bg);
//}
