import random as rd

"""
Dando um ficheiro de legendas .srt, cria um novo ficheiro com algumas palavras censuradas.
Isto é para ajudar a aprender uma nova lingua por aquisição (como crianças aprendem).
Isto dá-te alguma ajuda (algumas palavras não estarão censuradas), mas faz com que tenhas de entender o contexto para entender as palavras censuradas.
"""

nome_ficheiro = input("Nome do ficheiro .srt de legendas: ")
percentagem = float(input("Percentagem de legendas a censurar: "))

ficheiro = open("{}.srt".format(nome_ficheiro), "r")  # abrir ficheiro de legendas em modo de leitura apenas
novo_ficheiro = open("[censurado] {}.srt".format(nome_ficheiro), "w")  # vou criar novo ficheiro para escrever lá as legendas novas
censurar = False  # mudar para True ao detetar '-->' numa linha e volta a False quando a linha só tem '\n'
print("\nO ficheiro foi encontrado e aberto. Edição a decorrer.")

while True:
    linha = ficheiro.readline()  # ler linha seguinte
    if linha == "":
        break  # significa que já acabou o ficheiro, acabando o ciclo while

    if censurar is False:
        novo_ficheiro.write(linha)  # adicionar linha ao novo ficheiro
        if len(linha) > 16:
            if linha[13:16] == "-->":
                censurar = True

    elif censurar is True:
        if linha == "\n":
            censurar = False
            novo_ficheiro.write(linha)
            continue  # vai apenas continuar para a próxima iteração, avançando o que está abaixo (não edita esta linha)
        linha_lista = linha.split()
        nova_linha = ""
        for j in range(len(linha_lista)):
            if rd.random() < percentagem / 100:
                linha_lista[j] = "*"  # substitui a palavra por '*'
            nova_linha += (linha_lista[j] + " ")  # adicionar palavra (editada ou não) na nova linha que irá para o ficheiro
        nova_linha += "\n"
        novo_ficheiro.write(nova_linha)

# fechar os ficheiros usados, sempre necessário ao editar
ficheiro.close()
novo_ficheiro.close()
x = input("Processo terminado. Clica ENTER para fechar.")
