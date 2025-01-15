#MINESWEEPER
#2.1.1. - TAD gerador
def cria_gerador(b,s):
    if not (type(b)==int and (b==32 or b==64)):
        raise ValueError ('cria_gerador: argumentos invalidos')
    if type(s)!=int or s<=0 or s>=2**b:
        raise ValueError ('cria_gerador: argumentos invalidos')
    g={'b':b,'s':s}
    return g
"""
int x int -> gerador (dicionario)
A funçao recebe um inteiro (numero de bits do gerador) e um inteiro positivo
(seed) e devolve o gerador; levanta erros se os valores nao forem compativeis
com os de um gerador valido.
"""

def cria_copia_gerador(g):
    copia_gerador = {}
    for b,s in g.items(): 
        copia_gerador[b]=s
    return copia_gerador
"""
gerador -> gerador
Esta funçao recebe um gerador e devolve uma copia desse gerador.
"""

def obtem_estado(g):
    return g['s']
"""
gerador -> int
Esta funçao devolve o estado atual do gerador (nao o altera).
"""

def define_estado(g,s):
    g['s']=s
    return g['s']
"""
gerador x int -> int
Esta funçao define um valor para o estado do gerador como o valor s
e devolve esse valor.
"""

def atualiza_estado(g):
    if g['b']==32: 
        g['s']^=(g['s']<<13) & 0xFFFFFFFF
        g['s']^=(g['s']>>17) & 0xFFFFFFFF
        g['s']^=(g['s']<<5) & 0xFFFFFFFF
    elif g['b']==64:
        g['s']^=(g['s']<<13) & 0xFFFFFFFFFFFFFFFF
        g['s']^=(g['s']>>7) & 0xFFFFFFFFFFFFFFFF
        g['s']^=(g['s']<<17) & 0xFFFFFFFFFFFFFFFF
    return g['s']
"""
gerador -> int
ESta funçao atualiza o estado do gerador com o algoritmo xorshift 
(geraçao de numeros pseudoaleatorios) e devolve-o.
"""

def eh_gerador(arg):
    return type(arg)==dict and len(arg)==2 and 'b' in arg and 's' in arg and\
            type(arg['b'])==int and type(arg['s'])==int and arg['s']>0 and\
                (arg['b']==32 or arg['b']==64)
"""
universal -> booleano
Esta funçao devolve True se o argumento for um gerador ou False em contrario.
"""

def geradores_iguais(g1,g2):
    return eh_gerador(g1) and eh_gerador(g2) and g1['b']==g2['b'] and g1['s']==g2['s']
"""
gerador x gerador -> booleano
Esta funçao devolve True se os geradores passados como argumentos sao iguais e
False, caso nao sejam.
"""

def gerador_para_str(g):
    return 'xorshift{}(s={})'.format(g['b'],g['s'])
"""
gerador -> str
Esta funçao devolve a string que representa o gerador do argumento.
"""

def gera_numero_aleatorio(g,n):
    #resto da divisão inteira do estado atualizado pelo argumento inteiro + 1
    return atualiza_estado(g)%n+1
"""
gerador x int -> int
Esta funçao atualiza o estado do gerador e devolve um numero
pseudoaleatorio entre 1 e n (inclusive).
"""

def gera_carater_aleatorio(g,c):
    #comprimento da cadeia de caracteres de A a c
    l=ord(c)-ord('A')+1
    value_carater=atualiza_estado(g)%l+1
    #caracter correspondente ao resto da divisão inteira do estado atualizado por l
    return chr(ord('A')+value_carater-1)
"""
gerador x str -> str
Esta funçao atualiza o estado do gerador e devolve um carater
pseudoaleatorio entre A e o argumento c.
"""

#2.1.2. - TAD coordenada
def cria_coordenada(col,lin):
    if type(col)!=str or len(col)!=1 or not 65<=ord(col)<=90:
        raise ValueError ('cria_coordenada: argumentos invalidos')
    if type(lin)!=int or not 1<=lin<=99:
        raise ValueError ('cria_coordenada: argumentos invalidos')
    c={'col':col,'lin':lin}
    return c
"""
str x int -> coordenada (dicionario)
Esta funçao recebe os valores para a coluna e a linha e devolve a coordenada
correspondente; levanta erros se os valores nao forem compativeis
com os de uma coordenada valida.
"""

def obtem_coluna(c):
    return c['col']
"""
coordenada -> str
Esta funçao retorna a coluna da coordenada c passada como argumento.
"""

def obtem_linha(c):
    return c['lin']
"""
coordenada -> int
Esta funçao retorna a linha da coordenada c passada como argumento.
"""

def eh_coordenada(arg):
    return type(arg)==dict and len(arg)==2 and 'col' in arg and 'lin' in arg\
        and type(arg['col'])==str and len(arg['col'])==1 and\
            65<=ord(arg['col'])<=90 and type(arg['lin'])==int\
                and 1<=arg['lin']<=99
"""
universal -> booleano
Esta funçao retorna True se o argumento for uma coordenada e False se nao for.
"""

def coordenadas_iguais(c1,c2):
    return eh_coordenada(c1) and eh_coordenada(c2) and c1['col']==c2['col'] and c1['lin']==c2['lin']
"""
coordenada x coordenada -> booleano
Esta funçao devolve True se as coordenadas passadas como argumentos forem iguais e
False caso nao sejam.
"""

def coordenada_para_str(c):
    return '{}{}'.format(c['col'],str(c['lin']) if c['lin']>=10 else '0'+str(c['lin']))
"""
coordenada -> str
Esta funçao devolve a string que representa a coordenada do seu argumento.
"""

def str_para_coordenada(s):
    coordenada={}
    coordenada['col']=s[0]
    coordenada['lin']=int(s[1]+s[2])
    return coordenada
"""
str -> coordenada
Esta funçao devolve a coordenada representada pelo argumento.
"""

def obtem_coordenadas_vizinhas(c):

    resultado=()
    coluna_coordenada=obtem_coluna(c)
    linha_coordenada=obtem_linha(c)
    #obter os valores das linhas anteriores e seguintes
    linha_anterior=linha_coordenada-1
    linha_seguinte=linha_coordenada+1
    #obter os caracteres das colunas anteriores e seguintes
    coluna_anterior=chr(ord(obtem_coluna(c))-1)
    coluna_seguinte=chr(ord(obtem_coluna(c))+1)

    #para cada if:
    #verificar se a coordenada seria valida
    #adicionar a coordenada a um tuplo resultado

    if 'A'<=coluna_anterior<='Z' and 1<=linha_anterior<=99:                                    
        resultado+=(cria_coordenada(coluna_anterior,linha_anterior),)

    if 'A'<=coluna_coordenada<='Z' and 1<=linha_anterior<=99:
        resultado+=(cria_coordenada(coluna_coordenada,linha_anterior),)

    if 'A'<=coluna_seguinte<='Z' and 1<=linha_anterior<=99:
        resultado+=(cria_coordenada(coluna_seguinte,linha_anterior),)

    if 'A'<=coluna_seguinte<='Z' and 1<=linha_coordenada<=99:
        resultado+=(cria_coordenada(coluna_seguinte,linha_coordenada),)

    if 'A'<=coluna_seguinte<='Z' and 1<=linha_seguinte<=99:
        resultado+=(cria_coordenada(coluna_seguinte,linha_seguinte),)

    if 'A'<=coluna_coordenada<='Z' and 1<=linha_seguinte<=99:
        resultado+=(cria_coordenada(coluna_coordenada,linha_seguinte),)

    if 'A'<=coluna_anterior<='Z' and 1<=linha_seguinte<=99:
        resultado+=(cria_coordenada(coluna_anterior,linha_seguinte),)

    if 'A'<=coluna_anterior<='Z' and 1<=linha_coordenada<=99:
        resultado+=(cria_coordenada(coluna_anterior,linha_coordenada),)

    return resultado
"""
coordenada -> tuplo
Esta funçao devolve um tuplo com as coordenadas vizinhas da coordenada c,
pela ordem do enuciado.
"""

def obtem_coordenada_aleatoria(c,g):
    #gera uma coordenada com os valores obtidos pelas funçoes de alto nivel
    #do TAD gerador 
    return cria_coordenada(gera_carater_aleatorio(g,obtem_coluna(c)),gera_numero_aleatorio(g,obtem_linha(c)))
"""
coordenada x gerador -> coordenada
Esta funçao devolve uma coordenada gerada aleatoriamente como descrito
anteriormente em que c representa a coordenada "máxima".
"""

#2.1.3. - TAD parcela
def cria_parcela():
    return ['tapada','sem_mina']
"""
{} -> parcela (lista)
Esta funçao devolve uma parcela tapada sem mina.
"""

def cria_copia_parcela(p):
    copia_parcela=[i for i in p]
    return copia_parcela
"""
parcela -> parcela
Esta funçao recebe uma parcela e devolve uma copia dessa parcela.
"""

def limpa_parcela(p):
    p[0]='limpa'
    return p
"""
parcela -> parcela
Esta funçao modifica destrutivamente a parcela, troca o estado para limpa, 
e devolve a parcela.
"""

def marca_parcela(p):
    p[0]='marcada'
    return p
"""
parcela -> parcela
Esta funçao modifica destrutivamente a parcela, troca o estado para marcada, 
e devolve a parcela.
"""

def desmarca_parcela(p):
    p[0]='tapada'
    return p
"""
parcela -> parcela
Esta funçao modifica destrutivamente a parcela, troca o estado para tapada, 
e devolve a parcela.
"""

def esconde_mina(p):
    p[1]='com_mina'
    return p
"""
parcela -> parcela
Esta funçao modifica destrutivamente a parcela, esconde uma mina, 
e devolve a parcela.
"""

def eh_parcela(arg):
    return type(arg)==list and len(arg)==2 and type(arg[0])==str and\
         type(arg[1])==str and (arg[0]=='tapada' or arg[0]=='limpa' or\
             arg[0]=='marcada') and (arg[1]=='sem_mina' or arg[1]=='com_mina')
"""
universal -> booleano
Esta funçao retorna True se o argumento for uma parcela e False se nao for.
"""

def eh_parcela_tapada(p):
    return p[0]=='tapada'
"""
parcela -> booleano
Esta funçao devolve True se a parcela for tapada e False caso contrario.
"""

def eh_parcela_marcada(p):
    return p[0]=='marcada'
"""
parcela -> booleano
Esta funçao devolve True se a parcela for marcada e False caso contrario.
"""

def eh_parcela_limpa(p):
    return p[0]=='limpa'
"""
parcela -> booleano
Esta funçao devolve True se a parcela for limpa e False caso contrario.
"""

def eh_parcela_minada(p):
    return p[1]=='com_mina'
"""
parcela -> booleano
Esta funçao devolve True se a parcela esconder uma mina e False caso contrario.
"""

def parcelas_iguais(p1,p2):
    return eh_parcela(p1) and eh_parcela(p2) and p1[0]==p2[0] and p1[1]==p2[1]
"""
parcela x parcela -> booleano
Esta funçao devolve True se as parcelas passadas como argumentos forem iguais e
False caso nao sejam.
"""

def parcela_para_str(p):
    if p[0]=='tapada':
        return '#'
    if p[0]=='marcada':
        return '@'
    if p[0]=='limpa' and p[1]=='sem_mina':
        return '?'
    if p[0]=='limpa' and p[1]=='com_mina':
        return 'X'
"""
parcela -> str
Esta funçao devolve a string que representa a o estado da parecla:
# para tapadas, @ para marcadas, ? para limpas sem mina e X para limpas com mina.
"""

def alterna_bandeira(p):
    #desmarcar ou nao a parcela mediante o seu estado
    if eh_parcela_marcada(p):
        desmarca_parcela(p)
        return True
    elif eh_parcela_tapada(p):
        marca_parcela(p)
        return True
    else:
        return False
"""
parcela -> booleano
Esta funçao recebe uma parcela e modifica-a destrutivamente: 
desmarca se estiver marcada e marca se estiver tapada e devolve True,
caso contrario mantem a parcela e devolve False.
"""

#2.1.4. - TAD campo
def cria_campo(c,l):
    if type(c)!=str or len(c)!=1 or type(l)!=int or not 65<=ord(c)<=90 or not 1<=l<=99:
        raise ValueError ('cria_campo: argumentos invalidos')
    campo=[]
    for j in range(l):
        linha=[]
        for i in range(ord(c)-ord('A')+1):
            linha+=[cria_parcela()]
        campo+=[linha]
    return campo
"""
str x int -> campo (lista)
Esta funçao devolve o campo do tamanho pretendido (c e a ultima coluna,
l e a ultima linha) formado so por parcelas tapadas sem minas.
"""

def cria_copia_campo(m):
    copia_campo=[]
    for linha in m:
        copia_linha=[]
        for parcela in linha:
            copia_parcela=cria_copia_parcela(parcela)
            copia_linha+=[copia_parcela]
        copia_campo+=[copia_linha]
    return copia_campo
"""
campo -> campo
Esta funçao recebe um campo e devolve uma copia desse campo.
"""

def obtem_ultima_coluna(m):
    return chr(ord('A')+len(m[0])-1)
"""
campo -> str
Esta funçao devolve a string que corresponde a ultima coluna 
do campo de minas.
"""

def obtem_ultima_linha(m):
    return len(m)
"""
campo -> int
Esta funçao devolve o inteiro correspondente a ultima linha
do campo de minas.
"""

def obtem_parcela(m,c):
    return m[obtem_linha(c)-1][ord(obtem_coluna(c))-ord('A')]
"""
campo x coordenada -> parcela
Esta funçao devolve a parcela do campo que se encontra
na posiçao da coordenada c.
"""

def obtem_coordenadas(m,s):

    tuplo_coordenadas=()

    #para cada if:
    #selecionar parcelas com o valor de s
    #criar coordenadas e adiciona-las a um tuplo para retornar

    if s=='limpas':
        for i in range(len(m)):
            for j in range(len(m[i])):
                if eh_parcela_limpa(m[i][j]):
                    tuplo_coordenadas+=(cria_coordenada(chr(65+j),i+1),)

    elif s=='marcadas':
        for i in range(len(m)):
            for j in range(len(m[i])):
                if eh_parcela_marcada(m[i][j]):
                    tuplo_coordenadas+=(cria_coordenada(chr(65+j),i+1),)

    elif s=='tapadas':
        for i in range(len(m)):
            for j in range(len(m[i])):
                if eh_parcela_tapada(m[i][j]):
                    tuplo_coordenadas+=(cria_coordenada(chr(65+j),i+1),)

    elif s=='minadas':
        for i in range(len(m)):
            for j in range(len(m[i])):
                if eh_parcela_minada(m[i][j]):
                    tuplo_coordenadas+=(cria_coordenada(chr(65+j),i+1),)

    return tuplo_coordenadas
"""
campo x str -> tuplo
Esta funçao devolve o tuplo formado pelas coordenadas ordenadas de acordo
com o enuciado dependendo do estado das parcelas.
"""

def obtem_numero_minas_vizinhas(m,c):
    numero_minas_vizinhas=0
    for coordenada in obtem_coordenadas_vizinhas(c):
        #iterar sobre o tuplo retornado pela funçao anterior
        if eh_coordenada_do_campo(m,coordenada) and eh_parcela_minada(obtem_parcela(m,coordenada)):
            #se a coordenada pertencer ao campo e a parcela for minada
            numero_minas_vizinhas+=1
    return numero_minas_vizinhas
"""
campo x coordenada -> int
Esta funçao devolve o numero de minas nas parcelas vizinhas da coordenada c.
"""

def eh_campo(arg):

    if type(arg)==list and len(arg)!=0:
        verificacoes_linhas,verificacoes_elementos=[],[]
        comprimento_lista_1=len(arg[0])

        for linha in arg:
            verificacoes_linhas+=[type(linha)==list]
            verificacoes_linhas+=[len(linha)==comprimento_lista_1]
            #verificar se todas linhas tem o mesmo comprimento
            for elemento in linha: 
                verificacoes_elementos+=[eh_parcela(elemento)]
                #verificar se as parcelas sao validas

        verificacoes_totais=[type(arg)==list]+verificacoes_linhas+verificacoes_elementos

    return type(arg)==list and len(arg)!=0 and all(verificacoes_totais)
"""
universal -> booleano
Esta funçao devolve True se o argumento for um campo e False se nao for.
"""

def eh_coordenada_do_campo(m,c):
    return eh_coordenada(c) and obtem_linha(c)<=obtem_ultima_linha(m) and obtem_coluna(c)<=obtem_ultima_coluna(m)
"""
campo x coordenada -> booleano
Esta funçao devolve True se c e uma coordenada valida e pertence ao campo.
"""

def campos_iguais(m1,m2):
    lista_verificaçao=[]
    if obtem_ultima_coluna(m1)==obtem_ultima_coluna(m2) and obtem_ultima_linha(m1)==obtem_ultima_linha(m2):
        #verificar a igualdade das dimensoes do campo
        for i in range(len(m1)):
            for j in range(len(m1[i])): #iterar sobre os elementos do campo
                lista_verificaçao+=[parcelas_iguais(m1[i][j],m2[i][j])]
                #verificar se cada parcela e igual dos dois campos
    return obtem_ultima_coluna(m1)==obtem_ultima_coluna(m2) and obtem_ultima_linha(m1)==obtem_ultima_linha(m2) and all(lista_verificaçao)
"""
campo x campo -> booleano
Esta funçao devolve True se os argumentos forem campos iguais, se não,
devolve False.
"""

def campo_para_str(m):

    sequencia_letras,sequencia_campo,sequencia_linha='','',''

    for x in range(ord('A'),ord(obtem_ultima_coluna(m))+1):
        sequencia_letras+=str(chr(x)) #criar a sequencia inicial de letras
        
    sequencia_sinais='+'+'-'*len(sequencia_letras)+'+'

    for j in range(len(m)):
        for x in range(len(m[j])):
            if eh_parcela_limpa(m[j][x]) and not eh_parcela_minada(m[j][x]):
                #para parcelas limpas sem mina
                coord=cria_coordenada(chr(65+x),j+1)

                if eh_coordenada_do_campo(m,coord) and obtem_numero_minas_vizinhas(m,coord)==0:
                    #sem minas vizinhas
                    sequencia_linha+=' '
                elif eh_coordenada_do_campo(m,coord):
                    #com minas vizinhas
                    sequencia_linha+=str(obtem_numero_minas_vizinhas(m,coord))

            else:
                #para parcelas nao limpas ou minadas
                sequencia_linha+=parcela_para_str(m[j][x])
        #para os numeros no inicio da linha do layout do campo
        if j<9:
            numero_linha='0'+str(j+1)
        else:
            numero_linha=str(j+1)

        sequencia_campo+=numero_linha+'|'+sequencia_linha+'|'+'\n'
        #adicionar cada linha ao layout final
        sequencia_linha=''
        #dar 'reset' a linha

    return '   '+sequencia_letras+'\n  '+sequencia_sinais+'\n'+sequencia_campo+'  '+sequencia_sinais
"""
campo -> str
Esta funçao devolve uma representaçao em string do campo de minas.
"""

def coloca_minas(m,c,g,n):

    if eh_coordenada_do_campo(m,c):
        coordenada_maxima_campo=cria_coordenada(obtem_ultima_coluna(m),obtem_ultima_linha(m))
        #obter o limite do campo para obter coordenadas para minas
        coordenadas_minas=[]

        while n>0:
            coordenada_aleatoria=obtem_coordenada_aleatoria(coordenada_maxima_campo,g)

            if coordenada_aleatoria not in coordenadas_minas and not coordenadas_iguais(coordenada_aleatoria,c)\
                and coordenada_aleatoria not in obtem_coordenadas_vizinhas(c):
                #se a coordenada gerada nao estiver na vizinhanca da coordenada
                #inicial nem tiver sido gerada previamente
                coordenadas_minas.append(coordenada_aleatoria)
                n-=1

        for coordenada in coordenadas_minas:
            #esconder minas em todas as parcelas obtidas
            esconde_mina(obtem_parcela(m,coordenada))

        return m
"""
campo x coordenada x gerador x int -> campo
Esta funçao modifica destrutivamente o campo e esconde um numero n de minas em
parcelas do campo cujas coordenadas sao geradas com o gerador passado como
argumento; as coordenadas nao coincidem com a coordenada c nem com parcelas
vizinhas nem com outras minas anteriores.
"""

def limpa_campo(m,c):
    if (eh_coordenada_do_campo(m,c) and eh_parcela_minada(obtem_parcela(m,c))) or\
        (eh_coordenada_do_campo(m,c) and not eh_parcela_minada(obtem_parcela(m,c)) and obtem_numero_minas_vizinhas(m,c)!=0):
        #se a parcela for minada ou nao minada mas com minas na vinhanca
        limpa_parcela(obtem_parcela(m,c))
        return m
    elif eh_coordenada_do_campo(m,c) and not eh_parcela_minada(obtem_parcela(m,c)) and obtem_numero_minas_vizinhas(m,c)==0:
        #parcela nao minada sem minas vizinhas
        limpa_parcela(obtem_parcela(m,c))
        for coordenada in obtem_coordenadas_vizinhas(c):
                if eh_coordenada_do_campo(m,coordenada) and not eh_parcela_minada(obtem_parcela(m,coordenada))\
                    and eh_parcela_tapada(obtem_parcela(m,coordenada)):
                    #parcela nao minada e tapada
                    limpa_parcela(obtem_parcela(m,coordenada))
                    limpa_campo(m,coordenada) #limpar iterativamente o campo
        return m 
"""
campo x coordenada -> campo
Esta funçao modifica destrutivamente o campo, limpa a parcela na coordenada c 
e o devolve-a; caso nao haja minas nas parcelas vizinhas, limpa as parcelas 
vizinhas tapadas.
"""

#2.2.1.
def jogo_ganho(m):

    lista,lista_vf=[],[]
    lista_todas_coordenadas=list(obtem_coordenadas(m,'tapadas'))+list(obtem_coordenadas(m,'marcadas'))+\
        list(obtem_coordenadas(m,'limpas'))
    #obter uma lista com as coordenadas do campo
    lista_coordenadas_minadas=list(obtem_coordenadas(m,'minadas'))

    for coordenada in lista_todas_coordenadas:
        if coordenada not in lista_coordenadas_minadas:
            lista+=[coordenada] #lista com parcelas nao minadas

    for coordenada in lista:
        lista_vf+=[eh_parcela_limpa(obtem_parcela(m,coordenada))]
        #verificar se sao ou nao limpas

    return all(lista_vf)
"""
campo -> booleano
Esta funçao recebe um campo de minas e devolve True se as parcelas sem minas
estiverem limpas e False caso contrario.
"""

#2.2.2.
def pede_coordenada(m):
    string_coordenada=input('Escolha uma coordenada:')
    if len(string_coordenada)!=3:
        return pede_coordenada(m)
    else:
        if 'A'<=string_coordenada[0]<='Z' and string_coordenada[1:].isdigit():
            #se a string for uma coordenada valida
            if eh_coordenada(str_para_coordenada(string_coordenada)) and\
                eh_coordenada_do_campo(m,str_para_coordenada(string_coordenada)):
                #se a string corresponder a uma coordenada do campo
                return string_coordenada
            else:
                return pede_coordenada(m)
        else:
            return pede_coordenada(m)
"""
campo -> coordenada
Esta funçao (recursiva) auxiliar para a turno_jogador e minas pede um input
de uma coodenada ate que seja fornecida uma coordenada valida pertencente 
ao campo passado como argumento e retorna essa coordenada valida.
"""

def turno_jogador(m):
    acao=input('Escolha uma ação, [L]impar ou [M]arcar:')
    while not (acao=='L' or acao=='M'):
        acao=input('Escolha uma ação, [L]impar ou [M]arcar:')

    string_coordenada=pede_coordenada(m)
   
    if acao=='M':
        alterna_bandeira(obtem_parcela(m,str_para_coordenada(string_coordenada)))
        #trocar de marcada para nao marcada ou vice_versa
    elif acao=='L':
        #limpar parcela ou campo se for ou nao minada, respetivamente
        if not eh_parcela_minada(obtem_parcela(m,str_para_coordenada(string_coordenada))):
            limpa_campo(m,str_para_coordenada(string_coordenada))
        else:
            limpa_parcela(obtem_parcela(m,str_para_coordenada(string_coordenada)))
            return False
    return True
"""
campo -> booleano
Esta funçao  recebe um campo de minas e pede ao jogador para uma acao e uma
coordenada, caso os inputs sejam invalidos, repete o pedido ate que sejam
introduzidos valores validos. A funcao modifica destrutivamente o campo, de
acordo com acao e devolve False caso o jogador tenha limpo uma parcela minada,
ou True caso contrario.
"""

#2.2.3.
def minas(c,l,n,d,s):
    try:
        gerador=cria_gerador(d,s)
    except ValueError:
        raise ValueError ('minas: argumentos invalidos')
    if not eh_gerador(gerador):
        raise ValueError ('minas: argumentos invalidos')
    try:
        campo=cria_campo(c,l)
    except ValueError:
        raise ValueError ('minas: argumentos invalidos')
    if not eh_campo(campo):
        raise ValueError ('minas: argumentos invalidos')
    if type(n)!=int or not 1<=n<=(ord(c)-ord('A')+1)*l-9:
        raise ValueError ('minas: argumentos invalidos')
    if (ord(c)-ord('A')+1)*l<=9:
        raise ValueError ('minas: argumentos invalidos')

    def minas_aux(campo,n):
        #printar o layout do jogo quando for chamada
        numero_bandeiras=len(obtem_coordenadas(campo,'marcadas'))
        string_info_bandeiras='   '+'[Bandeiras {}/{}]'.format(numero_bandeiras,n)
        print(string_info_bandeiras)
        print(campo_para_str(campo))
    """
    campo x int -> str (prints)
    Esta funçao recebe um campo e um numero de minas e devolve o esquema do jogo.
    """

    minas_aux(campo,n)

    string_coordenada_inicial=pede_coordenada(campo)
    coloca_minas(campo,str_para_coordenada(string_coordenada_inicial),gerador,n)
    limpa_campo(campo,str_para_coordenada(string_coordenada_inicial))

    minas_aux(campo,n)

    while not jogo_ganho(campo):
        #repetir a turno_jogador enquanto o jogo nao terminar
        resultado_jogada=turno_jogador(campo)
        if not resultado_jogada:
            #caso de derrota
            minas_aux(campo,n)
            print('BOOOOOOOM!!!')
            return False
        
        minas_aux(campo,n)

    if jogo_ganho(campo):
        #caso de vitoria
        print('VITORIA!!!')
        return True
"""
str x int x int x int x int -> booleano
Esta funçao permite jogar efetivamente Minesweeper. A funçao recebe argumentos
que permitem gerar um campo(c,l) e um gerador(d,s) e um numero de minas.
A funçao chama repetidamente a turno_jogador até ao fim do jogo e devolve True
caso se ganhe o jogo ou False caso contrario.
"""
