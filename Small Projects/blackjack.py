"""In this problem we'll be working with a simplified version of blackjack (aka twenty-one). In this version there is one player (who you'll control) and a dealer. Play proceeds as follows:

The player is dealt two face-up cards. The dealer is dealt one face-up card.
The player may ask to be dealt another card ('hit') as many times as they wish. If the sum of their cards exceeds 21, they lose the round immediately.
The dealer then deals additional cards to himself until either:
the sum of the dealer's cards exceeds 21, in which case the player wins the round
the sum of the dealer's cards is greater than or equal to 17. If the player's total is greater than the dealer's, the player wins. Otherwise, the dealer wins (even in case of a tie).
When calculating the sum of cards, Jack, Queen, and King count for 10. Aces can count as 1 or 11 (when referring to a player's "total" above, we mean the largest total that can be made without exceeding 21. So e.g. A+8 = 19, A+8+8 = 17)

For this problem, you'll write a function representing the player's decision-making strategy in this game. We've provided a very unintelligent implementation below:
    """
# Return True if the player should hit (request another card) given the current game state, 
# or False if the player should stay.

def should_hit(dealer_total, player_total, player_low_aces, player_high_aces):
    # When player total is 17 or higher, should not ask another card
    if player_total >= 17:
        return False
    
    # When player total is 11 or less, ask one more card
    if player_total <= 11:
        return True
    
    if dealer_total>=7:
        return player_total<17
    
    if dealer_total<7:
        return player_total<13
    
    



