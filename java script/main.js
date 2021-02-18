const companies = [
				{name : "one", category : "finance", start : "1"},
				{name : "two", category : "travels", start : "2"},
				{name : "three", category : "finance", start : "3"},
				{name : "Four", category : "Tech", start : "4"},
]

const args = [48, 49, 39, 39, 49, 39,10 ,20 ,30, 100,68]
// console.log(companies.length);

// for(i=0; i<companies.length; i++){
// 	console.log(companies[i])
// }


// // push values into list and get index 
// let list2 =[]
// args.forEach(function(argument, index) {
// 	list2.push(argument)
// 	console.log(argument, index)
// })
// console.log("list2", list2)


//  for loop for args and push to list
// let list = []
// for(i=0; i<args.length; i++){
// 	if (args[i] > 40){
// 		list.push(args[i])
// 		console.log(args[i])
// 	}
// }
// console.log("list is ", list)


//  using filter function
// const list3 = args.filter(function(age, index){
// 	if (age>40){
// 		console.log("index",index)
// 		return true;
// 	}
// })
// console.log(list3)


// //  using another way to filter
// const list4 = args.filter(arg => arg>=40);
// console.log(list4)

// array filter
// const array1 = companies.filter((company, index) => {
// 	if(company.category === "finance"  && index === 0){
// 		return true;
// 	}
// });
// console.log(array1)


// //  array filter anoter method
// const array2 = args.filter((arg, index) => (arg>= 60 && arg<=100));
// console.log(array2)



//  map function
//  getting company values
const test = companies.map(function(company){
	return `${company.name}[${company.category} - ${company.start}]`
})
console.log(test)




