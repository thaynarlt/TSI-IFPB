import java.util.ArrayList;

public class Aluno {

    //Atributo matricula (número inteiro), nome (String), notas (ArrayList);
    private int matricula;
    private String nome;
    private ArrayList<Double> notas = new ArrayList<>();

    
    //Construtor para inicializar todos os atributos;
    public Aluno(int matricula, String nome) {
        this.matricula = matricula;
        this.nome = nome;
        this.notas = new ArrayList<Double>();
    }

    //Métodos acessadores getNome() e getMatricula();
    public String getNome() {
        return nome;
    }

    public int getMatricula() {
        return matricula;
    }

    //Método getMedia() que retorna a média das notas;
    public double getMedia() {
        if (notas.isEmpty()) {
            return 0.0;
        }

        double soma = 0;
        for (double nota : notas) {
            soma += nota;
        }
        return soma / notas.size();
    }


    //Método alterador apenas para o nome, setNome()
    public void setNome(String nome) {
        this.nome = nome;
    }


    //Método adicionaNota(nota), para adicionar uma nota ao ArrayList de notas do aluno.
    public void adicionaNota(double nota) {
        notas.add(nota);
    }


    //Escreva um programa para criar objetos dessa classe e testar os métodos.
    public static void main(String[] args) {
        // Criando um novo aluno
        Aluno aluno = new Aluno(123, "João");
        
        // Adicionando notas ao aluno
        aluno.adicionaNota(7.5);
        aluno.adicionaNota(8.0);
        aluno.adicionaNota(6.0);
        
        // Imprimindo informações do aluno
        System.out.println("Nome: " + aluno.getNome());
        System.out.println("Matrícula: " + aluno.getMatricula());
        System.out.println("Média: " + aluno.getMedia());
        
        // Alterando o nome do aluno
        aluno.setNome("Maria");
        System.out.println("Nome alterado: " + aluno.getNome());
    }
}
