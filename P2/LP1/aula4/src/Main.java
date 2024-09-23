import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        Funcionario f = new Funcionario();

        System.out.print("Digite a quantidade de horas trabalhadas: ");
        f.setHoras(sc.nextInt());
        System.out.print("Digite o valor da hora: ");
        f.setValor_hora(sc.nextInt());

        System.out.println("Você trabalhou " + f.getHoras() + " horas.");
        System.out.println("O valor da hora trabalhada é de R$" + f.getValor_hora() + "/h");
        System.out.println("Seu salário SEMANAL é de R$" + f.calculaSalario());
        System.out.println("Seu salário MENSAL é de R$" + f.calculaSalario_mes());

    }
}