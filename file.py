# CraftFunction
import square, triangle


print("Minecraft Function Constructor V.0.0.2")
#Caio Carnelós
'''
0.0.1 - Funcionou :P
0.0.2 - Varios Blocos :)
0.0.3 - Gravando em arquivo xD

'''

Block_List = ["air","stone 1","stone 2","stone 3","stone 4"]

def func_file(L, tam):
    if (len(L) % 2 == 0):
        TamX = len(L) - 1
    else:
        TamX = len(L)
    
    if (len(L[0]) % 2 == 0):
        TamZ = len(L[0]) - 1
    else:
        TamZ = len(L[0])
        
    middle_X = int(TamX/2)
    middle_Z = int(TamZ/2)
    
    print("Middle X:" + str(middle_X) + "| Middle Z:" + str(middle_Z))
    print("Len Z:" + str(TamZ))
    print("Len X:" + str(TamX))
    
    #i = Linha
    #j = Coluna
    #ni= PosLinha
    #nj= PosColuna
    
    file = open(str(tam) + ".txt", "w")
    for ni,i in enumerate(L):
        for nj,j in enumerate(i):
           file.write("setblock ~" + str(ni-middle_X)+ " ~0 ~" + str(nj-middle_Z) + " " + Block_List[j] + "\n")
    file.close()



for i in range(3,10):
    func_file(triangle.triangle_function(i),i+1)
    
