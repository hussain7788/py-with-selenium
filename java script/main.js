const companies = [
				{name : "one", category : "finance", start : 1955, end: 1960},
				{name : "two", category : "travels", start : 1965, end: 1970},
				{name : "three", category : "finance", start : 1975, end: 1980},
				{name : "Four", category : "Tech", start : 1985, end: 1990},
]

const args = [10,20,30,40,50,60,70,80,90,100]
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


/////////////////////////////////////////////////////////////////////////////////////////////////////////
// //  map function
// //  getting company values
// const test = companies.map(function(company){
// 	return `${company.name}[${company.category} - ${company.start}]`
// })
// console.log(test)


// // map fnunction 
// // square root of args
// const res = args.map(age => Math.sqrt(age)).map(age => age * 2);
// console.log(res)

//////////////////////////////////////////////////////////////////////////////////////////////////////////
// // sort function
// const sortMethod = companies.sort(function(c1, c2){
// 		console.log("c1", c1,   "c2", c2)
// })
// console.log(sortMethod)


// //sort another method
// const sortComapnies = companies.sort((a, b) => (a.start > b.start ? 1: -1));
// console.log(sortComapnies)


// //sort ages in ascending and descending orders
// const argsSort = args.sort((a, b) => b -a);
// console.log(argsSort)

/////////////////////////////////////////////////////////////////////////////////////////////////////////////
//  reduce function

// var ageSum = 0;
// for ( i=0; i<args.length; i++){
// 	ageSum += args[i];
// }


// // reduce method to calculate total of args
// const ages = args.reduce(function(total, age){
// 		console.log(total, age)
// 		return total + age;
// }, 0)
// console.log("total",ages)


// //reduce function using map to calculate total of args
// const res = args.reduce((total, age) => total + age);
// console.log(res)

// // reduce function to get total years for all companies
// const totalYears = companies.reduce(function(total, company){
// 	return total + (company.end - company.start)
// }, 0)
// console.log(totalYears)


// // reduce function using arrow function
// const total = companies.reduce((total, company) => total + (company.end - company.start), 0);
// console.log(total)


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// COMBINE ALL METHODS 

const combined = args
	.map(age => age *2)
	.filter(age => age >=100)
	.sort((a,b) => b-a)
	.reduce((total, age) => total + age, 0);

console.log(combined)

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////






