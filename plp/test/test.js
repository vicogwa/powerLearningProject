// Global variables to track the game state
let cards = [];
let sum = 0;
let hasBlackJack = false;
let isAlive = false;

// References to HTML elements to update the game state display
const messageEl = document.getElementById('message-el');
const cardsEl = document.getElementById('cards-el');
const sumEl = document.getElementById('sum-el');

// Function to generate a random card value
function getRandomCard() {
    // Generate a random number between 1 and 13 (inclusive)
    const randomNumber = Math.floor(Math.random() * 13) + 1;
        if (randomNumber > 10) {
        return 10;
    } else if (randomNumber === 1) {
        // Ace is worth 11 points, can be adjusted if needed
        return 11;
    } else {
        return randomNumber;
    }
}

// Function to start a new game
function startGame() {
    // Set game status flags
    isAlive = true; 
    hasBlackJack = false; 
    
    // Initialize or reset game variables
    cards = []; 
    sum = 0; 

    // Deal two initial cards to the player
    for (let i = 0; i < 2; i++) {
        let card = getRandomCard();
        cards.push(card);
        sum += card;
    }
    
    // Update the game display with the initial cards and sum
    renderGame();
}

// Function to update the game state display
function renderGame() {
    cardsEl.textContent = 'Cards: ';
    for (let i = 0; i < cards.length; i++) {
        // Append each card value to the cards display
        cardsEl.textContent += cards[i] + ' ';
    }
    
    // Display the total sum of card values
    sumEl.textContent = 'Sum: ' + sum;
    
    // Determine the appropriate message based on the sum
    if (sum <= 20) {
        messageEl.textContent = 'Do you want to draw a new card?';
    } else if (sum === 21) {
        messageEl.textContent = 'BlackJack! You win!';
        hasBlackJack = true;
    } else {
        messageEl.textContent = 'You are out of the game!';
        isAlive = false; 
    }
}

// Function to draw a new card and update the game state
function newGame() {
    if (isAlive === true && hasBlackJack === false) {
        let card = getRandomCard();
                cards.push(card);
                sum += card;
        
        // Update the game display with the new card and updated sum
        renderGame();
    }
}
