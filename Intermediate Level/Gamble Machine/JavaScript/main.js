const prompt = require("prompt-sync")();

const ROWS = 3;
const COLS = 3;

// the possibility
const SYMBOLS_COUNT = {
  A: 2,
  B: 4,
  C: 6,
  D: 8,
};

// multiplier
const SYMBOL_VALUES = {
  A: 5,
  B: 4,
  C: 3,
  D: 2,
};

//1. Deposit some money
const deposit = () => {
  while (true) {
    const depositAmount = prompt("Enter a deposit amount: ");
    const numberDepositAmount = parseFloat(depositAmount);

    if (isNaN(numberDepositAmount) || numberDepositAmount <= 0) {
      console.log("Invalid deposit amount, try again.");
    } else {
      return numberDepositAmount;
    }
  }
};

//2. Determine number of lines to bet on
const getNumberOfLines = () => {
  while (true) {
    const lines = prompt("Enter the number of lines to bet on (1-3): ");
    const numberOfLines = parseFloat(lines);

    if (isNaN(numberOfLines) || numberOfLines <= 0 || numberOfLines > 3) {
      console.log("Invalid number of lines, try again.");
    } else {
      return numberOfLines;
    }
  }
};

//3. Collect a bet amount
const getBet = (balance, lines) => {
  while (true) {
    const bet = prompt("Enter the bet per line: ");
    const numberBet = parseFloat(bet);

    if (isNaN(numberBet) || numberBet <= 0 || numberBet > balance / lines) {
      console.log("Invalid bet, try again.");
    } else {
      return numberBet;
    }
  }
};

// 4. spin the slot machine
const spin = () => {
  const symbols = [];
  for (const [symbol, count] of Object.entries(SYMBOLS_COUNT)) {
    for (let i = 0; i < count; i++) {
      symbols.push(symbol);
    }
  }

  const reels = [];
  // while i or j less than column, increment i or j
  for (let i = 0; i < COLS; i++) {
    reels.push([]);
    // copy the symbols that we have in reelSymbols
    const reelSymbols = [...symbols];
    for (let j = 0; j < ROWS; j++) {
      const randomIndex = Math.floor(Math.random() * reelSymbols.length);
      const selectedSymbols = reelSymbols[randomIndex];
      reels[i].push(selectedSymbols);
      reelSymbols.splice(randomIndex, 1);
    }
  }

  return reels;
};

// 5. give the user winning
const transpose = (reels) => {
  // initialization
  const rows = [];
  // run based on the number of rows
  for (let i = 0; i < ROWS; i++) {
    rows.push([]);
    // In each row, we take elements from each coloumn
    for (let j = 0; j < COLS; j++) {
      // swap rows and columns
      rows[i].push(reels[j][i]);
    }
  }

  return rows;
};

const printRows = (rows) => {
  for (const row of rows) {
    let rowString = "";
    for (const [i, symbol] of row.entries()) {
      rowString += symbol;
      if (i != row.length - 1) {
        rowString += " | ";
      }
    }
    console.log(rowString);
  }
};

const getWinnings = (rows, bet, lines) => {
  let winnings = 0;

  // main loop: runs as many as the number of lines placed bets by the player
  for (let row = 0; row < lines; row++) {
    // take one row from (rows)
    const symbols = rows[row];
    // flag
    let allSame = true;
    // check each symbol in the row one by one.
    for (const symbol of symbols) {
      // compares the current symbol with the first symbol in the row
      if (symbol != symbols[0]) {
        allSame = false;
        break;
      }
    }
    if (allSame) {
      // calculate the bet value multiplied by the symbol multiplier value
      winnings += bet * SYMBOL_VALUES[symbols[0]];
    }
  }

  return winnings;
};

const game = () => {
  let balance = deposit();
  while (true) {
    console.log("You have a balance of $" + balance);
    const numberOfLines = getNumberOfLines();
    const bet = getBet(balance, numberOfLines);
    balance -= bet * numberOfLines;
    const reels = spin();
    const rows = transpose(reels);
    printRows(rows);
    const winnings = getWinnings(rows, bet, numberOfLines);
    balance += winnings;
    console.log("You Won, $" + winnings.toString());

    if (balance <= 0) {
      console.log("You ran out of the money");
      break;
    }
    const playAgain = prompt("Do you want to play again? (y/n) ");

    if (playAgain != "y") console.log("Thanks For Playing !");
    break;
    console.clear();
  }
};

game();
