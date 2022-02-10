let arr = [10, 20, 30, 40, 50, 60, 70]
const data = arr
.map(value => value*2)
.filter(val => val %2 == 0)
.sort((a,b) => b-a)
.reduce((a,b) => a+b, 0)

console.log(data)