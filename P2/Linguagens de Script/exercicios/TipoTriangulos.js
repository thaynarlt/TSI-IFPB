// Tipos de triângulos
//a<b+c and b<c+a and c<a+b

function verificarTriangulo(a,b,c) {
    if (a<b+c && b<c+a && c<a+b) {
        if (a ===b && b ===c) {
            return "Equilátero"; //Todos os lados iguais
        } else if (a === b || b === c || c === a) {
            return "Isósceles"; //Dois lados iguais
        } else {
            return "Escaleno"; //Todos os lados diferentes
        }
    } else {
        return 'Não formam um triângulo';
    }
}

// Exemplos de chamada da função com diferentes conjuntos de lados
console.log(verificarTriangulo(3, 3, 3)); // Equilátero
console.log(verificarTriangulo(3, 4, 4)); // Isósceles
console.log(verificarTriangulo(5, 12, 13)); // Escaleno
console.log(verificarTriangulo(1, 2, 3)); // Não forma um triângulo
