import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        do {
            Scanner sc = new Scanner(System.in); // inicia o scanner
            Calculadora c = new Calculadora(); // chama a classe Calculadora

            int n1, n2; // Cria variáveis n1 e n2

            System.out.println("Qual operação gostaria de fazer?");
            System.out.println("1 - Soma");
            System.out.println("2 - Subtracao");
            System.out.println("3 - Multiplicacao");
            System.out.println("4 - Divisao");
            System.out.println("5 - Sair");
            int opcao = sc.nextInt();

            System.out.print("Digite o primeiro número: ");
            int num1 = sc.nextInt();

            System.out.print("Digite o segundo número: ");
            int num2 = sc.nextInt();

            if (opcao == 1) {
                c.somar(num1, num2);
                System.out.println(num1 + " + " + num2 + " = " + c.somar(num1, num2));
            } else if (opcao == 2) {
                c.subtrair(num1, num2);
                System.out.println(num1 + " - " + num2 + " = " + c.subtrair(num1, num2));
            } else if (opcao == 3) {
                c.multiplicar(num1, num2);
                System.out.println(num1 + " * " + num2 + " = " + c.multiplicar(num1, num2));
            } else if (opcao == 4) {
                c.dividir(num1, num2);
                System.out.println(num1 + " / " + num2 + " = " + c.dividir(num1, num2));
            } else if (opcao == 5) {
                break;
            }

        }while(true);
    }
}
