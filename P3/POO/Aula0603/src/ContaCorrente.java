import java.util.Scanner;

public class ContaCorrente {

    // Atributos: numero, saldo e nomeTitular
    public int numero;
    public Double saldo;
    public String nomeTitular;

    // Construtores para inicializar os valores dos atributos dos objetos instanciados
    public ContaCorrente(int numero, Double saldo, String nomeTitular) {
        this.numero = numero;
        this.saldo = saldo;
        this.nomeTitular = nomeTitular;
    }

    // Métodos: depositar e sacar (parametrizando o valor a ser depositado ou sacado)
    // depositar: Não possui retorno, devendo apenas incrementar o valor do saldo
    public void depositar(double valor) {
        saldo += valor;
    }

    // sacar: Deve retornar um valor booleano (true – se sacou com sucesso, pois há saldo suficiente, decrementando-o; ou false caso contrário)
    public boolean sacar(double valor) {
        if (valor <= saldo) {
            saldo -= valor;
            return true; // Sacou com sucesso
        } else {
            return false; // Saldo insuficiente
        }
    }

    // Getters e Setters
    public int getNumero() {
        return numero;
    }

    public void setNumero(int numero) {
        this.numero = numero;
    }

    public Double getSaldo() {
        return saldo;
    }

    public void setSaldo(Double saldo) {
        this.saldo = saldo;
    }

    public String getNomeTitular() {
        return nomeTitular;
    }

    public void setNomeTitular(String nomeTitular) {
        this.nomeTitular = nomeTitular;
    }

    // Método principal (main)
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Quantas contas você deseja criar? (máximo de 10): ");
        int numContas = scanner.nextInt();
        if (numContas > 10) {
            System.out.println("O número máximo de contas é 10. Criando 10 contas...");
            numContas = 10;
        }

        // Criando array para armazenar as contas correntes
        ContaCorrente[] contas = new ContaCorrente[numContas];

        // Instâncias das contas correntes com valores lidos do teclado
        for (int i = 0; i < numContas; i++) {
            System.out.println("Número da conta " + (i + 1) + ":");
            int numero = scanner.nextInt();
            System.out.println("Saldo Inicial da conta " + (i + 1) + ":");
            double saldoInicial = scanner.nextDouble();
            scanner.nextLine(); // Limpa o buffer do scanner
            System.out.println("Nome do titular da conta " + (i + 1) + ":");
            String nomeTitular = scanner.nextLine();
            contas[i] = new ContaCorrente(numero, saldoInicial, nomeTitular);
        }

        // Menu de operações
        int opcao;
        do {
            System.out.println("\n --------- MENU ---------");
            System.out.println("1. Depositar");
            System.out.println("2. Sacar");
            System.out.println("3. Saldo");
            System.out.println("4. Sair");
            System.out.print("Escolha a operação desejada: ");
            opcao = scanner.nextInt();

            switch (opcao) {
                case 1:
                    depositar(contas, scanner);
                    break;
                case 2:
                    sacar(contas, scanner);
                    break;
                case 3:
                    exibirSaldo(contas, scanner);
                    break;
                case 4:
                    System.out.println("Encerrando o programa!");
                    break;
                default:
                    System.out.println("Opção inválida. Tente novamente.");
            }

        } while (opcao != 4);

        scanner.close();
    }

    // 1) Depositar: Ao digitar a opção 1, o programa deverá ler o número da conta e o valor a ser depositado, e realizar a operação.
    public static void depositar(ContaCorrente[] contas, Scanner scanner) {
        System.out.println("Informe o número da conta: ");
        int numeroConta = scanner.nextInt();

        for (ContaCorrente conta : contas) {
            if (conta != null && conta.getNumero() == numeroConta) {
                System.out.println("Informe o valor a ser depositado: ");
                double valor = scanner.nextDouble();
                conta.depositar(valor);
                System.out.println("Depósito realizado com sucesso! Seu Saldo atual: " + conta.getSaldo());
                return;
            }
        }
        System.out.println("Conta não encontrada.");
    }

    // 2) Sacar: Ao digitar a opção 2, o programa deverá ler o número da conta e o valor a ser sacado, e realizar a operação, testando se o saque ocorreu ou não.
    public static void sacar(ContaCorrente[] contas, Scanner scanner) {
        System.out.println("Informe o número da conta:");
        int numeroConta = scanner.nextInt();

        for (ContaCorrente conta : contas) {
            if (conta != null && conta.getNumero() == numeroConta) {
                System.out.println("Informe o valor que deseja sacar: ");
                double valor = scanner.nextDouble();
                boolean saqueRealizado = conta.sacar(valor);
                if (saqueRealizado) {
                    System.out.println("Saque realizado com sucesso. Saldo atual: " + conta.getSaldo());
                } else {
                    System.out.println("Saldo insuficiente para o saque.");
                }
                return;
            }
        }
        System.out.println("Conta não encontrada!");
    }

    // 3) Saldo: Ao digitar a opção 3, o programa deverá ler o número da conta e exibir o seu saldo.
    public static void exibirSaldo(ContaCorrente[] contas, Scanner scanner) {
        System.out.println("Informe o número da conta: ");
        int numeroConta = scanner.nextInt();

        for (ContaCorrente conta : contas) {
            if (conta != null && conta.getNumero() == numeroConta) {
                System.out.println("Saldo da conta: " + conta.getSaldo());
                return;
            }
        }
        System.out.println("Conta não encontrada.");
    }
}
