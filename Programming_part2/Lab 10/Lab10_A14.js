const fs = require("fs");

const findSigns = (text) => {
    const validSigns = new Set([',', '.', '!', ';', ':', '-', '?'])
    return new Set([...text].filter(char => validSigns.has(char)));
}   

let fileContent = fs.readFileSync("E:\\Codding\\University-Labs\\Programming_part2\\Lab 10\\Lab10_A14_INPUT.txt", "utf-8");
    const result = findSigns(fileContent);

console.log('\nThe result is\n', result);