const form = document.querySelector('form');
const nameInput = document.getElementById('name');
const emailInput = document.getElementById('email');
const messageInput = document.getElementById('message');

form.addEventListener('submit', function(event) {
  event.preventDefault();

  // Validate name
  if (!nameInput.value) {
    alert('Please enter your name.');
    return;
  }

  // Validate email
  if (!emailInput.value || !emailInput.value.includes('@')) {
    alert('Please enter a valid email address.');
    return;
  }

  // Validate message
  if (!messageInput.value) {
    alert('Please enter a message.');
    return;
  }

  // Submit data to server
  const data = {
    name: nameInput.value,
    email: emailInput.value,
    message: messageInput.value,
  };

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
});
