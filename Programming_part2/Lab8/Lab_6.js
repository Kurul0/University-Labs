let userInput = prompt("Enter 12 months in Ukrainian, separated by SPACES:");
let monthsList = userInput.trim().split(/\s+/);
let isValid = true;

const validMonths = ["січень", "лютий", "березень", "квітень", "травень", "червень", "липень", "серпень", "вересень", "жовтень", "листопад", "грудень"];
for (let word of monthsList) {
    if (!validMonths.includes(word.toLowerCase())) {
        isValid = false;
        console.log(`"${word}" is not valid. Please restart the program with valid data.`);
        break;
    }
}

if (isValid === true) {
    monthsList.sort((a, b) => a.localeCompare(b, "uk"));
    console.log("Sorted list of months in alphabetical order:");
    for (let word of monthsList) {
        console.log(word);
    }
}