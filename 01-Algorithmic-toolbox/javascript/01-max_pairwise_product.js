function program() {
    console.log("Welcome to Max Pairwise program");
    const readline = require("readline").createInterface({
        input: process.stdin,
        output: process.stdout
    })

    let n = 0;
    let numbers = [];
    readline.question("Enter n: ", number => {
        n = parseInt(number);
        readline.question("Enter numbers ", input => {
            numbers = input.split(' ').map(Number);
            readline.close();

            console.log(calculateMaxPairwise(n, numbers));
        });
    })
}

function calculateMaxPairwise(n, numbers) {
    if (n < 1) {
        return -1;
    } else if (n == 1)
    {
        return n;
    } else if (n == 2)
    {
        return numbers[0] * numbers[1];
    }

    let max1 = numbers[0] > numbers[1] ? numbers[0] : numbers[1];
    let max2 = numbers[0] > numbers[1] ? numbers[1] : numbers[0];

    for (let i = 2; i <= numbers.length; i++) {
        if (numbers[i] > max1) {
            max2 = max1;
            max1 = numbers[i];
        } else if (numbers[i] > max2) {
            max2 = numbers[i]
        }
    }

    return max1 * max2;
}

program();

