// Preferences_Form.tsx

import React, { useState, } from 'react';
import '../css/form_style.css';

interface PrefFormData {
    username: string;
    password: string;
  }

const Pref: React.FC = () => {
  const [formData, setFormData] = useState<PrefFormData>({ username: '', password: '' });

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = event.target;
    setFormData({ ...formData, [name]: value });
  };
  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    try {
        const response = await fetch('http://127.0.0.1:5000/login', {
            method: 'POST',
            mode: 'cors',
            headers: { 
            'Content-Type': 'application/json',
           },
            body: JSON.stringify(formData),
        });
        const data = await response.json();
        console.log(response)
        if (response.ok) {
            alert('Login successful!');
        } else {
            alert(data.message);
        }
    } catch (error) {
        console.error(error);
        alert('An error occurred while logging in. Please try again later.');
    } 
  };

  return (
    <div className="pref-container">
      <h1>Habits and Preferences</h1>
      <h4>Please answer honestly, as potential roommate matches will be more accurate.</h4>
      <form id="habits-form">
        <script>
            function question(x, y, z) {
                this.label = x;
                this.question = y;
                this.options = z;
            }

            const questions = [
                new question("l-smoke", "I am willing to live with a smoker:", ["yes", "no", "maybe"]),
                new question("smoke", "I smoke:", ["often", "sometimes", "never"]),
                new question("l-drink", "I am willing to live with someone who drinks:", ["yes", "no", "maybe"]),
                new question("drink", "I drink:", ["often", "sometimes", "never"]),
                new question("extrovert", "On a scale of 1 (extremely introverted) to 5 (extremely extroverted), I describe myself as:", ["1", "2", "3", "4", "5"]),
                new question("l-extrovert", "On a scale of 1 (extremely introverted) to 5 (extremely extroverted), I get along best with people who are:", ["1", "2", "3", "4", "5"]),
                //ADD NEW QUESTIONS HERE
                //new question("", "", ["1", "2", "3", "4", "5"]),
                //new question("", "", ["1", "2", "3", "4", "5"]),
                //new question("", "", ["1", "2", "3", "4", "5"]),
                new question("l-sexuality", "I am comfortable living with someone who has a different sexual orientation than me:", ["yes", "no"]),
                new question("sexuality", "My sexual orientation:", ["straight", "gay", "bisexual", "other", "prefer not to say"]),
                new question("l-gender", "I am comfortable living with someone of a different gender identity than me:", ["yes", "no"]),
                new question("gender", "My gender identity:", ["cisgender", "transgender", "other", "prefer not to say"]),
            ]

            var form = document.getElementById("habits-form");

            for (var i = 0; i < questions.length; i++) {
                var curr = questions[i];

                var div = document.createElement("div");

                var label = document.createElement("label");
                label.textContent = curr.question;
                label.setAttribute("for", curr.label);

                div.appendChild(label);

                for (var j = 0; j < curr.options.length; j++) {
                    var radioButton = document.createElement("input");
                    radioButton.type = "radio";
                    radioButton.required = "required";
                    radioButton.name = curr.label;
                    radioButton.value = curr.options[j];
                    radioButton.id = curr.label + curr.options[j];

                    var radioLabel = document.createElement("label");
                    radioLabel.textContent = curr.options[j];
                    radioLabel.setAttribute("for", curr.label + curr.options[j]);

                    div.appendChild(radioButton);
                    div.appendChild(radioLabel);
                    div.appendChild(document.createElement("br"));
                }

                var span = document.createElement("span");
                span.class = "error";
                var p = document.createElement("p");
                p.id = curr.label + "_error";
                span.appendChild(p);
                div.appendChild(span);

                form.appendChild(div);
            }
        </script>
        <button type="submit" class="btn">Submit</button>
      </form>
    </div>
  );
};


export default Pref;