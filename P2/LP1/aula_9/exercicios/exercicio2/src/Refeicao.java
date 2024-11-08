public abstract class Refeicao {

    private int mesa;
    private String cliente;
    protected Dieta dieta;


    public Refeicao(int mesa, String cliente, Dieta dieta) {
        this.cliente = cliente;
        this.mesa = mesa;
        this.dieta = dieta;
    }

    // métodos para todas as subclasses
    public abstract void preparar();
    public abstract void servir();

    // Set
    public void setMesa(int mesa) {
        this.mesa = mesa;
    }
    public void setCliente(String cliente) {
        this.cliente = cliente;
    }

    // Get
    public int getMesa() {
        return mesa;
    }
    public String getCliente() {
        return cliente;
    }
    public Dieta getDieta() {
        return dieta;
    }


}
