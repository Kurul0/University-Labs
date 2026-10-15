const A = new Set(prompt("\nВведи числа від 1 до 25 через пробіл:\n").split(" ").map(Number));
const B = new Set(prompt("\nВведи числа від 1 до 25 через пробіл:\n").split(" ").map(Number));

const C = new Set([...A, ...B]); //об'єднання
const D = new Set([...A].filter(x => B.has(x))); //перетин
const E = new Set([...A].filter(x => !B.has(x))); //різниця
const F = new Set([...B].filter(x => !A.has(x))); //різниця

console.log("A належить C:", [...A].every(x => C.has(x)));
console.log("D належить C:", [...D].every(x => C.has(x)));
const temp = new Set([...E, ...F, ...D]);
console.log("C = E перетин F перетин D:", C.size === temp.size && [...C].every(x => temp.has(x)));
console.log("Перетин E і F = пуста множина", [...E].every(x => !F.has(x)));

console.log("A:", A);
console.log("B:", B);
console.log("C:", C);
console.log("D:", D);
console.log("E:", E);
console.log("F:", F);