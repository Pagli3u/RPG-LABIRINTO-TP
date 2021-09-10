print("Você esta na sala: 1")
print("[1] - Caminho Vermelho\n[2] - Caminho Preto")
j=1
i=0
h=7

while (j < 9) and (h!=0):
    
    print(h)
    caminho = int(input())
    if (caminho == 1):
        h=h-1
        print("Você esta na sala:", j+1)
        print("[1] - Caminho Vermelho\n[2] - Caminho Preto")
        
        j=j+1
    elif (caminho == 2):
        h=h-1
        print("Você esta na sala:", j+2)
        print("[1] - Caminho Vermelho\n[2] - Caminho Preto")
        j=j+2
