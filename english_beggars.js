function beggars(values, n) {

    if (n < 1) return [];

    // Crate an object of beggars with their cash amount as value
    var beggars = {};
    for (let i = 1; i <= n; i++) {
        beggars[i] = 0;
    }

    var counter = 1;

    // Loop through the values array, incrementing each beggar property by the avlue amount then moving onto the next beggar 
    for (let i = 0; i < values.length; i++) {

        if (counter > n) counter = 1; // Reset counter if it reaches the number of beggars

        beggars[counter] += values[i];
        counter++;

    }


    return Object.values(beggars);
}

console.log(beggars([1, 2, 3, 4, 5, 6, 7, 8, 9], 12));

// Better method below

/*
function beggars(values, n){
  var out = Array.from("0".repeat(n)).map(Number)
  for(var i=0;i<values.length;i++){
    out[i%n] += values[i]
  }
  return out

  */