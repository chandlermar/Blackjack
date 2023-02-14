#Please make the terminal full screen to see my amazing ascii art title!
#Chandler Martin - CS333 - Blackjack
#This program allows the user to play blackjack against the dealer. After each game, the player is prompted to play again or exit.


from Blackjack import Blackjack
from unitTest import testCases
import os




def main():

    test_case = testCases()
    test_case.test_deal()
    test_case.test_player_generate_card()
    test_case.test_player_hand_sum()
    test_case.test_specific_card_gen()
    test_case.test_blackjack()
    test_case.test_finish_dealing_dealer()
    
    userInput = ""
  
  
    while userInput != 'EXIT':
      print(r"""
      
      
.------..------..------..------..------..------..------..------..------.        .------..------..------..------..------..------.
|C.--. ||H.--. ||A.--. ||N.--. ||D.--. ||L.--. ||E.--. ||R.--. ||S.--. | .-.    |C.--. ||A.--. ||S.--. ||I.--. ||N.--. ||O.--. |
| :/\: || :/\: || (\/) || :(): || :/\: || :/\: || (\/) || :(): || :/\: |((5))   | :/\: || (\/) || :/\: || (\/) || :(): || :/\: |
| :\/: || (__) || :\/: || ()() || (__) || (__) || :\/: || ()() || :\/: | '-.-.  | :\/: || :\/: || :\/: || :\/: || ()() || :\/: |
| '--'C|| '--'H|| '--'A|| '--'N|| '--'D|| '--'L|| '--'E|| '--'R|| '--'S|  ((1)) | '--'C|| '--'A|| '--'S|| '--'I|| '--'N|| '--'O|
`------'`------'`------'`------'`------'`------'`------'`------'`------'   '-'  `------'`------'`------'`------'`------'`------'
      
      
      
      """)
      print("Game of the night: Blackjack.\n")
      blackjack = Blackjack()
      blackjack.playBlackjack()
      userInput = input("\nPlay Again? YES | EXIT\n")
      if (userInput == "YES"):
        os.system('clear')
    
if __name__ == "__main__":
    main()

