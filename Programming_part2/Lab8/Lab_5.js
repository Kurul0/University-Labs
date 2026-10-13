const m = 6;
const n = 8;
const matrix = [];

for (let i = 0; i < m; i++){
    matrix.push([]);
    for (let j = 0; j < n; j++) { 
        let value = Math.floor(Math.random() * 100) + 1;
        matrix[i].push(value);
    }
}

console.log("\nПочаткова матриця\n");
for (let i = 0; i < m; i++) {
    let row = [];
    for (let j = 0; j < n; j++) {
        row.push(String(matrix[i][j]).padStart(4, " "));
    }
    console.log(row.join(" "));
}

let maxValue = matrix[0][0];
for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
        if (matrix[i][j] > maxValue) {
            maxValue = matrix[i][j];
        }
    }
}
console.log("\nНайбільше число:" + maxValue);

console.log("\nНормалізована матриця:\n");
for (let i = 0; i < m; i++) {
    let row = [];
    for (let j = 0; j < n; j++) {
        matrix[i][j] = matrix[i][j] / maxValue;
        row.push(matrix[i][j].toFixed(4));
    }
    console.log(row.join(" "));
}
console.log("");