var form = document.querySelector('form');
const proxyUrl = 'https://cors-anywhere.herokuapp.com/';
const apiUrl = 'http://127.0.0.1:5000/submit-form';

form.addEventListener('submit', function(event) {
  event.preventDefault();
  
  var formData = new FormData(form);

  var output = "";
  var count = 0;
  var data = {}
  for (const [name, value] of formData.entries()) {
    output += `${name}: ${value}\n`;
    data[name] = value;
    count += 1;
  }
  if (count != 17) {
    output = "PLEASE SELECT A RESPONSE FOR ALL QUESTIONS.";
    document.getElementById("resultArea").textContent = output;
  } else {
    document.getElementById("resultArea").textContent = "We've received your responses!";

    (async () => {
      try {
        const response = await fetch(proxyUrl + apiUrl, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(formData),
        })
        .then(response => {
          alert("Form submitted successfully");
        })
        .catch(error => {
          alert("There was an error receiving the responses.");
        });
      } catch (error) {
        alert('There was an error submitting the form.');
      }
    })();
  }
});