const fs = require('fs');

const fullText = fs.readFileSync('G:\\My Drive\\Programming_part2\\Lab 9\\Text_B13.txt', 'utf-8');
const textStep1 = fullText.replace(/\bin\b/g, '_TEMP_');
const textStep2 = textStep1.replace(/\bon\b/g, 'in');
const finalText = textStep2.replace(/\b_TEMP_\b/g, 'on');

fs.writeFileSync('G:\\My Drive\\Programming_part2\\Lab 9\\Text_B13_2.txt', finalText);

console.log('\nDone\n');