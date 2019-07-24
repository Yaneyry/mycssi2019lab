let redButton = document.querySelector('#red')
let greenButton = document.querySelector('#green')
let blueButton = document.querySelector('#blue')
let responsebox = document.querySelector('#response-box')
let list = '';

redButton.addEventListener('click', (e) => {
  console.log("You clicked the red button!");
  list = list + "Red"
  responsebox.style.backgroundColor = "red";
  responsebox.innerHTML = list;

});



greenButton.addEventListener('click', (e) => {
  console.log("You clicked the green button!");
  list = list + "green"
  responsebox.style.backgroundColor = "green";
  responsebox.innerHTML = list;



});


blueButton.addEventListener('click', (e) => {
  console.log("You clicked the blue button!");

  list = list + "blue"
  responsebox.style.backgroundColor = "blue";
  responsebox.innerHTML = list;

});
