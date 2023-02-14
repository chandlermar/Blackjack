import random


class Dealer():

  def __init__(self):
    self.numCards = 0
    self.hand = []
    self.cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    self.cards_values = [11,2,3,4,5,6,7,8,9,10,10,10,10,10]
    self.handValues = []
    
  def generateCard(self):
    #self.hand.append(random.randint(1,14))
    chosenCard = random.choice(self.cards) #Grabs a random card
    self.hand.append(chosenCard) #Appends chosen random card to deck

    correctIndex = self.cards.index(chosenCard) #Index of card in base arr
    self.handValues.append( int(self.cards_values[correctIndex]) )
      
    self.numCards = self.numCards + 1

    if (self.hand[0] and self.handValues[0] and self.numCards == 1): #Generate card unit testing
      return True

  def generateSpecificCard(self, cardID):
    self.hand.append(cardID)
    correctIndex = self.cards.index(cardID) #Index of card in base arr
    self.handValues.append( int(self.cards_values[correctIndex]) )
      
    self.numCards = self.numCards + 1

  def getHandValue(self):
    return ( sum(self.handValues) )


  def dealerSum(self):
    return (self.getHandValue())

  
      
  