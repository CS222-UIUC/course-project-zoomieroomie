var form = document.querySelector('form');

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
    document.getElementById("resultArea").textContent = output;

    (async () => {
      try {
        const response = await fetch('/submit-form', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(data),
        });

        if (response.ok) {
          alert('Form submitted successfully.');
          form.reset();
        } else {
          alert('1-There was an error submitting the form.');
        }
      } catch (error) {
        alert('2-There was an error submitting the form.');
      }
    })();
  }
});
