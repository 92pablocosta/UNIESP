package ex2;

public class Carro {
    String marca;
    String modelo;
    String ano;

    public Carro(String marca, String modelo) {
        this.marca = marca;
        this.modelo = modelo;
        this.ano = "Indisponível";
    }

    public Carro(String marca, String modelo, String ano) {
        this.marca = marca;
        this.modelo = modelo;
        this.ano = ano;
    }

    void exibirInfo() {
        System.out.println("Marca: " + marca);
        System.out.println("Modelo: " + modelo);
        System.out.println("Ano: " + ano);
    }
}
