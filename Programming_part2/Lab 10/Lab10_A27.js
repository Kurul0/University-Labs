const findOperators = (text) => {
    const validSigns = new Set(['<', '>', '=', '!'])
    return new Set([...text].filter(char => validSigns.has(char)));
}   

const userInput = prompt ("Enter your data with relational operators:");
const result = findOperators(userInput);
console.log('The result is', result);