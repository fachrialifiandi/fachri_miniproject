const expressionDisplay = document.getElementById("expression");
const resultDisplay = document.getElementById("result");

let currentInput = "";

function appendToDisplay(input){
    currentInput += input;
    resultDisplay.textContent = currentInput.replace(/\*/g, " x ").replace(/\//g, " ÷ ");
}

function clearDisplay(){
    currentInput = "";
    expressionDisplay.textContent = "";
    resultDisplay.textContent = '0';
}

function calculate(){

    try{
        expressionDisplay.textContent = currentInput.replace(/\*/g, " x ").replace(/\//g, " ÷ ") + " =";
        const calculation = eval(currentInput);
        resultDisplay.textContent = calculation;
        currentInput = calculation.toString();
    }
    catch(error){
        resultDisplay.textContent = "Error";
        currentInput = "";
    }
    
}