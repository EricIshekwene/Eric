from random import shuffle




class Deckofcards():

    def __init__(self):
        self.deck = [
    ('2', 'Hearts'), ('3', 'Hearts'), ('4', 'Hearts'), ('5', 'Hearts'), ('6', 'Hearts'),
    ('7', 'Hearts'), ('8', 'Hearts'), ('9', 'Hearts'), ('10', 'Hearts'), ('J', 'Hearts'),
    ('Q', 'Hearts'), ('K', 'Hearts'), ('A', 'Hearts'),
    
    ('2', 'Diamonds'), ('3', 'Diamonds'), ('4', 'Diamonds'), ('5', 'Diamonds'), ('6', 'Diamonds'),
    ('7', 'Diamonds'), ('8', 'Diamonds'), ('9', 'Diamonds'), ('10', 'Diamonds'), ('J', 'Diamonds'),
    ('Q', 'Diamonds'), ('K', 'Diamonds'), ('A', 'Diamonds'),
    
    ('2', 'Clubs'), ('3', 'Clubs'), ('4', 'Clubs'), ('5', 'Clubs'), ('6', 'Clubs'),
    ('7', 'Clubs'), ('8', 'Clubs'), ('9', 'Clubs'), ('10', 'Clubs'), ('J', 'Clubs'),
    ('Q', 'Clubs'), ('K', 'Clubs'), ('A', 'Clubs'),
    
    ('2', 'Spades'), ('3', 'Spades'), ('4', 'Spades'), ('5', 'Spades'), ('6', 'Spades'),
    ('7', 'Spades'), ('8', 'Spades'), ('9', 'Spades'), ('10', 'Spades'), ('J', 'Spades'),
    ('Q', 'Spades'), ('K', 'Spades'), ('A', 'Spades')]
        
    def shuffleDeck(self, times=1):
        for i in range(times):
            shuffle(self.deck)

    def giveCard(self):
        return self.deck.pop()
    


class playerHand():

    def __init__(self):
        self.hand=[]
    
    def recieveCard(self,card):
        self.hand.append(card)
        
    def placeCard(self):
        return self.hand.pop(0)
    
    def count(self):
        return len(self.hand)
    


class table():
    def __init__(self, p1,p2):
        self.p1=p1
        self.p2=p2
        
        self.p2TableCards=[]
        self.p1TableCards=[]

    def draw4(self):
        
        for _ in range(4):
            self.p1TableCards.append(self.p1.placeCard())
            self.p2TableCards.append(self.p2.placeCard())
        
    
    def chooseAndDistr(self, choice1, choice2):
        print(f"The cards for player one are: X,X,X {self.p1TableCards[choice1-1]}")
        print(f"The cards for player two are: X,X,X {self.p2TableCards[choice2-1]}")
        
        val=moreValuable(self.p1TableCards[choice1-1],self.p2TableCards[choice2-1] )
        allCards= self.p1TableCards+self.p2TableCards
        if (val==1):
            for cards in allCards:
                self.p1.recieveCard(cards)
        elif val==2:
            for cards in allCards:
                self.p2.recieveCard(cards)
        else:
            pass



         


def moreValuable(card1, card2):
    cardValue={'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13,'A':14}
    card1Val= cardValue[card1[0]]
    card2Val=cardValue[card2[0]]
    if (card1Val>card2Val):
        return 1
    elif (card2Val>card1Val):
        return 2
    else:
        return 0


def totalWar(hand1, hand2, tiecard1, tiecard2):
    warPile = [tiecard1, tiecard2]
    
    while True:
        if hand1.count() < 4:
            print("Player 1 doesn’t have enough cards for war.")
            return
        if hand2.count() < 4:
            print("Player 2 doesn’t have enough cards for war.")
            return
        
        faceDown1 = [hand1.placeCard() for _ in range(3)]
        faceDown2 = [hand2.placeCard() for _ in range(3)]
        
        faceUp1 = hand1.placeCard()
        faceUp2 = hand2.placeCard()
        
        print(f"The war cards are: Player 1: {faceUp1} | Player 2: {faceUp2}")
        
        warPile.extend(faceDown1 + faceDown2 + [faceUp1, faceUp2])

        result = moreValuable(faceUp1, faceUp2)
        
        if result == 1:
            for card in warPile:
                hand1.recieveCard(card)
            print("Player 1 wins the war.")
            return
        elif result == 2:
            for card in warPile:
                hand2.recieveCard(card)
            print("Player 2 wins the war.")
            return
        else:
            print("Another tie! The war continues...")
            continue