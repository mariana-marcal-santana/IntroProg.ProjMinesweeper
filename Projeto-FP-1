#Exercício 1
#1.2.1
"""
A funcao limpa_texto recebe uma cadeia de caracteres com caracteres brancos\
    e espacos a mais e devolve uma cadeia limpa sem caracteres como\
         \n, \t, \v, \f, \r e com apenas um espaco entre cada palavra.
"""
def limpa_texto(frase):
    #separar a frase em palavras (tirar caracteres brancos) e junta-las
    return ' '.join(frase.split()) 

#1.2.2
"""
A funcao corta_texto recebe uma cadeia de texto limpo e um inteiro e retorna\
    um tuplo com a uma parte de cadeia ate ao caracter na posicao do indice\
        inteiro e outra parte, o resto da string; se o a zona do corte for a\
            meio de uma palavra, a funcao corta pelo espaco anterior a palavra\
                que ficaria cortada.           
"""
def corta_texto(texto_limpo,largura_cadeia):

    if len(texto_limpo) <= largura_cadeia or len(texto_limpo) == 0:
        return (texto_limpo, '') 
        #se a cadeia nao tiver cumprimento para se efetuar um corte

    i=-(len(texto_limpo)-largura_cadeia) 
    #calcular i (indice negativo do inicio da string)

    while i>-len(texto_limpo):
        #calcular o indice do primeiro espaco a partir do corte da cadeia 
        # (a contar de tras)
        if texto_limpo[i]==' ': 
            break
        i-=1

    tuplo_final=(texto_limpo[:i],limpa_texto(texto_limpo[i:])) 
    #concatenar os tuplos com as duas partes da frase

    return tuplo_final

#1.2.3
"""
A funcao insere_espacos recebe uma cadeia limpa e um inteiro positivo\
    se a cadeia tiver apenas uma palavra, retorna essa palavra seguida do numero\
        necessario de espacos para perfazer o comprimento de cadeia igual ao\
            inteiro positivo, se a cadeira tiver 2 ou mais palavras, retorna a cadeia\
                com espacos adicionados a partir da esquerda ate perfazer o comprimento.
"""
def insere_espacos(texto_limpo,largura_cadeia):

    slots=texto_limpo.count(' ') 
    numero_espacos=largura_cadeia-len(texto_limpo)+slots
    lista_texto=texto_limpo.split(' ')
    
    if slots == 0: #cadeia com uma palavra
        cadeia_espacada=texto_limpo+' '*numero_espacos
        return cadeia_espacada
    
    espacos_por_slot=numero_espacos//slots
    espacos_sobra=numero_espacos%slots

    if slots>=1: #cadeia com 2 ou mais palavras
        for i in range(len(lista_texto)-1):
            lista_texto[i]=lista_texto[i]+' '*espacos_por_slot 
            #adicionar numero igual de espacos depois de todas as palavras
            #(excepto a ultima) 
        
        for i in range(espacos_sobra):  
            lista_texto[i]=lista_texto[i]+' ' 
            #adicionar 1 espaço depois das palavras ate a 
            #palavra de indice [espacos_sobra-1]
        cadeia_espacada=''.join(lista_texto)

    return cadeia_espacada

#1.2.4
"""
A funcao justifica_texto recebe uma cadeia de caracteres e uma largura de\
    cadeia e devolve essa cadeia limpa, cortada pela largura indicada (de\
        acordo com a corta_texto) e espacos inseridos em cada segmento cortado\
            da cadeia (de acordo com a insere espacos).
"""
def justifica_texto(cadeia_caracteres,largura_cadeia):

    if not isinstance (cadeia_caracteres,str) or not isinstance (largura_cadeia,int):
        raise ValueError ('justifica_texto: argumentos invalidos')

    if cadeia_caracteres=='':
        raise ValueError ('justifica_texto: argumentos invalidos')

    lista_palavras = cadeia_caracteres.split()

    for palavra in lista_palavras:
        if len(palavra)>largura_cadeia:
            raise ValueError ('justifica_texto: argumentos invalidos')

    texto_limpo=limpa_texto(cadeia_caracteres)

    if len(texto_limpo) <= largura_cadeia:
        texto_limpo = texto_limpo + ' '*(largura_cadeia-len(texto_limpo))
        return (texto_limpo, )
        
    tuplo_cortado=()

    while True:
        segmento_texto1,segmento_texto2=corta_texto(texto_limpo,largura_cadeia) 
        #cortar texto pela largura pedida
        tuplo_cortado+=(segmento_texto1,) #adicinar a parte cortada 

        if len(segmento_texto2)>largura_cadeia and len(segmento_texto1)!=0: 
            #se ainda se puderem efutuar cortes ao segmento2
            texto_limpo=segmento_texto2 
            #atribuir a parte nao cortada a variavel texto limpo

        elif len(segmento_texto2)<=largura_cadeia and len(segmento_texto2)!=0: 
            #se nao se efetuarem mais cortes
            tuplo_cortado+=(segmento_texto2,) 
            #adicionar o ultimo segmento ao tuplo
            break

    lista_cortada=list(tuplo_cortado)

    for i in range(len(lista_cortada)-1):
        lista_cortada[i]=insere_espacos(lista_cortada[i],largura_cadeia) 
        #inserir espacos a cada elemento da lista (excepto o ultimo)

    espacos=largura_cadeia-len(lista_cortada[-1])
    lista_cortada[-1]=lista_cortada[-1]+' '*espacos 
    #para o ultimo elemento da lista manter string "normal" e apenas
    #adicionar espacos no fim
    
    return tuple(lista_cortada)

#Exercício 2
#2.2.1
"""
A funcao calcula_quocientes recebe um dicionario e um interiro e devolve um\
    dicionario com as mesmas chaves do anterior que contenha como valores os\
        quocientes da divisao do valores dicionario inicial por todos os\
            numeros naturais menores ou iguais ao inteiro recebido.
"""
def calcula_quocientes(dicionario_votos_apurados,numero_deputados):

    dicionario_final,lista_partido,list_ext,i={},[],[],1

    for partido in dicionario_votos_apurados:

        while i<=numero_deputados:
            lista_partido+=[dicionario_votos_apurados[partido]/i] 
            #Calcular cada quociente e adiciona-lo a lista do seu partido
            i+=1

        i = 1
        list_ext = [x for x in lista_partido]
        dicionario_final[partido]=list_ext 
        #Criar uma lista com os quocientes de todos os partidos
        lista_partido.clear()

    return dicionario_final

#2.2.2
"""
A funcao atribui_mandatos recebe um dicionario de votos e um numero de\
    deputados e devolve uma lista com os partidos que venceram cada mandato;\
        em casos de empates, a funcao verifica qual o partido com menos\
            deputados e insere esse na lista. Esta funcao utiliza a funcao\
                calcula_quocientes para verificar que partido tem os maiores\
                    quocientes e assim, seleciona-lo          
"""
def atribui_mandatos(dicionario_votos_apurados,numero_deputados):

    dicionario_quocientes = calcula_quocientes(dicionario_votos_apurados, numero_deputados)
    copia_dicionario_votos_apurados = dicionario_votos_apurados.copy()
    valores_votos_inicais = []
    indices_quocientes_votos = {}
    lista_partidos_finais = []

    for partido in dicionario_votos_apurados:
        valores_votos_inicais+=[dicionario_votos_apurados[partido]]   
        #adiciona a uma lista os valores dos votos apurados de cada partido
        indices_quocientes_votos[partido] = 0

    for indice in range(numero_deputados):
        valores_votos_atuais = {}

        for partido in dicionario_votos_apurados:
            valores_votos_atuais[partido] = copia_dicionario_votos_apurados[partido] 
            #dicionario contendo apenas os votos apurados de cada partido
            
        maximo_lista = max(valores_votos_atuais.values())   
        #procura o valor maximo dos votos do respetivo dicionario de votos atuais
        
        lista_partidos = []

        for partido in copia_dicionario_votos_apurados:

            if copia_dicionario_votos_apurados[partido] == maximo_lista:    
                #criar lista com os partidos com o numero max de votos
                lista_partidos+=[partido]

        if len(lista_partidos) >= 2:
            minimo_lista = []   
                #caso sejam mais que dois partidos com o mesmo numero de votos maximo
            for i in lista_partidos:
                minimo_lista += [dicionario_votos_apurados[i]]
            for partido in lista_partidos:                          
                #escolher o partido com o valor minimo para desempate
                if dicionario_votos_apurados[partido] == min(minimo_lista):
                    lista_partidos=[partido]

        lista_partidos = ''.join(lista_partidos)
        indices_quocientes_votos[lista_partidos] += 1  
        #continuar para os segundos quocientes dos votos
    
        lista_partidos_finais += [lista_partidos] 
        #adicionar os partidos ja selecionados a lista final

        if indices_quocientes_votos[lista_partidos]<len(dicionario_quocientes[lista_partidos]):
            copia_dicionario_votos_apurados[lista_partidos] = \
                dicionario_quocientes[lista_partidos][indices_quocientes_votos[lista_partidos]]
                #procurar os votos do proximo quociente, continuando o loop
    
    return lista_partidos_finais

#2.2.3
"""
A funcao obtem_partidos recebe um dicionario com informacoes relativas as\
    eleicoes e retorna a lista dos nomes dos partidos por ordem alfabetica.
"""
def obtem_partidos(dicionario_info):
    lista_votos,lista_info,lista_partidos,lista_final=[],[],[],[]

    for circulo_eleitoral in dicionario_info:
        lista_info+=[dicionario_info[circulo_eleitoral]] 
        #retirar os nomes dos circulos eleitorais

    for elemento in lista_info:
        lista_votos+=[elemento['votos']] 
        #apresentar apenas os nomes dos partidos e os votos respetivos

    for conjunto in lista_votos:
        for keys in conjunto:
            lista_partidos+=[keys] 
            #apresentar apenas os nomes dos partidos

    for j in range(len(lista_partidos)):
        if lista_partidos[j] not in lista_final:
            lista_final+=[lista_partidos[j]] 
            #apresentar os nomes dos partidos sem repeticoes

    return sorted(lista_final) #ordenar alfabeticamente os partidos
                
#2.2.4
"""
A funcao obtem_resultados_eleicoes_erros e uma funcao auxiliar da\
    obtem_resultados_eleicoes e caso algum argumento seja invalido,\
        nao permite a segunda funcao retornar qualquer resultado e\
            devolve um ValueError.
"""
def obtem_resultado_eleicoes_erros(dicionario_info):
    if not isinstance(dicionario_info, dict):
        raise ValueError('obtem_resultado_eleicoes: argumento invalido')
        
    if len(dicionario_info) < 1:
        raise ValueError('obtem_resultado_eleicoes: argumento invalido')
    
    for circulo in dicionario_info:
        if not isinstance(dicionario_info[circulo], dict) or not \
            isinstance(circulo, str) or len(dicionario_info[circulo]) < 1:
            raise ValueError('obtem_resultado_eleicoes: argumento invalido')
        chaves = []
        for i in dicionario_info[circulo]:
            chaves += [i]

        if 'deputados' not in chaves or 'votos' not in chaves:
            raise ValueError('obtem_resultado_eleicoes: argumento invalido')
        elif len(dicionario_info[circulo]) > 2:
            raise ValueError('obtem_resultado_eleicoes: argumento invalido')
        elif not isinstance(dicionario_info[circulo]['deputados'], int)\
            or not isinstance(dicionario_info[circulo]['votos'], dict):
            raise ValueError('obtem_resultado_eleicoes: argumento invalido')
        elif len(dicionario_info[circulo]['votos']) < 1:
            raise ValueError('obtem_resultado_eleicoes: argumento invalido')
        elif dicionario_info[circulo]['deputados'] < 1:
            raise ValueError('obtem_resultado_eleicoes: argumento invalido')
        
        for votos in dicionario_info[circulo]['votos']:
            if not isinstance(dicionario_info[circulo]['votos'][votos], int):
                raise ValueError('obtem_resultado_eleicoes: argumento invalido')
            if dicionario_info[circulo]['votos'][votos] < 0:
                raise ValueError('obtem_resultado_eleicoes: argumento invalido')
"""
A funcao obtem_reseultado_eleicoes recebe informacoes sobre as eleicoes em\
    varios circulos eleitorais e retorna uma lista com tuplos relativos a cada\
        partido que participou na eleicoes, com as informacoes: nome do partido,\
            numero de deputados eleitos e numero de votos conseguidos; esta lista\
                encontra-se ordenada pelo numeros de deputados e em caso de\
                    empate, pelo numero de votos de cada partido.
"""
def obtem_resultado_eleicoes(dicionario_info):

    obtem_resultado_eleicoes_erros(dicionario_info)
    lista_partidos=obtem_partidos(dicionario_info)
    dicionario={}
    dicionario=dicionario.fromkeys(lista_partidos,0)
    #criar um dicionario com os nomes dos partidos como chaves e valores 0
    
    mandatos,valores_circulos_eleitorais,resultado_eleicoes=[],[],[]

    for key in dicionario_info:    
            valores_circulos_eleitorais.append(dicionario_info[key])
            #criar uma lista com os values do dicionario inicial 

    for circulo in valores_circulos_eleitorais:
        for partido in lista_partidos:

            if partido in circulo['votos'].keys():
                #se o partido tiver votos naquele circulo eleitoral
                dicionario[partido] += circulo['votos'][partido]
                #somar o numero de votos obtidos e aos que ja tiver
        mandatos+= atribui_mandatos(circulo['votos'],circulo['deputados'])
        #fazer uma lista com os partidos que ganharam cada mandato

    for partido in lista_partidos:
        numero_mandatos=mandatos.count(partido) 
        #contar o numero de mandatos/ deputados de cada partido
        resultado_eleicoes.append((partido,numero_mandatos,dicionario[partido]))
        #criar uma lista com as informacoes de cada partido 
        #(nome, numero de mandatos e numero de votos)

    resultado_eleicoes=sorted(resultado_eleicoes, key=lambda t: (t[1], t[2]), reverse=True)
    #ordenar a lista anterior seguindo o numero de mandatos e em caso de\
    #desempate, seguindo o numero de votos

    return resultado_eleicoes

#Exercício 3
#3.2.1
"""
A funcao produto_interno multiplica os elementos com mesmo indice\
    de cada tuplo e adiciona-os, retornando essa soma real
"""
def produto_interno(tuplo_linha1,tuplo_linha2):

    res=0
    
    for i in range(len(tuplo_linha1)):
        res+=tuplo_linha1[i]*tuplo_linha2[i] 
        #multiplicar os elementos com indices iguais dos tuplos e soma-los
    
    return float(res) #retornar em formato real

#3.2.2
"""
A funcao verifica convergencia recebe 3 tuplos e um real, calcula o modulo\
    da diferenca entre o resultado do produto interno de cada linha da matriz\
        pelo tuplo solucao e a constante referente a essa linha, compara com a\
            precisao e retorna verdadeiro se o valor do modulo for menor que o\
                real em todas as linhas. 
"""
def verifica_convergencia(tuplo_matriz,tuplo_constantes,tuplo_soluçao_atual,precisao):

    for i in range(len(tuplo_matriz)):#iterar sobre os indices do tuplo

        if not abs(produto_interno(tuplo_matriz[i],tuplo_soluçao_atual)\
            -tuplo_constantes[i])<precisao:
            #comparar o modulo da diferenca entre o produto de uma linha pela
            #solucao atual com a precisao
                return False
        
    return True

#3.2.3
"""
A funcao retira_zeros_diagonal recebe um tuplo matriz e um tuplo de constantes\
    e procura nos elementos da diagonal dessa matriz por um que tenha valor 0;\
         caso encontre troca essa linha (e o valor correspondente no tuplo de\
            de constantes) com outra linha que nao tenha 0 na diagonal
"""
def retira_zeros_diagonal(tuplo_matriz,tuplo_constantes):

    lista_matriz=list(tuplo_matriz)
    lista_constantes=list(tuplo_constantes)

    for i in range(len(lista_matriz)):

        if lista_matriz[i][i]==0: #verificar se ha um 0 na diagonal

            for j in range(len(lista_matriz)):

                if lista_matriz[j][i]!=0 and lista_matriz[i][j]!=0: 
                    #verificar se as linhas podem ser trocadas
                    lista_matriz[j],lista_matriz[i]=\
                        lista_matriz[i],lista_matriz[j] #trocar as linhas
                    lista_constantes[j],lista_constantes[i]=\
                        lista_constantes[i],lista_constantes[j] 
                        #trocar as constantes
                    break

    return (tuple(lista_matriz),tuple(lista_constantes))

#3.2.4
"""
Esta funcao recebe um tuplo de tuplos (linhas da matriz) e compara a soma\
    dos modulos dos valores (nao diagonais) de cada linha com o valor da\
        diagonal; retorna True se os valores da diagonal forem maiores que\
            a soma em todas as linhas.
"""
def eh_diagonal_dominante(tuplo_matriz):
    for i in range(len(tuplo_matriz)): #iterar sobre cada linha da matriz

        soma=0

        for j in range(len(tuplo_matriz[i])): 
            #iterar sobre cada elemento de cada linha da matriz
            if i!=j:
                soma+=abs(tuplo_matriz[i][j]) 
                #calcular a soma dos modulos dos elementos nao diagonais da linha

        if  soma>abs(tuplo_matriz[i][i]): 
            return False
        #se a soma for menor que o modulo do elemento da diagonal

    return True 

#3.2.5
"""
A funcao resolve sistema recebe um tuplo com tuplos (matriz), um vetor com as\
    variaveis independentes do sistema e a precisao; levanta erros se alguma\
        das variaveis for invalida ou se a matriz, depois de lhe retirada os\
            zeros da diagonal, nao for diagonal dominante. A funcao utiliza\
                o metodo de Jacobi para criar estimativas sucessivas, enquanto\
                    a funcao verifica convergencia nao retornar True; quando\
                        isso acontece, retorna as solucoes com a precisao que se\
                            pretendia.

"""
def resolve_sistema(tuplo_matriz_quadrada,tuplo_vetor_constantes,precisao):
    if type(tuplo_matriz_quadrada)!=tuple:
        raise ValueError ('resolve_sistema: argumentos invalidos')
    for i in range(len(tuplo_matriz_quadrada)):
        if type(tuplo_matriz_quadrada[i])!=tuple:
            raise ValueError ('resolve_sistema: argumentos invalidos')
        if len(tuplo_matriz_quadrada)!=len(tuplo_matriz_quadrada[i]):
            raise ValueError ('resolve_sistema: argumentos invalidos')
        for j in range(len(tuplo_matriz_quadrada[i])):
            if not isinstance(tuplo_matriz_quadrada[i][j],(int,float)): 
                raise ValueError ('resolve_sistema: argumentos invalidos')
    if tuplo_matriz_quadrada==():
        raise ValueError ('resolve_sistema: argumentos invalidos')

    if type(tuplo_vetor_constantes)!=tuple:
        raise ValueError ('resolve_sistema: argumentos invalidos') 
    if tuplo_vetor_constantes==():
        raise ValueError ('resolve_sistema: argumentos invalidos')   
    for x in range(len(tuplo_vetor_constantes)):
        if not isinstance(tuplo_vetor_constantes[x],(int,float)):
            raise ValueError ('resolve_sistema: argumentos invalidos')
        if len(tuplo_vetor_constantes)!=len(tuplo_matriz_quadrada):
            raise ValueError ('resolve_sistema: argumentos invalidos')

    if not isinstance(precisao,float) or precisao<=0 or precisao>=1:
        raise ValueError ('resolve_sistema: argumentos invalidos')      

    tuplo_matriz_quadrada, tuplo_vetor_constantes=\
        retira_zeros_diagonal(tuplo_matriz_quadrada,tuplo_vetor_constantes)

    if not eh_diagonal_dominante(tuplo_matriz_quadrada):
        raise ValueError ('resolve_sistema: matriz nao diagonal dominante')

    tuplo_solucao_atual=(0,)*len(tuplo_vetor_constantes)

    while not verifica_convergencia(tuplo_matriz_quadrada,tuplo_vetor_constantes,\
        tuplo_solucao_atual,precisao):

        lista_sol=tuple(tuplo_solucao_atual) 
        #atualizar os valores da solucao do ciclo anterior

        for j in range(len(tuplo_matriz_quadrada)):
        
            lista_solucao_atual=list(tuplo_solucao_atual)

            lista_solucao_atual[j]=lista_solucao_atual[j]+\
                (tuplo_vetor_constantes[j]-produto_interno(lista_sol,\
                    tuplo_matriz_quadrada[j]))/tuplo_matriz_quadrada[j][j] 
                    #atualizar os elementos da lista solucao atual para as\
                    #estimativas mais exatas

            tuplo_solucao_atual=tuple(lista_solucao_atual)
       
    return tuple(lista_solucao_atual)
