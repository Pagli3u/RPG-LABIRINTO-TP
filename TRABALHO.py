import random
import sys

j=1

h=7

z=j

caminhos = [1,2,3,4,5]

while (j != 6) and (j!= 9):
        
        print("Você esta na sala:", j)
        print("[1] - Caminho Vermelho\n[2] - Caminho Preto")
        print(h)
        caminho = int(input())

        if (caminho == 1):
            j=j+1
        
        elif (caminho == 2):
            h=h-1
            j=j+2
if j == 9:
    print("Você esta na sala:", j)
    print("https://www.youtube.com/watch?v=SC4xMk98Pdc")
    sys.exit()           

if j==6:
    print("Você esta na sala:", j)
    print("[2] - Caminho Preto")
    caminho = int(input())
    while (caminho != 2):
        
        if (caminho == 2):
            h=h-1
            j=j+2

        elif (caminho == 1):
            print("Você não pode ir para este lado, só existem paredes cobertas com musgo!!")
            caminho = int(input())
    j=j+2
    h=h-1
print("Você esta na sala:", j)
print("[1] - Caminho Vermelho\n[2] - Caminho Preto")
caminho = int(input())

if caminho == 1:
    h=h-1
    j=j+1

if caminho == 2:
    h=h-1
    j=j+2

if j==9:
    print("Você esta na sala:", j)
    print("https://www.youtube.com/watch?v=SC4xMk98Pdc")
    sys.exit()
    
if j==10:
    def selectRandom(caminhos):
        return random.choice(caminhos)
    j=selectRandom(caminhos)

if h!= 0:
    while (h!=0) and (j != 6):
        
        print("Você esta na sala:", j)
        print("[1] - Caminho Vermelho\n[2] - Caminho Preto")
        print(h)
        caminho = int(input())

        if (caminho == 1):
            h=h-1
            j=j+1
            
        elif (caminho == 2):
            h=h-1
            j=j+2

if j==6 and h!=0:
    print("Você esta na sala:", j)
    print("[2] - Caminho Preto")
    caminho = int(input())
    h=h-1
    j=j+2

if h==0:
    print("Seus heróis ficaram presos na sala", j,"!!")
    sys.exit()

if j==10:
    def selectRandom(caminhos):
        return random.choice(caminhos)
    j=selectRandom(caminhos)

else:
    print("Você esta na sala:", j)
    print("[1] - Caminho Vermelho\n[2] - Caminho Preto")
    caminho = int(input())

    if caminho == 1:
        h=h-1
        j=j+1

    if caminho == 2:
        h=h-1
        j=j+2

    if j==9:
        print("Você esta na sala:", j)
        print("https://www.youtube.com/watch?v=SC4xMk98Pdc")
        sys.exit()


    
