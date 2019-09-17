var uniqueInOrder = function(iterable) {
    if (typeof(iterable) === 'string') {
        iterable = iterable.split('');
    }

    var currentValue = '';
    var previousValue = '';

    return iterable.filter((a) => {
        previousValue = currentValue;
        currentValue = a;
        return previousValue !== a;
    })



}

console.log(uniqueInOrder([1, 2, 3, 3, 2, 1]));