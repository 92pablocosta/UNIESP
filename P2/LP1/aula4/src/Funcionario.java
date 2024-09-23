public class Funcionario {

    private int horas;
    private int valor_hora;
    private int salario_semanal;

    public void setHoras(int horas) {
        this.horas = horas;
    }
    public int getHoras() {
        return horas;
    }

    public void setValor_hora(int valor_hora) {
        this.valor_hora = valor_hora;
    }

    public int getValor_hora() {
        return valor_hora;
    }

    public int calculaSalario() {
        salario_semanal = valor_hora * horas;
        return salario_semanal;
    }

    public int calculaSalario_mes() {
        return salario_semanal * 4;
    }

}
