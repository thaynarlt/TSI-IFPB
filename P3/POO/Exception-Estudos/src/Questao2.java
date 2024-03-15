// Nesta questão você deve identificar as partes problemáticas do código e reescrevê-lo utilizando
// tratamento de exceções. Ou seja, devem ser identificadas todas as exceções que podem ser
// levantadas e, para cada uma, deve ser dado o tratamento adequado que, nesse exercício,
// significa alertar o usuário quanto ao problema. Entretanto, nesse programa a leitura dos valores
// deve ser feita, mesmo que para isso o usuário tenha que tentar informar várias vezes os valores
// na mesma execução do programa.

import java.util.Scanner;

public class Questao2 {

    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);

        System.out.println("Eu sei dividir!");
        System.out.println("Informe o primeiro valor: ");
        int x = teclado.nextInt();
        System.out.println("Informe o segundo valor: ");
        int y = teclado.nextInt();
        double r = (x/y);
        System.out.println("O resultado da divisão é: " + r);

    }
}