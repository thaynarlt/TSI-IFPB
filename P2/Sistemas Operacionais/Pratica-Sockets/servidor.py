import socket
from pathlib import Path

HOST = '127.0.0.1' #Coloque o host aqui!
PORT = 8000

print('=== Servidor ===')

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)

udp.bind(orig)

def trata_opcoes(msg):
    # 1 /tmp
    valores = msg.split(sep=':')
    operacao = valores[0]
    caminho = ':'.join(valores[1:])
    caminho = Path(caminho)

    # LERDIR:/tmp/
    # CRIARDIR:/tmp/eu
    # EXCLUIRDIR:/tmp/eu
    # MOSTRAR:/tmp/eu/proxima_prova.txt

    msg = ''
    res = ''
    if operacao == "LERDIR":
        # Mostra o conteúdo do diretório.
        print('LERDIR:' + str(caminho))
        res += f'\nArquivos e pastas encontradas em {caminho}\n'
        for arquivo in caminho.iterdir():
            res += str(arquivo) + '\n'
    elif operacao == "CRIARDIR": # Cria novo diretório.
        print('CRIARDIR:' + str(caminho))
        caminho.mkdir(parents=True, exist_ok=True)
        res += f'\nPasta {caminho} criada com sucesso!\n'
    elif operacao == "EXCLUIRDIR": # Exclui diretório.
        print('EXCLUIRDIR:' + str(caminho))
        caminho.rmdir()
        res += f'\nPasta {caminho} removida com sucesso!\n'
    elif operacao == "MOSTRAR": # Mostrar conteúdo de um arquivo.
        print('MOSTRAR:' + str(caminho))
        res += f'\Lendo de {caminho}:\n'
        res += str(caminho.read_text())
    return res

while True:
    try:
        msg, cliente = udp.recvfrom(1024)
        res = trata_opcoes(msg.decode())
        print('RECEBI DE', cliente, 'A MENSAGEM', msg.decode(encoding='utf-8', errors='backslashreplace'))
        udp.sendto(res.encode(encoding='utf-8', errors='backslashreplace'), cliente)
        print('RESPOSTA ENVIADA')
    except Exception as err:
        print(f"ERRO: {err}")
        udp.sendto(str(err).encode(encoding='utf-8', errors='backslashreplace'), cliente)




