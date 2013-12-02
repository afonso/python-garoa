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

def xor_bytes(senha:bytes, conteudo:bytes) -> bytes:
    pares = zip(itertools.cycle(senha), conteudo)
    return bytes(a ^ b for a, b in pares)

def xor_cifra(senha:str, claro:str) -> bytes:
    saida = xor_bytes(senha.encode(CODIF), claro.encode(CODIF))
    return saida

def xor_decifra(senha:str, cifrado:bytes) -> str:
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

    if tipo == 'cifrar':
        print('Cifrando:', nome_entrada)

        arq_entrada = open(nome_entrada, 'rt', encoding = CODIF)
        texto = arq_entrada.read()
        arq_entrada.close()

        saida = xor_cifra(senha, texto)

        nome_arq_saida = nome_entrada + '.blob'
        arq = open(nome_arq_saida, 'wb')
        arq.write(saida)
        arq.close()

    elif tipo == 'decifrar':
        print('Decifrando:', nome_entrada)
        arq = open(nome_entrada, 'rb')
        blob = arq.read()
        texto = xor_decifra(senha, blob)
        print(texto)

if __name__ == '__main__':
    main()