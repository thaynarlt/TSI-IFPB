import java.util.InputMismatchException; //Classe que será usada para lidar com exceções
import java.util.Scanner;

public class Questao2 {

	public static void main(String[] args) {
		Scanner teclado = new Scanner(System.in);

		System.out.println("Informe um numero: ");
		int numero = teclado.nextInt();

		do { // Inicia loop do-while para que o código seja executado dentro do loop e assim por diante
			try { // Onde as operações podem lançar exceções são colocadas

				System.out.println("Eu sei dividir!");
				System.out.println("Informe o primeiro valor: ");

				int x = teclado.nextInt();
				System.out.println("Informe o segundo valor: ");

				int y = teclado.nextInt();
				double r = (x / y);

				System.out.println("O resultado da divisão é: " + r);
			}
            // capturar exceções específicas que podem ser lançadas dentro do bloco try 
			catch (ArithmeticException ae) { //ArithmeticException (divisão por zero)
				System.err.println("Não se divide por zero");
			} 
			catch (InputMismatchException ime) { //InputMismatchException (entrada inválida)
				System.err.println("Você inseriu um caractere,  insira um numero");
			}
			teclado.nextLine();
		} while (numero == 0); //será executado pelo menos uma vez e continuará a ser executado enquanto numero for igual a zero.
		
		teclado.close(); //Fechar a entrada de mais dados
	}
}