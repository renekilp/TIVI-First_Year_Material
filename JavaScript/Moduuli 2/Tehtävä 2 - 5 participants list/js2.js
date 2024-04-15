'use strict';

const participantAmount = parseInt(prompt('Kuinka monta osallistujaa haluat?'));
const participantList = document.querySelector('ol');
let i = 0


while (i < participantAmount) {
    const participantInput = prompt('Syötä osallistujan nimi:');
    const participant = document.createElement('li');
    participant.textContent = participantInput;
    participantList.appendChild(participant);
    i ++;
}

const reverseParticipants = participantList.querySelectorAll('li');
for (let i = reverseParticipants.length - 1; i >= 0; i-- ) {
    participantList.appendChild(reverseParticipants[i]);
}