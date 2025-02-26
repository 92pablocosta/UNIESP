package ex2;

public class Main {
    public static void main(String[] args) {
        Carro c1 = new Carro("BMW", "X6");
        Carro c2 = new Carro("Mercedes", "C380", "2023");

        c1.exibirInfo();
        c2.exibirInfo();
    }
}
