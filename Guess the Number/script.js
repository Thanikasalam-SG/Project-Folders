 //selecting the input box, paragraph
 var guessnumber = document.getElementById("guessnumber")
 var result = document.getElementById("result")
 var score = document.getElementById("score")
 var randomNumber = Math.floor(Math.random()*10)+1
 var totalscore = 10
 function check()
 {
     var enternumber = guessnumber.value
     if(randomNumber == enternumber)
     {
         result.textContent="Right"
         alert("You Won...")
     }
     else
     {
         totalscore = totalscore-1
         score.textContent="Your Score:"+totalscore
         result.textContent="Wrong"
     }
 }