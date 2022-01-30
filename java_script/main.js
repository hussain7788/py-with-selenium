const companies = [
				{name : "one", category : "finance", start : 1955, end: 1960},
				{name : "two", category : "travels", start : 1965, end: 1970},
				{name : "three", category : "finance", start : 1975, end: 1980},
				{name : "Four", category : "Tech", start : 1985, end: 1990},
]

const args = [10,20,30,40,50,60,70,80,90,100]

const data = [{"tab_config":[{"tab_name":"Unassigned","id":"unassignedTab","internal":"Unassigned","status":[{"status_name":"Initial"}]},{"tab_name":"Preparation","id":"preparationTab","internal":"AdminPreparation","status":[{"status_name":"Assigned"},{"status_name":"In Progress"},{"status_name":"Mgr Review"}]},{"tab_name":"Review","id":"reviewTab","internal":"AdminReview","status":[{"status_name":"Admin Review"}]},{"tab_name":"Finalization","id":"finalizationTab","internal":"Finalization","status":[{"status_name":"Info Pending"},{"status_name":"Client Review"},{"status_name":"Efile Auth"}]},{"tab_name":"Closure","id":"closureTab","internal":"Closure","status":[{"status_name":"Efiled"},{"status_name":"Closed"}]},{"tab_name":"Extension","id":"extensionTab","internal":"Extension"},{"tab_name":"Overview","id":"overviewTab","internal":"Overview"}],
			"years":[2020,2019,2018,2017],
			"buttons":{"Initial":[{"type":"dropdown","options":["Team Member","Sarah Walker","John Casey","Morgan Grimes","d1 lname"],"values":[-1,0,1,4,7],"id":"mgrDropDown"},{"type":"button","display":"Assign","id":"assign","active":true}],"Assigned":[{"type":"button","display":"Admin Review","id":"preparationTabadminReview","active":true},{"type":"button","display":"Client Review","id":"preparationTabclientReview","active":true}],"In Progress":[{"type":"button","display":"Admin Review","id":"preparationTabadminReview","active":true},{"type":"button","display":"Client Review","id":"preparationTabclientReview","active":true}],"Mgr Review":[{"type":"button","display":"Admin Review","id":"preparationTabadminReview","active":true},{"type":"button","display":"Client Review","id":"preparationTabclientReview","active":true}],"Admin Review":[{"type":"button","display":"Client Review","id":"reviewTabclientReview","active":true},{"type":"button","display":"Efile Auth","id":"reviewTabefileAuth","active":true}],"Info Pending":[{"type":"button","display":"Admin Review","id":"finalizationTabadminReview","active":true},{"type":"button","display":"Client Review","id":"finalizationTabclientReview","active":true},{"type":"button","display":"Efile Auth","button":"efileAuth","active":false},{"type":"button","display":"Efiled","button":"efiled","active":false},{"type":"button","display":"Send Reminder","id":"sendReminder","active":true}],"Client Review":[{"type":"button","display":"Admin Review","button":"adminReview","active":false},{"type":"button","display":"Client Review","button":"clientReview","active":false},{"type":"button","display":"Efile Auth","id":"finalizationTabefileAuth","active":true},{"type":"button","display":"Efiled","button":"efiled","active":false},{"type":"button","display":"Send Reminder","id":"finalizationTabsendReminder","active":true}],"Efile Auth":[{"type":"button","display":"Admin Review","button":"adminReview","active":false},{"type":"button","display":"Client Review","button":"clientReview","active":false},{"type":"button","display":"Efile Auth","button":"efileAuth","active":false},{"type":"button","display":"Efiled","id":"finalizationTabefiled","active":true},{"type":"button","display":"Send Reminder","id":"finalizationTabsendReminder","active":true}],"Efiled":[{"type":"button","display":"Close","id":"closureTabclose","active":true}],"Closed":[{"type":"button","display":"Close","button":"close","active":false}],"Unassigned":[{"type":"dropdown","options":["Team Member","Sarah Walker","John Casey","Morgan Grimes","d1 lname"],"values":[-1,0,1,4,7],"id":"mgrDropDown"},{"type":"button","display":"Assign","id":"assign","active":true}],"Preparation":[{"type":"button","display":"Admin Review","id":"adminReview","active":false},{"type":"button","display":"Client Review","id":"clientReview","active":false}],"Review":[{"type":"button","display":"Client Review","id":"clientReview","active":true},{"type":"button","display":"Efile Auth","id":"efileAuth","active":true}],"Finalization":[{"type":"button","display":"Admin Review","id":"adminReview","active":false},{"type":"button","display":"Client Review","id":"clientReview","active":false},{"type":"button","display":"Efile Auth","id":"efileAuth","active":false},{"type":"button","display":"Efiled","id":"efiled","active":false},{"type":"button","display":"Send Reminder","id":"sendReminder","active":false}],"Closure":[{"type":"button","display":"Close","id":"close","active":false}],"Extension":null,"Overview":null}}]

// console.log(data[0].tab_config.length)
// const res = data[0].tab_config.forEach(ele => {
//     console.log("data updated", ele)
// })

// for(let i of companies){
// 	console.log(i.name)
// }




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
// // sort function for asc and desc
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
// // COMBINE ALL METHODS 

// const combined = args
// 	.map(age => age *2)
// 	.filter(age => age >=100)
// 	.sort((a,b) => b-a)
// 	.reduce((total, age) => total + age, 0);

// console.log(combined)

// const comb = args
// .map(age => age *2)
// .filter(age => age>=100)
// .sort((a,b) => b-a)
// .reduce((total,age) => total+age, 0 ) ;
// console.log(comb)

// // reduce is used to calculate the total value of list values
// const r1 = args.reduce((p_value, c_value) => p_value+c_value, )
// console.log(r1)

// // sort method for asc and desc list
// const s1 = args.sort((a,b) => b-a)
// console.log(s1)


///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////






