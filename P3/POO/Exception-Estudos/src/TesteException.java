// O código abaixo lança uma exceção (propositalmente) e interrompe sua execução. Utilizando o
// tratamento de exceções, corrija a classe com o objetivo de não parar sua execução. OBS: A
// Exception lançada é ArrayIndexOutOfBoundsException.

public class TesteException {
    public static void main(String[] args) {
        System.out.println("início do main");
        try {
            metodo1();
        } catch (ArrayIndexOutOfBoundsException e) {

        }
        System.out.println("Fim do main");
    }

    static void metodo1() {
        System.out.println("inicio do método1");
        metodo2();
        System.out.println("Fim do método1");
    }

    static void metodo2() {
        System.out.println("início do método2");
        int[] array = new int[10];
        try {
                for (int i = 0; i <=15; i++) {
                array[i] = i;
                System.out.println(i);
            }
        }catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("índice fora do limite");
        }

        System.out.println("fim do método2");
    }
}
