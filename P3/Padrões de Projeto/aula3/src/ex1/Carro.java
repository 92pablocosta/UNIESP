package ex1;

public class Carro extends Veiculo{

    int portas;

    public Carro(String marca, String modelo, int portas) {
        super(marca, modelo);
        this.portas = portas;
    }

    @Override
    public String toString() {
        return "Veiculo [Marca= " + marca + ", modelo= " + modelo + ", Portas= " + portas + "]";
    }
}
