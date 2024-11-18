import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int mesa;
        String nome;
        int opcao;


        System.out.println("Bem vindo ao Restaurante ComeIESP");
        System.out.println("Em que mesa você está?");
        mesa = sc.nextInt();

        System.out.println("Qual o seu nome?");
        nome = sc.next();

        System.out.println("Alguma restrição de dieta?");
        System.out.println("[1] Sem restrições");
        System.out.println("[2] Vegana");
        System.out.println("[3] Gluten-Free");
        opcao = sc.nextInt();



    }
}
