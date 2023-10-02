function show(companies){
    companies.forEach(
        element => {
        console.log(`${element.name.padEnd(15, '.')}${element.founded}`);
        }
    );
}

//Exportanto de forma default
export default show;