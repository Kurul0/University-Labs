const fs = require('fs');

const fullText = fs.readFileSync('G:\\My Drive\\Programming_part2\\Lab 9\\Text_A13.txt', 'utf-8').split('\n');

let linesCount = 0;
for (let line of fullText) {
    let cleanLine = line.trim();
    if (cleanLine.length < 40) {
        linesCount++;
    }
}
console.log(`\nThe amount of lines with less than 40 characters = ${linesCount}\n`)