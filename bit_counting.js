/*var countBits = function(n) {
  return parseInt(n.toString(2).split("").reduce((acc, curr) => parseInt(acc) + parseInt(curr)));
  
};*/

countBits = n => n.toString(2).split('0').join("").length;

console.log(countBits(1234));

