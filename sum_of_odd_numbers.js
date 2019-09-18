function rowSumOddNumbers(n) {
	var oddsTriangle = [];
	var oddNums = [...Array(1000).keys()].filter((a) => a % 2 !== 0);
	
	for(let i = 0; i <= n; i++) {
		oddsTriangle.push(oddNums.slice(i, i+1));
		i += (i-1) ;
	}

	return oddsTriangle;
	
 }

console.log(rowSumOddNumbers(9));