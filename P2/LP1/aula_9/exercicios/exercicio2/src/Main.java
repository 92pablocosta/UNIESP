import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        Refeicao r1 = new Entrada("Pablo", 18, Dieta.TRADICIONAL);

        System.out.println("Cliente: " + r1.getCliente());
        System.out.println("Mesa: " + r1.getMesa());
        System.out.println("Dieta: " + r1.getDieta());

        r1.preparar();
    }
}
