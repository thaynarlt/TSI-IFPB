public class Conta {
    private double saldo = 50;

    public void sacar(double valor) throws Exception{
        if (this.saldo < valor)
            throw new Exception("quantia errada!");
        else
            this.saldo = this.saldo - valor;
    }

    public static void main(String[] args) {
        
        Conta c = new Conta();

        try {
            c.sacar(100);
        }
        catch(Exception e) {
            System.out.println(e.getMessage());
        }
    }
}
