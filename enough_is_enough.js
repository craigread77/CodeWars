function deleteNth(arr,n){
	var logs = {};
	return arr.filter((a) => {
		logs[a] = (logs[a] || 0) + 1;
		return logs[a] <= n;
	})
}

console.log(deleteNth([1, 2, 3, 4, 4, 4, 4], 2)) // Only allow 2 of the same value, delete the extras