// JS mod 2 - taulukot

const names = [];
// Alkioon viittaaminen indeksin avulla
names[0] = 'Aku';
names[1] = 'Iines';

console.log(names[2]);

// Taulukon loppuun lisääminen
names.push('Hannu');
console.log(names);

// Taulukkon viimeisen arvon poistaminen
const lastName = names.pop();
console.log(names);
console.log(lastName);
names.unshift('Minni');

const ages = [4, 55, 6];
// console.log(ages.length);

for (let i = 0; i < ages.length; i++) {
    console.log(ages[i], names[i]);
}
console.log('-');
// Taulukko tulostus taaksepäin
for (let i = ages.length-1; i >= 0; i--) {
    console.log(ages[i], names[i]);
}

// samaten kun pythonissa for i in range()
for (const name of names) {
    console.log('Nimi: ' + name);
}

ages.reverse();
console.log(ages);

//  console.log(ages.toReversed());

//  arvon etsiminen taulukosta

const searchParam = 'Aku'
//
if (names.includes(searchParam)) {
    console.log(searchParam + ' löytyi.');
    // katsotaan missä kohtaa taulukko löydetty alkion arvo on
    console.log(names.indexOf(searchParam));
} else {
    console.log(searchParam + ' ei löytynyt.');
}

//  taulukon järjestäminen aakkos järjestykseen
ages.sort();
console.log(ages);

//  pienimmästä numeerisestä arvosta suurinpaan
ages.sort((a, b) => a-b);
console.log(ages);

const person1 = {
  age:67,
  name: 'Roope',
};

const person2 = {
  age: 24,
  name: 'Aku'
};

person1.lastName = 'Ankka';
person2.name = 'Donald';

console.log(person1, person2);

delete person1.lastName;
console.log(person1, person2);

//  sijoittaminen olion taulukkoon

const persons = [person1, person2]
persons.push({name: names[0], age: ages[0]});
console.log(persons);

for (const person of persons){
  console.log(`Nimi:${person.name}, Ikä: ${person.age}`);
}


