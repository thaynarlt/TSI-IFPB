from Aluno import Aluno
# Exemplo de uso da classe Aluno

aluno1 = Aluno(20231009, "Felipe Chupetinha") #Passamos dois argumentos para a classe "Aluno" criada
aluno1.adicionaNota(9.9) #Adiciona nota para a "lista de notas" do aluno
aluno1.adicionaNota(4.3) #Adiciona nota para a "lista de notas" do aluno

print(f"Nome: {aluno1.nome}") #Imprime o nome do aluno
print(f"Matrícula: {aluno1.getMatriculaFormatada()}") #Imprime a matrícula formatada do aluno
print(f"Média: {aluno1.media()}") #Imprime a média do aluno

#aluno1.nome = "Maria"  # Modifica o nome do aluno
#print(f"Novo Nome: {aluno1.nome}") 