// comp = [1,2,3,4,5,6]
// for (var i = 0; i<comp.length; i++) {
// 	console.log(comp[i])
// }

// for(let i of comp){
// 	console.log("data::", i)
// }

// const js_obj = {
//     name: "hussain",
//     age: 23,
//     add: "kadapa"
// }

// var keys = Object.keys(js_obj)
// console.log(keys)

// var values = Object.values(js_obj)
// console.log(values)

// var ent = Object.entries(js_obj)
// console.log(ent)

// var assign = Object.assign(js_obj, {designation: 'dev'})
// console.log(assign)


const companies = [
	{name : "one", category : "finance", start : 1955, end: 1960},
	{name : "two", category : "travels", start : 1965, end: 1970},
	{name : "three", category : "finance", start : 1975, end: 1980},
	{name : "Four", category : "Tech", start : 1985, end: 1990},
]

const args = [10,20,30,40,50,60,70,80,90,100, 101, 102]

const l1 = []
// const data = args.forEach((res,i) => l1[i] = res*2)
// const data = args.forEach((res,i) => args[i] = res*2)

// const fil =  args.filter(res => res%2==0)

const data = companies.filter(filter_data)
function filter_data(value, index){
	if (value.name == "one" || value.name == "Four"){
		return value.category
	}
}

const red = args.reduce(redu)
function redu(total, num){
	if(total == 10){
		d= total += num
		console.log(d)
	}
	else if(total == 20){
		d= total += num
		console.log(d)
	}
}
// console.log(red)


const args2 = args.every(res => res%2 ==0)
// console.log("args",args2)


const ent = args.entries()

for (let x of ent){
	console.log(x+ "\n")
}

console.log(args.findIndex(33939))