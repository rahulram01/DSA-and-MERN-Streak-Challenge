const arr = [4, 5, 6, 7, 8];

function double(x) {
  return x * 2;
}
function triple(x) {
  return x * 3;
}

const doublearr = arr.map(double);
const triplearr = arr.map(triple);

console.log(doublearr);
console.log(triplearr);

const binaryArr = arr.map(function binary(x) {
  return x.toString(2);
});

function isODD(x) {
  return x % 2;
}
const findOdd = arr.filter(isODD);

console.log(binaryArr);
console.log(findOdd);

function reducerr(acc, curr) {
  acc = acc + curr;
  return acc;
}
const sumR = arr.reduce(reducerr, 0);
console.log(sumR);

const sumRR = arr.reduce(function reducerrr(acc, curr) {
  acc = acc + curr;
  return acc;
}, 0);
console.log(sumRR);
