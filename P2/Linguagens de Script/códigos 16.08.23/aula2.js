// Estrutura de decisão

const operando1 = 30;
const operando2 = 5;
let operador = '+';
let resultado = undefined

if (operador === '+'){
    resultado = operando1 + operando2;
}   else if(operador === '-'){
    resultado = operando1 - operando2;
}   else if(operador === '*'){
    resultado = operando1 * operando2;
}   else if(operador === '/'){
    resultado = operando1 / operando2;
}   else if(operador === '%'){
    resultado = operando1 % operando2
}