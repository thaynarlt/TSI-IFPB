public class Data {



    //Os atributos privados: dia, mês e ano;
    private int dia;
    private int mes;
    private int ano;

    //Construtor

    public Data(int dia, int mes, int ano) {
        this.dia = dia;
        this.mes = mes;
        this.ano = ano;
    }

   

    //Métodos acessadores (get) e modificadores (set);

    public int getDia() {
        return dia;
    }
    
    public int getMes() {
        return mes;
    }
    
    public int getAno() {
        return ano;
    }

    @Override
    public String toString() {
        return "Data: " + "/" + mes + "/" + ano;
    }


    //Método toString(), que devera retornar a data no formato dd/mm/aaaa.
    public static void main(String[] args) {
        Data d = new Data(16,4,1979);

        System.out.println(d);
    }
    
    //Escreva um programa para criar objetos dessa classe e testar os métodos.
    
}


