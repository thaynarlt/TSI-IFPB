// Estrutura de decisão

const operando1 = 30;
const operando2 = 5;
let operador = '+';
let resultado = undefined

switch(operador){
    case '+': resultado = operando1 + operando2; break;
    case '-': resultado = operando1 - operando2; break;
    case '*': resultado = operando1 * operando2; break;
    case '/': resultado = operando1 / operando2; break;
    case '%': resultado = operando1 % operando2; break;
    default: resultado = 'Operação não suportada!'
}