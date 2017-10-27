print("Minecraft Function Constructor - square function V.0.0.1 \n")
#Caio Carnelos

def square_function(size):
    largura = size
    ListFinal = []
    #Borda Superior
    lista = []
    for i in range(largura):
        lista.append(1)
    ListFinal.append(lista)
    
    #Borda Lateral
    for i in range(size-2):
        lista = []
        for i in range(largura):
            if((i == 0) or (i == largura - 1)):
                lista.append(1)
            else:
                lista.append(0)
        ListFinal.append(lista)
    
    #Borda Inferior
    lista = []
    for i in range(largura):
        lista.append(1)
    ListFinal.append(lista)
    
    return(ListFinal)
    
print(square_function(2))
