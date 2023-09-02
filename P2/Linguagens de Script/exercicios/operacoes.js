//SOMA SIMPLES
/*function soma(op1, op2) {
    return op1 + op2;
}

console.log(soma(5,10,15,20,25))
console.log(soma(5))
console.log(soma(5,10)) */

//-----------------------------------------------------------------------------

//SOMA DE TODOS OS ELEMENTOS [I]
/*function soma(...params) { //parâmetros
    let resultado = 0;

    for(const elemI of params) {
        resultado = resultado +elemI
    }
    return resultado
}
console.log(soma(5,10,15,20,25))*/

//-----------------------------------------------------------------------------

//ATIVAR UMA FUNÇÃO ANÔNIMA - (Soma de dois números)

/*let f =10;
f = function(op1,op2) {
    return op1 + op2;
};

console.log(f(15,10));*/

//-----------------------------------------------------------------------------

//Mesmo sentido da função a cima -> + simplificada
f = (op1, op2) => op1 + op2; //Identificado com Return
console.log(f(25,10));

//-----------------------------------------------------------------------------