import show from './lib.js';
import company from './classe.js';

const company = {
    name: "",
    founded: 0,
    industry: ""
}
company.kind = "Internet Company";

const amazon = { ... company};
const facebook = { ... company};
const alphabet = { ... company};

amazon.nome = 'Amazon';
amazon.founded = 1994;
amazon.industry = 'E-commerce';

facebook.nome = 'Facebook';
facebook.founded = 2004;
facebook.industry = 'Social';

alphabet.nome = 'Alphabet Inc';
alphabet.founded = 2015;
alphabet.industry = 'Search, Cloud';

console.log(company);
console.log(amazon.kind);

const arrayCompanies = [];

arrayCompanies.push(amazon);
arrayCompanies.push(facebook);
arrayCompanies.push(alphabet);

show(arrayCompanies);

const microsoft = new company('Microsoft', 1978, 'OS');
arrayCompanies.push(microsoft);

