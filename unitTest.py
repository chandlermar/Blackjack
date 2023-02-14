import unittest
from Blackjack import Blackjack
from Dealer import Dealer
from Player import Player


class testCases(unittest.TestCase):

  def test_deal(self):
    blackjack  = Blackjack()
    dealer = Dealer()
    player = Player()

    blackjack.isGameStart = False
    dealCorrectly = blackjack.DealInitialHands(dealer, player)

    assert (dealCorrectly == 1)

  #Tests that when a card is generated for the player, that the type of card is documented in their hand, the value is documented in a corresponding value array, and the card count is incremented
  def test_player_generate_card(self):
    player = Player()

    cardGenerated = player.generateCard()
    assert (cardGenerated == 1)
  #Same as above, but for the dealer
  def test_dealer_generate_card(self):
    dealer = Dealer()

    cardGenerated = dealer.generateCard()
    assert (cardGenerated == 1)

  #Tests to see if the sum of card's value in the hand is the correct sum for the player
  def test_player_hand_sum(self):
    player = Player()

    player.generateCard()
    player.generateCard()

    assert (player.getHandValue() == sum(player.handValues))

  #Same as above, but for the dealer
  def test_dealer_hand_sum(self):
    dealer = Dealer()

    dealer.generateCard()
    dealer.generateCard()

    assert (dealer.getHandValue() == sum(dealer.handValues))

  #Tests generating a specific card. In this case, an Ace is generated and the card is checked to ensure it was added to the players hand, the number of cards was increased by one, and the ace was counted with a value of 11
  def test_specific_card_gen(self):
    player = Player()

    player.generateSpecificCard('A')

    assert (player.hand[0] == 'A' and player.numCards == 1 and player.handValues[0] == 11)

  #Tests that when generating two cards that equal a blackjack, that the checkPlayerBJ function returns True
  def test_blackjack(self):
    player = Player()

    player.generateSpecificCard('A')
    player.generateSpecificCard('K')

    assert (player.checkPlayerBJ() == True)

#Tests that in the case that the dealer has less than a value of 17, he gets new cards until his value is >=17
  def test_finish_dealing_dealer(self):
    dealer = Dealer()
    blackjack  = Blackjack()
    blackjack.isGameStart = False
    dealer.generateSpecificCard('2')
    blackjack.finishDealingDealer(dealer)

    assert (dealer.getHandValue() >= 17)

