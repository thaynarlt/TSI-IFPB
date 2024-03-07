public class TesteLargura {
    public static void main(String[] args) {
        Retangulo r = new Retangulo();
        r.id = 1;
        r.largura = 1;
        r.comprimento = 7;
        System.out.println(r.calcularArea());
        r.largura = 3;
        r.comprimento = 4;
        System.out.println(r.calcularArea());
    }
}
