function buildTower(n) {
	var tower = [];
	for (let i = n; i > 0; i--) {
		tower.unshift(' '.repeat(n-i) + '*'.repeat(i-1) + '*' + '*'.repeat(i-1) + ' '.repeat(n-i))
	}

	return tower;
}

console.log(buildTower(80));














