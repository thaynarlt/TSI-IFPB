public class IMC {
    public static void main(String[] args) {
        double peso = 150;
        double altura = 1.70;
        double imc = peso / Math.pow(altura,2);
        if (imc < 18.5)
            System.out.println("Abaixo da média");
        else
            if (imc < 25)
                System.out.println("Normal");
            else
                if (imc <30)
                    System.out.println("Acima do normal");
                else
                    if (imc <35)
                        System.out.println("Obesidade 1");
                    else
                        if (imc <40)
                            System.out.println("Obesidade 2");
                            else
                                System.out.println("Morbidade");
}}
