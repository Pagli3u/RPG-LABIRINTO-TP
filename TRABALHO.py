print("Você esta na sala: 1")
print("[1] - Caminho Vermelho\n[2] - Caminho Preto")
j=1
i=0
h=7
z=j
while (j != 6) and (h!=0):
    print(h)
    caminho = int(input())
    if (caminho == 1):
        h=h-1
        j=j+1
        print("Você esta na sala:", j)
        print("[1] - Caminho Vermelho\n[2] - Caminho Preto")
        
        
    elif (caminho == 2):
        h=h-1
        j=j+2
        print("Você esta na sala:", j)
        print("[1] - Caminho Vermelho\n[2] - Caminho Preto")
            
if j==6:
    caminho = int(input())
    print("[2] - Caminho Preto")
    h=h-1
    j=j+2
else:
    while (j<=9):
        caminho = int(input())
        if (caminho == 1):
            h=h-1
            j=j+1
            print("Você esta na sala:", j+1)
            print("[1] - Caminho Vermelho\n[2] - Caminho Preto")
        
            
        elif (caminho == 2):
            h=h-1
            j=j+2
            print("Você esta na sala:", j+2)
            print("[1] - Caminho Vermelho\n[2] - Caminho Preto")

