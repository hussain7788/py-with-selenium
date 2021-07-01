"use strict";
// we have these data types in typesctipt
exports.__esModule = true;
var result = true;
var Name = "valli";
var age = 23;
var nothing = null;
var myName = undefined;
var Sentence = "my name is " + Name + ".. i am exp person in typescript";
console.log(Sentence);
// declare array in ts
var list1 = [1, 2, 3, 4];
var list2 = [2, 3, 4];
console.log(list2);
var person = ["hussain", 23];
//enum 
var Color;
(function (Color) {
    Color[Color["red"] = 0] = "red";
    Color[Color["blue"] = 1] = "blue";
    Color[Color["green"] = 2] = "green";
})(Color || (Color = {}));
var c = Color.green;
console.log(c);
var a;
a = 10;
a = 20;
console.log(a);
