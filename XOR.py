"""
Cifra XOR

Aplica ciclicamente um XOR combinando os bytes da senha com os bytes do conteudo.

	>>> s = 'pizza'
	>>> t = 'Garoando'
	>>> xor_decifra('pizza', xor_cifra('pizza', t))
	'Garoando'

"""
CODIF = 'utf-8'
senha = 'garoas'
import itertools

def xor_bytes(senha, conteudo):
	pares = zip(itertools.cycle(senha), conteudo)
	return bytes(a ^ b for a, b in pares)

def xor_cifra(senha, claro):
	saida = xor_bytes(senha.encode(CODIF), claro.encode(CODIF))
	return saida

def xor_decifra(senha, cifrado):
	saida = xor_bytes(senha.encode(CODIF), cifrado)
	return saida.decode(CODIF)

def main():
    import sys
    
    if len(sys.argv) < 4:
        nome_entrada = input('nome do arquivo: ')
        tipo = input('qual o tipo da acao? (cifrar|decifrar): ')
        senha = input('senha: ')
    elif len(sys.argv) == 4:
        nome_entrada = sys.argv[3]
        tipo = sys.argv[1]
        senha = sys.argv[2]
    else:
        print("modo usar: XOR.py [cifrar|decifrar] [senha] [nome_arquivo]")
        sys.exit(-1)

    arq_entrada = open(nome_entrada, 'rt')

    if tipo == 'cifrar':
    	print('Cifrando:', nome_entrada)
    	for linha in arq_entrada:
        	linha = linha.rstrip()
        	saida = xor_cifra(senha, linha)
        	print(saida)
    elif tipo == 'decifrar':
    	print('Decifrando:', nome_entrada)
    	for linha in arq_entrada:
	        linha = linha.rstrip()
	        saida = xor_decifra(senha, linha)
	        print(saida)

    arq_entrada.close()

if __name__ == '__main__':
    main()