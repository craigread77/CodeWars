function removeSmallest(numbers) {

	var minIndex = numbers.indexOf(Math.min(...numbers));
	return [...numbers.slice(0, minIndex), ...numbers.slice(minIndex + 1)];
  
}

console.log(removeSmallest([1, 2, 3, 4, 5]));
