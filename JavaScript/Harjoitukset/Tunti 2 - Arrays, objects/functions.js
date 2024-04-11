//  perinteinen funktio määritelmä
function doSomething(){
  console.log('doing something...')
}

doSomething();

const doSomethingMore = () => {
  console.log('something else...');
};

doSomethingMore()

const ages = [4, 36, 55];

function compare(val1, val2) {
  return val1 - val2;
}

console.log(compare(4, 33));
console.log()
//  ages.sort(function(val1,val2) => val1 - val2); ei toimi
console.log(ages)

//  tulostaa arrayn sisällön ja paluattaa uuden taulukon käännetyssä jörjestyksessä
function longArray(array){
  //  funktion sisältä esitelty näkyy vain funktion sisällä
  //  const ages = [];
  //  console.log(ages);
  console.log(array);
  const newArray = array.slice(0);
  newArray.reverse();
  return newArray;
}

const reversedAges = longArray(ages)

console.log(ages);
console.log(reversedAges)