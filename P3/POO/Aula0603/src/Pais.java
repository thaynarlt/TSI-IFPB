import java.util.ArrayList;
import java.util.Arrays;

public class Pais {
    
    //Atributos Privados o seu nome,
    //o nome da capital, sua dimensão em Km2
    //uma lista de países com os quais ele faz fronteira (array de String).

    private String nome;
    private String capital;
    private Double dimensao;
    private ArrayList<String> fronteiras = new ArrayList<>();
    

    //Construtor que inicialize o nome, capital e a dimensão do país;
    public Pais(String nome,String capital,Double dimensao) {
        this.nome = nome;
        this.capital = capital;
        this.dimensao = dimensao;
        this.fronteiras = new ArrayList<String>();
    }

    //Métodos de acesso para os atributos indicados no item (a);
    public String getNome() {
        return nome;
    }
    public String getCapital() {
        return capital;
    }
    public Double getDimensao() {
        return dimensao;
    }

    //Método que retorne a lista de países que fazem fronteira;
    //Países que fazem fronteira com Brasil:
    //Argentina, Bolívia, Colômbia, Guiana, Guiana Francesa, Paraguai, Peru, Suriname, Uruguai, Venezuela 

    public ArrayList<String> getFronteiras() {
        return fronteiras;
    }

    // Método que adiciona o nome de país à lista de países que fazem fronteira
    public void adicionarFronteira(String pais) {
        fronteiras.add(pais);
    }

    //Método toString() - retorna o nome do país, capital e o nome dos países que fazem fronteira.
    //Para transformar imprimir o array, usar: Arrays.toString()
    @Override
    public String toString() {
        return "País: " + nome + "\nCapital: " + capital + "\nFronteiras: " + Arrays.toString(fronteiras.toArray());
    }

     // Exemplo de uso
     public static void main(String[] args) {
        Pais brasil = new Pais("Brasil", "Brasília", 8515767.049);
        brasil.adicionarFronteira("Argentina");
        brasil.adicionarFronteira("Bolívia");
        brasil.adicionarFronteira("Paraguai");
        brasil.adicionarFronteira("Uruguai");
        brasil.adicionarFronteira("Colômbia");
        brasil.adicionarFronteira("Peru");
        brasil.adicionarFronteira("Venezuela");
        brasil.adicionarFronteira("Suriname");
        brasil.adicionarFronteira("Guiana");
        brasil.adicionarFronteira("Guiana Francesa");

        System.out.println(brasil);
    }
}



