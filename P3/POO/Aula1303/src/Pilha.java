import java.util.ArrayList;

public class Pilha {

	private ArrayList<String> dados = new ArrayList<>();

	public void empilhar(java.lang.String string) {
		dados.add(string);
	}

	public void desempilha() throws Exception{
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
