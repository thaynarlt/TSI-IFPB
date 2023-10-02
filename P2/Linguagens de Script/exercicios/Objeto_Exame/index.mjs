import { Exame } from './exam.mjs'

const pesos = {
  q1: 2,
  q2: 3,
  q3: 2,
  q4: 2,
  q5: 2

}

const gabarito = {
  q1: 'a',
  q2: 'b',
  q3: 'a',
  q4: 'c',
  q5: 'd'
}

const exame = new Exame(pesos, gabarito)

const reposta1 = {
  estudante: 'Lucas',
  respostas: {
    q1: 'a',
    q2: 'b',
    q3: 'a',
    q4: 'c',
    q5: 'd'
  }
}

exame.add(reposta1)

const reposta2 = {
  estudante: 'João',
  respostas: {
    q1: 'a',
    q2: 'c',
    q3: 'a',
    q4: 'e',
    q5: 'b'
  }
}

exame.add(reposta2)

const reposta3 = {
  estudante: 'Maria',
  respostas: {
    q1: 'a',
    q2: 'c',
    q3: 'b',
    q4: 'c',
    q5: 'd'
  }
}

exame.add(reposta3)

console.log(exame.avg());

console.log(exame.lt(6)) // notas menores que 6
console.log(exame.gt(10)) // notas maiores que 10