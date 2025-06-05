public class Celular extends Produto {
    private int id;
    private String OS;
    private boolean Novo;

    public Celular(String nome, double preco, int id, String OS, boolean Novo) {
        super(nome, preco);
        this.id = id;
        this.OS = OS;
        this.Novo = Novo;
    }

    @Override
    public void exibirInfo() {
        super.exibirInfo();
        System.out.println("id: " + id);
        System.out.println("OS: " + OS);
        System.out.println("Novo: " + (Novo ? "Sim" : "Não"));
    }
}