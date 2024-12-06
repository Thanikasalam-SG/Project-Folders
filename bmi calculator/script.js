// JavaScript Code for BMI Calculator
document.getElementById("calculate").addEventListener("click", function (event) {
    event.preventDefault();

    // Get input values
    const age = document.getElementById("age").value;
    const height = document.getElementById("height").value;
    const weight = document.getElementById("weight").value;
    const male = document.getElementById("male").checked;
    const female = document.getElementById("female").checked;

    // Validate inputs
    if (!age || !height || !weight || (!male && !female)) {
        alert("Please fill all fields correctly.");
        return;
    }

    if (age < 2 || age > 120) {
        alert("Age must be between 2 and 120.");
        return;
    }

    if (height <= 0 || weight <= 0) {
        alert("Height and weight must be greater than zero.");
        return;
    }

    // Calculate BMI
    const bmi = (weight / ((height / 100) ** 2)).toFixed(1);

    // Determine BMI category
    let category = "";
    if (bmi < 16) {
        category = "Severe Thinness";
    } else if (bmi >= 16 && bmi < 17) {
        category = "Moderate Thinness";
    } else if (bmi >= 17 && bmi < 18.5) {
        category = "Mild Thinness";
    } else if (bmi >= 18.5 && bmi < 25) {
        category = "Normal";
    } else if (bmi >= 25 && bmi < 30) {
        category = "Overweight";
    } else if (bmi >= 30 && bmi < 35) {
        category = "Obese Class I";
    } else if (bmi >= 35 && bmi < 40) {
        category = "Obese Class II";
    } else {
        category = "Obese Class III";
    }

    // Display result
    const resultDiv = document.querySelector(".result");
    resultDiv.querySelector(".Bmi").innerHTML = `BMI = ${bmi} kg/m<sup>2</sup>`;
    resultDiv.querySelector("h3").textContent = category;
    resultDiv.style.display = "block";
});
