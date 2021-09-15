import random
import sys

sala=1

jogadas=0

caminhos = [1,2,3,4,5]

while (sala != 6) and (sala!= 9) and (sala!=10):
        
        print("Você esta na sala:", sala)
        print("[1] - Caminho Vermelho\n[2] - Caminho Preto")
        caminho = int(input())

        if (caminho == 1):
            jogadas=jogadas+1
            sala=sala+1
        
        elif (caminho == 2):
            jogadas=jogadas+1
            sala=sala+2

if sala == 9:
    print("Você esta na sala:", sala)
    print("https://youtu.be/SC4xMk98Pdc?t=35")
    sys.exit()           

if sala==6:
    print("Você esta na sala:", sala)
    print("[2] - Caminho Preto")
    caminho = int(input())
    while (caminho != 2):
        
        if (caminho == 2):
            jogadas=jogadas+1
            sala=sala+2

        elif (caminho == 1):
            print("Você não pode ir para este lado, só existem paredes cobertas com musgo!!")
            caminho = int(input())
    sala=sala+2
    jogadas=jogadas+1

if sala==10:
    def selectRandom(caminhos):
        return random.choice(caminhos)
    sala=selectRandom(caminhos)
    print("Seus heróis foram teleportados para a sala", sala)

if jogadas>=7:
    print("Seus heróis ficaram presos na sala", sala,"!!")
    sys.exit()
    
print("Você esta na sala:", sala)
print("[1] - Caminho Vermelho\n[2] - Caminho Preto")
caminho = int(input())

if caminho == 1:
    jogadas=jogadas+1
    sala=sala+1

if caminho == 2:
    jogadas=jogadas+1
    sala=sala+2

if sala==9:
    print("Você esta na sala:", sala)
    print("https://youtu.be/SC4xMk98Pdc?t=35")
    sys.exit()
    
if sala==10:
    def selectRandom(caminhos):
        return random.choice(caminhos)
    sala=selectRandom(caminhos)
    print("Seus heróis foram teleportados para a sala", sala)

if jogadas>=7:
    while (jogadas>=7) and (sala != 6) and (sala != 9) and (sala != 10):
        
        print("Você esta na sala:", sala)
        print("[1] - Caminho Vermelho\n[2] - Caminho Preto")
        caminho = int(input())

        if (caminho == 1):
            jogadas=jogadas+1
            sala=sala+1
            
        elif (caminho == 2):
            jogadas=jogadas+1
            sala=sala+2

if sala==10:
    def selectRandom(caminhos):
        return random.choice(caminhos)
    sala=selectRandom(caminhos)
    print("Seus heróis foram teleportados para a sala", sala)
    
if sala==6 and jogadas>=7:
    print("Você esta na sala:", sala)
    print("[2] - Caminho Preto")
    caminho = int(input())
    jogadas=jogadas+1
    sala=sala+2

if sala==10:
    def selectRandom(caminhos):
        return random.choice(caminhos)
    sala=selectRandom(caminhos)
    print("Seus heróis foram teleportados para a sala", sala)

if sala==9:
    print("Você esta na sala:", sala)
    print("https://youtu.be/SC4xMk98Pdc?t=35")
    sys.exit()

if jogadas>=7:
    print("Seus heróis ficaram presos na sala", sala,"!!")
    sys.exit()

else:
    print("Você esta na sala:", sala)
    print("[1] - Caminho Vermelho\n[2] - Caminho Preto")
    caminho = int(input())

    if caminho == 1:
        jogadas=jogadas+1
        sala=sala+1

    if caminho == 2:
        jogadas=jogadas+1
        sala=sala+2

    if sala==9:
        print("Você esta na sala:", sala)
        print("https://youtu.be/SC4xMk98Pdc?t=35")
        sys.exit()
