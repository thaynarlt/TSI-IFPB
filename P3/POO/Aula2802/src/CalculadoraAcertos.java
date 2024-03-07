
/*Faça em java: Uma prova objetiva tem 10 questões cujas
respostas podem ser “a”, “b”, “c”, “d” ou “e”.
Faça um programa para ler as respostas do gabarito e as respostas da prova e calcular o número de acertos
Exemplo:
Digite o gabarito com 10 caracteres:
aaeecbdbcd
Digite a resposta com 10 caracteres
aaeecccaad
Número de acertos: 6 */

import java.util.Scanner;

public class CalculadoraAcertos {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Ler o gabarito
        System.out.println("Digite o gabarito com 10 caracteres:");
        String gabarito = scanner.nextLine();

        // Ler as respostas do aluno
        System.out.println("Digite a resposta com 10 caracteres:");
        String respostas = scanner.nextLine();

        // Verificar número de acertos
        int numAcertos = contarAcertos(gabarito, respostas);

        // Exibir o resultado
        System.out.println("Número de acertos: " + numAcertos);
    }

    public static int contarAcertos(String gabarito, String respostas) {
        int acertos = 0;
        for (int i = 0; i < gabarito.length(); i++) {
            if (gabarito.charAt(i) == respostas.charAt(i)) {
                acertos++;
            }
        }
        return acertos;
    }
}
