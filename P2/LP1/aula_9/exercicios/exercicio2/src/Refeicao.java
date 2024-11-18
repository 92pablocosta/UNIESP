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

    // metodo unico da classe
    public void tipoDieta(int opcao) {
        switch (opcao) {
            case 1:
                dieta = Dieta.TRADICIONAL;
                break;
            case 2:
                dieta = Dieta.VEGANA;
                break;
            case 3:
                dieta = Dieta.GLUTEN_FREE;
                break;
            default:
                System.out.println("Opção inválida");
        }
    }

    // Set
    public void setMesa(int mesa) {
        this.mesa = mesa;
    }
    public void setCliente(String cliente) {
        this.cliente = cliente;
    }
    public void setDieta(Dieta dieta) { this.dieta = dieta; }

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
