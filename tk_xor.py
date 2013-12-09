CODIF = 'utf-8'

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
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

def abrirArquivo():
    return filedialog.askopenfile(mode = 'r')

def processar(*args):
    if tipo.get() == 'cifrar':
        with open(arquivo.get(), 'rt', encoding = CODIF) as arq_entrada:
            texto = arq_entrada.read()
        saida = xor_cifra(senha.get(), texto)

        nome_arq_saida = arquivo.get() + '.blob'
        with open(nome_arq_saida, 'wb') as arq:
            arq.write(saida)

    elif tipo.get() == 'decifrar':
        with open(arquivo.get(), 'rb') as arq:
            blob = arq.read()
        texto = xor_decifra(senha.get(), blob)

        nome_arq_saida = arquivo.get() + '.dec'
        with open(nome_arq_saida, 'wb') as arq:
            arq.write(bytes(texto, CODIF))

root = Tk()
root.title("XOR - Cifra / Decifra")

status = StringVar()
status.set("Digite os campos \ne selecione um tipo")
statusLabel = Label(textvariable = status, height = 5)
statusLabel.pack()

tipo = StringVar()
strTipoCifrar = Radiobutton(text = 'Cifra', variable = tipo, value = 'cifrar')
strTipoCifrar.pack()

strTipoDecifrar = Radiobutton(text = 'Decifra', variable = tipo, value = 'decifrar')
strTipoDecifrar.pack()

labelSenha = StringVar()
labelSenha.set("Digite a senha:")
labelSenhaConfig = Label(textvariable = labelSenha, height = 1)
labelSenhaConfig.pack()

campoSenha = StringVar()
senha = Entry(textvariable = campoSenha, show = "*")
senha.pack()

labelArquivo = StringVar()
labelArquivo.set("Digite o nome do arquivo:")
labelArquivoConfig = Label(textvariable = labelArquivo, height = 1)
labelArquivoConfig.pack()

campoArquivo = StringVar()
arquivo = Entry(textvariable = campoArquivo)
arquivo.pack()

botaoArquivo = Button(text='Abrir Arquivo', command = abrirArquivo)
botaoArquivo.pack()

botao = Button(text = "Rodar", command = processar)
botao.pack()

root.bind('<Return>', processar)

root.mainloop()