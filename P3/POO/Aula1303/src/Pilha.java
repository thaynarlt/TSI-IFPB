import java.util.ArrayList;

public class Pilha {

	private ArrayList<String> dados = new ArrayList<>();
	
	public void empilhar(String s) {
		dados.add(s);
	}
	
	public void desempilha() {
		int ultimo = dados.size() - 1;
		dados.remove(ultimo);
	}
	public boolean vazia() {
		return dados.isEmpty();
	}
	public String topo() {
		int ultimo = dados.size() - 1;
		return dados.get(ultimo);
	}
	public void esvaziar() {
		dados.clear();
	}
	
}