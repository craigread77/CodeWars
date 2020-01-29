function getSum(a, b) {
	if (a === b) return b;

	min = Math.min(a, b);
	max = Math.max(a, b);

	let total = 0;
	let i = min;
	while (i <= max) {
		total += i;
		i++;
	}

	return total;

}

console.log(getSum(5, 20));