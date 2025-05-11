from colorama import init, Fore, Style
init(autoreset=True)
import gameObj
import time


def gameStart():
    
    try:
        print("We will split the Decks")
        firstPlayer= input("What is the  first players name ")
        secondPlayer= input("What is the second players name ")
        deck1= gameObj.Deckofcards()
        deck1.shuffleDeck()
        player1= gameObj.playerHand()
        player2= gameObj.playerHand()
        for _ in range(26):
            player1.recieveCard(deck1.giveCard())
            player2.recieveCard(deck1.giveCard())
        
    except:
        print("There was a problem we will try again!")
    
    print("Decks have been split we will start now")
    

    time.sleep(4)
    gameCycle = True
    while gameCycle:
        
        firstDraw=player1.placeCard()
        secondDraw=player2.placeCard()
        print(f"{firstPlayer}'s draw is {str(firstDraw)}")
        print(f"{secondPlayer}'s draw is {str(secondDraw)}")
        
        if gameObj.moreValuable(firstDraw, secondDraw)==1:
            player1.recieveCard(firstDraw)
            player1.recieveCard(secondDraw)

            print(f"{firstPlayer} seizes")
            print(f'{firstPlayer} has {player1.count()} cards')
            
       
        elif gameObj.moreValuable(firstDraw, secondDraw)==2:
            player2.recieveCard(secondDraw)
            player2.recieveCard(firstDraw)

            print(f"{secondPlayer} seizes")
            print(f'{secondPlayer} has {player2.count()} cards')
            
            
        else:
            if player1.count()<5:
                print(f"{secondPlayer} player won {firstPlayer} didn't have enough for war")
                gameCycle=False
            elif player2.count()<5:
                print(f"{firstPlayer} player won. {secondPlayer} didn't have enough for war")
                gameCycle=False
            gameObj.totalWar(player1,player2, firstDraw, secondDraw)
            print(f'{firstPlayer} has {player1.count()} cards')
            print(f'{secondPlayer} has {player2.count()} cards')
            
        
        if(player1.count()==0):
            print(f"{secondPlayer} player won")
            gameCycle=False
            continue
        elif player2.count()==0:
            print(f"{firstPlayer} player won")
            gameCycle=False
            continue