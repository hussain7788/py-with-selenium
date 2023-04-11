var data = '{"name":"hussain","age":23}'

console.log(data[2])
var json_parse = JSON.parse(data)
console.log("json string data::", data)
console.log("converted json string data into javascript object:::", json_parse)
console.log("type of javascript object:::", typeof json_parse)


var json_string = JSON.stringify(json_parse)

console.log("converted javascript object into json string data:::", json_string)
console.log("type of json object:::", typeof json_string)
