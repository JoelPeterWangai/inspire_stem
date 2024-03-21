const randomnumber = Math.floor(Math.random() + 100) +1;

let attempt =0;

function CheckGuess(){
    const guess= parseInt(document.getElementById("guessfield").value)
    attempt++;
    if(isNaN(guess)|| guess < 1 || guess > 100){
        setMessage("Please enter a valid number between 1 and 100")
        return;
    }
    if(guess === randomnumber){
        setMessage("Congratualtions! Guessed correctly")
        document.getElementById("guessfield").disabled=true;
    }else if(guess < randomnumber){
        setMessage("Too low,try again");
    }else{
        setMessage("Too high,try again");
    }
}
function setMessage(message){
    document.getElementById("message").textContent = message;
}