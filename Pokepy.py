#PokePy 


#Start 

inventario_Poke ={

    "025" : {

        "nome" : "Pikachu",
        "vida" : 25,
        "lvl" : 1,
        "tipo" : "elétrico"

    }

} #inventario de pokemons
inventario_I = {} #inventario de itens

while True :

    #texto inicial 
    print("Bem vindo ao mundo PokePy, você vera criaturas fántasticas")
    print("Você quer começar agora ?")
    print("1. Sim")
    print("2. Não(sair)")

    #var temp de escolha
    vaR1 = int(input())

    if vaR1 == 2 :
        break 

    while True :

        #Loop central de escolha 
        print("O que vocẽ quer fazer agora ?")
        print("1. Explorar em busca de pokemons")
        print("2. Batalha com um treinador")

        #var temp de escolha
        vaR2 = int(input())


        if vaR2 == 2 :    
            break 
        elif  vaR2 == 1 :
            break 