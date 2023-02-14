from Dealer import Dealer
from Player import Player


class Blackjack:

  def __init__(self):
    self.cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    self.cards_values = [11,2,3,4,5,6,7,8,9,10,10,10,10,10]
    self.isGameOver = False
    self.isGameStart = True
    self.playerValue = 0
  
  def playBlackjack(self):

    dealer = Dealer()
    player = Player()
    self.DealInitialHands(dealer, player)

    if (player.checkPlayerBJ()): #Initial game flow of both players being dealt but player has BJ
      self.isGameOver = True
      if (dealer.dealerSum() == 21):
        print("Push\n")
      else:
        while (dealer.dealerSum() < 17):
          dealer.generateCard()
          if (dealer.dealerSum() > 21 and 11 in dealer.handValues):
            replaceIndex = dealer.handValues.index(11)
            dealer.handValues[replaceIndex] = 1
      
          print("\nDealer has: ")
          dealer.printDealerHand(dealer)
          
        if (dealer.dealerSum() > 21):
          print("Dealer Busts. You win.\n")
        elif (dealer.dealerSum() == 21):
          print("Push\n")
        elif (dealer.dealerSum() < player.playerSum()):
          print("You win\n")
    else: #Initial game flow if player does not get dealt insta BJ
         while (self.playerValue != 1):
           self.playerValue = int(input("\nWould you like to hit or stand? 0 | 1\n"))
           if (self.playerValue == 0):
             player.generateCard()

             if (player.playerSum() > 21 and 11 in player.handValues): #Handle case of bust, but change ace to 1
              replaceIndex = player.handValues.index(11)
              player.handValues[replaceIndex] = 1
               
             print("\nPlayer has:")
             print(player.hand)
             print("Value: " + str(player.getHandValue()))
           if (player.playerSum() > 21): #Busts, exits loop, prompted they busted outside the loop
             break
             
         dealer.isGameOver = True

         if (player.playerSum() > 21): #Logic to handle if player busts
           print("\nYou Bust.\n")
         else:
           
           self.finishDealingDealer(dealer)
  
           if (dealer.dealerSum() > 21):
             print("Dealer Busts. You win!\n")
           else:
             if (player.playerSum() > dealer.dealerSum()):
               print("Player Wins\n")
             elif (dealer.dealerSum() > player.playerSum()):
               print("Dealer Wins\n")
             elif (dealer.dealerSum() == player.playerSum()):
              print("You push.\n")

  def DealInitialHands(self, dealer, player):
    dealer.generateCard()
    dealer.generateCard()
    
    if (dealer.hand[0] == 'A' and dealer.hand[1] == 'A'): #Handle pocket aces
      dealer.handValues[0] = 1

    if (self.isGameStart == True): #Checks to see if this code is being executed for unittest purpose or if game has started
      print("\nDealer has:")
      self.printDealerHand(dealer)
      print("\n")
  
    player.generateCard()
    player.generateCard()
    if (player.hand[0] == 'A' and player.hand[1] == 'A'): #Handle pocket aces
      player.handValues[0] = 1

    if (self.isGameStart == True): #Checks to see if this code is being executed for unittest purpose or if game has started
      print("\nPlayer has:")
      print(player.hand)
      print("Value: " + str(player.getHandValue()) + "\n")

    if (dealer.numCards == 2) and (player.numCards == 2):
      return True

  def printDealerHand(self, dealer):
    if (self.isGameOver):
      print(dealer.hand)
    else:
      print("['" + dealer.hand[0] + "', '" + "?']'")

  def finishDealingDealer(self, dealer):
    if (dealer.dealerSum() < 17):
      
      while (dealer.dealerSum() < 17):
        dealer.generateCard()
        if (dealer.dealerSum() > 21 and 11 in dealer.handValues):
          replaceIndex = dealer.handValues.index(11)
          dealer.handValues[replaceIndex] = 1
        if (self.isGameStart == True):
          print("\nDealer has: ")
          print(dealer.hand)
          print("Value: " + str(dealer.getHandValue()) + "\n")
    else:
      if (self.isGameStart == True):
        print("\nDealer has: ")
        print(dealer.hand)
        print("Value: " + str(dealer.getHandValue()) + "\n")

  
  