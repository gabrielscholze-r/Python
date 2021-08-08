import json

try:
    # verifica a existencia de um arquivo historico
    historicofat = json.load(open('historicofat.json', 'r'))
except (IOError, ValueError):
    # caso não exista, cria um dicionario historico para criar um arquivo ao fim do programa
    historicofat = {}

def fat(n):
    try:
        return historicofat[n] #tenta retornar um numero que ja existe no dicionario
    except:
        if n < 2: #condição de base
            return 1
        else:
            fat1 = fat(n-1)
            historicofat[n-1] = fat1 #adicionando os termos ecessarios para calcular n ao dicionario
            #após todos os calculos necessários para achar o n termo na sequencia, os numeros encontrados são salvos para encurtar o processamento posteriormente
            json.dump(historicofat, open('historicofat.json', 'w'))
            #retorna o termo n
            return n * fat(n-1)
