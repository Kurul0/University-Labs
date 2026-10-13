const fs = require("fs");

let maxCount = 0;
let maxLine = "";

let fileContent = fs.readFileSync("G:\\My Drive\\Programming_part2\\Lab8\\F1.txt", "utf-8");
let lines = fileContent.split(/\r?\n/);

for (let line of lines) {
    let currentKCount = line.toLowerCase().split('к').length - 1;
    if (currentKCount > maxCount) {
        maxCount = currentKCount;
        maxLine = line;
    }
}

if (maxCount === 0) {
    console.log("У тексті немає символів 'к'");
} else {
    fs.writeFileSync("G:\\My Drive\\Programming_part2\\Lab8\\F2.txt", maxLine, "utf-8");
    console.log("Done\n")
    console.log(`The biggest amount of 'к' symbols is in: ${maxLine}\n`);
    console.log(`The amount of 'к' symbols = ${maxCount}\n`);
}