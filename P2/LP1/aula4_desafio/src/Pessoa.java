public class Pessoa {

    private String nome;
    private double peso, altura, imc;

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getNome() {
        return nome;
    }

    public void setPeso(double peso) {
        this.peso = peso;
    }

    public double getPeso() {
        return peso;
    }

    public void setAltura(double altura) {
        this.altura = altura;
    }

    public double getAltura() {
        return altura;
    }

    public void calcula_imc() {
        imc = peso / (altura * altura);
        System.out.println("O seu IMC é " + String.format("%.2f", imc));
    }

    public void faixas_imc() {

        if (imc < 18.50) {
            System.out.println("Você está abaixo do peso.");
        } else if (imc >= 18.50 && imc < 25) {
            System.out.println("Você está no seu peso normal!");
        } else if (imc >= 25) {
            System.out.println("Você está obeso, procure um médico.");
        }

    }


}
