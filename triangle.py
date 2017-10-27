print("Minecraft Function Constructor - triangle function V.0.0.1 \n")
#Caio Carnelos

#Dado um numero X que varia a partir de 4. Construa uma funcao que ira gerar um triangulo com as bordas com 1 e o miolo com 0.

def function_pair(size):
    largura = size
    ListFinal = []
    meioinicio = int(largura / 2) - 1
    meiofim = int(largura / 2)
    #Borda Superior
    lista = []
    for i in range(largura):
        if((i == int(largura/2)) or (i == meioinicio)):
            lista.append(1)
        else:
            lista.append(0)
    ListFinal.append(lista)

    #Borda Meio
    for i in range(int(size/2) - 2):
        lista = []
        meioinicio = meioinicio - 1
        meiofim = meiofim + 1   
        for i in range(largura):
            if((i == meioinicio) or (i == meiofim)):
                lista.append(1)
            else:
                lista.append(0)    
        ListFinal.append(lista)
    
    #Borda Inferior
    lista = []
    for i in range(largura):
        lista.append(1)
    ListFinal.append(lista)
    return ListFinal

def function_odd(size):
    largura = size
    ListFinal = []
    meioinicio = int(largura / 2)
    meiofim = int(largura / 2)
    #Borda Superior
    lista = []
    for i in range(largura):
        if(i == int(largura/2)):
            lista.append(1)
        else:
            lista.append(0)
    ListFinal.append(lista)
    
    #Borda Meio
    for i in range(int(size/2) - 1):
        lista = []
        meioinicio = meioinicio - 1
        meiofim = meiofim + 1   
        for i in range(largura):
            if((i == meioinicio) or (i == meiofim)):
                lista.append(1)
            else:
                lista.append(0)    
        ListFinal.append(lista)
    
    #Borda Inferior
    lista = []
    for i in range(largura):
        lista.append(1)
    ListFinal.append(lista)
    return ListFinal

def triangle_function(size):
    if(size % 2 == 0):
        return function_pair(size)
    else:
        return function_odd(size)
