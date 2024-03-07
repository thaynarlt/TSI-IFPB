public class Retangulo {
    public int id;
    public double largura;
    public double comprimento;

    public double calcularArea() {
        return largura * comprimento;
    }

    public static void main(String [] args){
        Retangulo r = new Retangulo();
        double result = r.calcularArea();
        System.out.println(result);
    }
}
