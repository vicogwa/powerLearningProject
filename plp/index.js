document.getElementById("count-el").innerText = 0

// Get the necessary elements from the DOM
let countEl = document.getElementById("count-el");
let saveEl = document.getElementById("save-el");

console.log(countEl)
console.log(saveEl)

let count = 0; 

// Function to increment the count
function incrementCount() {
    count += 1; 
    countEl.textContent = count; 
}

function save(){
    let countStr = count + '-'
    saveEl.textContent += countStr
    // saveEl.textContent = 0
    count = 0
    console.log(count)
}

// Attach the function to the button's click event
document.querySelector("button").addEventListener("click", incrementCount, save);
