'use strict';

function locationSuccess(location) {
  console.log('Käyttäjä paikannettu!', location);
}

function locationError(error) {
  console.log('Käyttäjän paikannus epäonnistui!', error);
}

const locationOptions = {
  timeout: 1000
}

//  tätä käytetään tapahtumamäärittelijänä, kun p-mäppäintä painetaan2
function locateUser(event){
  if (event.key === 'p') {
   navigator.geolocation.getCurrentPosition(locationSuccess, locationError, locationOptions);
   console.log('paikannusnäppäin tapahtui', event)
  }
}

const section2 = document.querySelectorAll('section')[1];
const pElement = section2.querySelector('p');
pElement.textContent = 'muokattu';

const newP = document.createElement('p');
newP.textContent = 'Uusi kappale';
section2.append(newP);
//  newP.style = 'color: blue';
newP.classList.add('blue')

const thirdSection = document.querySelector('#third-section');
thirdSection.innerHTML =`
  <h2>Kolmanne osion otsikko</h2>
  <p>
    Tässä taas tekstiä.
  </p>`

//  Tapahtumamäärrittely

const buttonElement = document.querySelector('button');
buttonElement.addEventListener('click', (event) => {
  event.stopPropagation();
  console.log('button clicked!');
  //  newP.classList.add('red');
  //  newP.classList.remove('blue');
  newP.classList.toggle('red');
  newP.classList.toggle('blue');
})

document.addEventListener('keypress', locateUser)

//  'mouseover'
document.addEventListener('contextmenu', (event) =>{
  console.log(event)
  event.preventDefault();
  alert('Ei toimi');
})

newP.addEventListener('click', () =>{
  newP.textContent = 'Hasu temppu! 🥶'
})

document.addEventListener('click', (event)=> {
  console.log('sivua klikattu!', event);
})