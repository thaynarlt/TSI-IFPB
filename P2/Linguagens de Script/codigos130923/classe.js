//Criando classe e objetos em JavaScript

//Criando Classe
class Company{
    constructor(name, founded,industry){
        this.fullName = name;
        this.founded = founded;
        this.industry = industry
    }

    //Função para calcular o tempo de criação
    obterExistencia(){
        const anoAtual = new Date();
        return anoAtual.getFullYear() - this.founded;
    }

    getName(){
        return this.fullName;
    }
    setName(name){
        this.fullName = name;
    }

}
/*
//Declarando Objeto
const amazon = new Company('Amazon', 1994, 'E-commerce');
//Funciona mas pode ser melhor inicializando
amazon.name = 'Amazon';

const facebook = new Company('Facebook', 2004, 'Social')
const alphabet = new Company('Alphabet', 2015, 'Search')

console.log(amazon.founded);

Company.prototype.kind = 'Internet Company';
console.log(amazon.obterExistencia());
console.log(amazon.getName());

amazon.setName('AWS')
console.log(amazon.getName());
*/
export default Company;