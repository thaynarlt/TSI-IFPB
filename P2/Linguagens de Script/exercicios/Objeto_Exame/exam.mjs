export class Exame {
    constructor(pesos, gabarito) {
      this.pesos = pesos;
      this.gabarito = gabarito
      this.exames = [] // exames dos estudantes
    }
  
    add(exame) {
      let nota = 0
  
      Object.keys(exame.respostas).forEach(questao => {
        if (exame.respostas[questao] === this.gabarito[questao]) {
          // Obtem a resposta do aluno, a resposta do gabarito e o peso da questão
          // de acordo com a questão
  
          nota += this.pesos[questao]
        }
      })
  
      exame.nota = nota
  
      this.exames.push(exame)
    }
  
    avg() {
      let soma = 0
  
      this.exames.forEach(exame => {
        soma += exame.nota
      })
  
      return soma / this.exames.length
    }
  
    lt(limite) {
      // Retornar uma lista das notas menores que o limite
      const notas = this.exames.map(exame => {
        return exame.nota
      })
  
      return notas.filter(nota => nota < limite)
    }

    min(count = 1) {
        let notas = this.exames.map((gabarito) => gabarito.nota);
    
        notas.sort((a, b) => a - b);
    
        return notas.slice(0, count);
      }
    
    max(count = 1) {
        let notas = this.exames.map((gabarito) => gabarito.nota);
    
        notas.sort((a, b) => a - b);
    
        return notas.slice(-count);
      }
  
    gt(limite) {
      // Retornar uma lista das notas menores que o limite
      const notas = this.exames.map(exame => {
        return exame.nota
      })
      
      return notas.filter(nota => nota > limite)
    }
  }
