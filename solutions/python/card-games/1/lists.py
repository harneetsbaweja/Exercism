"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    Parameters:
        number (int): The current round number.

    Returns:
        list: The current round number and the two that follow.
    """
    rounds = []
    for item in range(3):
        rounds.append(number+item)
    return rounds


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    Parameters:
        rounds_1 (list): The first rounds played.
        rounds_2 (list): The second group of rounds played.

    Returns:
        list:  All rounds played.
    """
    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    Parameters:
        rounds (list): The rounds played.
        number (int): The round number.

    Returns:
        bool: Was the round played?
    """
    return number in rounds


def card_average(hand):
    """Calculate and returns the average card value from the list.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        float: The average value of the cards in the hand.
    """
    return sum(hand)/len(hand)


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.
    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Does one of the approximate averages equal the `true average`?
    """
    true_avg = card_average(hand)
    min_max_avg = (min(hand)+max(hand))/2
    ordered_hand = sorted(hand)
    median_idx = int(len(ordered_hand)/2)
    print(median_idx)
    median = ordered_hand[median_idx]
    return min_max_avg == true_avg or median == true_avg


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Are the even and odd averages equal?
    """
# Act - The function body
    even_hand = hand[0::2]
    odd_hand = hand[1::2]
    mean_even = card_average(even_hand)
    mean_odd = card_average(odd_hand)
    return mean_even == mean_odd


# %%
if __name__ == "__main__":
    # Arrange - test data setup (cell-specific, delete before function)
    hand = [1, 3, 4, 5, 6, 7, 8]
# Act - See above
# Assert
    print(average_even_is_average_odd(hand))#
    
# %%
def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        list: The hand with Jacks (if present) value doubled.
    """
    if hand[-1] == 11:
        hand[-1] = hand[-1]*2

    return hand

# %%
if __name__ == "__main__":
    # Arrange - test variables
    # hand = [1, 2, 3, 6, 11]
    hand = [1, 2, 4, 12]
# Act - See Above
    if hand[-1] == 11:
        hand[-1] = hand[-1]*2
# Assert - outputs
# %%
