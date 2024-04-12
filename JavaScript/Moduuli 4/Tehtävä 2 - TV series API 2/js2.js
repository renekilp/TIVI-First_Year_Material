'use strict';

document.addEventListener('submit', async function(evt) {
    // ... prevent the default action.
    evt.preventDefault();
    // create an object 'data' to which user input from the form is added and the http method is set to POST
    const data = {
        body: JSON.stringify({
            fname: document.querySelector('input[name=fName]').value,
            lname: document.querySelector('input[name=lName]').value
        }),
        method: 'POST',
        headers: {
              'Content-type': 'application/json',
        },
    }
    // send the data
   try {
      const response = await fetch('/someAddressWhereDataIsSent', data);  // Send data to server and receive a server response
      if (!response.ok) throw new Error('Invalid input!');         // If an error occurs, an error message is thrown
      const json = await response.json();                                 // convert the loaded text JSON to a JavaScript object / array
      console.log('result', json);                                        // print the result to the console
   } catch (e) {
      console.log('error', e);
   }
});