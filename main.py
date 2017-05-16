from NewDeck import Deck
from NewCard import Card 

pile=Deck()
pile.Shuffle()
player1card=pile.TakeFromTop()
player2card=pile.TakeFromTop()
player1card.displayCard()
player2card.displayCard()
if(player1card.rank > player2card.rank):
    print("PLAYER 1 WINS!!!")
if(player2card.rank > player1card.rank):
	print("PLAYER 2 WINS!!!")
if(player1card.rank == player2card.rank):
	print("A TIE!")
	print("ITS TIME TO THROW DOWN!")
	player1card1=pile.TakeFromTop()
	player1card2=pile.TakeFromTop()
	player1card3=pile.TakeFromTop()
	player1card3.displayCard()
	player2card1=pile.TakeFromTop()
	player2card2=pile.TakeFromTop()
	player2card3=pile.TakeFromTop()
	player2card3.displayCard()
	if(player1card3.rank > player2card3.rank):
		print("PLAYER 1 WINS!!!")
	if(player2card3.rank > player1card3.rank):
		print("PLAYER 2 WINS!!!")
		
	

		




	
	
    
