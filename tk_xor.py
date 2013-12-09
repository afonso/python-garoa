from tkinter import *
from tkinter import ttk
import XOR

root = Tk()
root.title("XOR - Cifra / Decifra")

status = StringVar()
status.set("Digite os campos e selecione um tipo")
statusLabel = Label(textvariable = status, height = 5)

def processar(arquivo, senha, tipo):
    if tipo == 'cifrar':
        print('Cifrando:', nome_entrada)

        with open(nome_entrada, 'rt', encoding = CODIF) as arq_entrada:
            texto = arq_entrada.read()

        saida = xor_cifra(senha, texto)

        nome_arq_saida = nome_entrada + '.blob'

        with open(nome_arq_saida, 'wb') as arq:
            arq.write(saida)

    elif tipo == 'decifrar':
        print('Decifrando:', nome_entrada)

        with open(nome_entrada, 'rb') as arq:
            blob = arq.read()
        
        texto = xor_decifra(senha, blob)
        print(texto)

def abrirArquivo(arquivo):
    with open(arquivo, 'rt', encoding = CODIF):
        campoArquivo = arquivo.read()


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

botao = Button(text = "Rodar", command = processar(arquivo, senha, tipo))
botao.pack()

senha.focus()

root.bind('<Return>', processar(arquivo, senha, tipo))

root.mainloop()