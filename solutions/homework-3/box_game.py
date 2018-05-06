import random

def play_game(num_ppl, num_tries, strategy, num_runs = 1) :
    """ A tool to simulate many random rounds of the box game.
    Parameters
    ----------
    num_ppl : int, required
        Number of contestants.
    num_tries : int, required
        Number of tries each contestant has to find their box.
    strategy : function(boxes, num_tries, person), required
        A strategy function to be used for each contestant.
    num_runs : int, optional
        Number of times to play the game. Defaults to 1.

    Returns
    ----------
        rate of victory with given strategy function
    """
    boxes = list(range(num_ppl))
    ppl = list(range(num_ppl))
    wins = 0
    games_played = 0
    while games_played < num_runs :
        # Shuffle the boxes once per game
        random.shuffle(boxes)
        result = True
        for person in ppl :
            result = strategy(boxes, num_tries, person)
            if result is False : # we have lost !!!
                break # stops the inner for loop
        # remember that int(True) = 1, and int(False) = 0
        wins += result
        games_played += 1       
    # we have played all the games
    return wins/num_runs

def individual_strategy(boxes, num_tries, num_to_find) :
    """ Implements the cycle strategy for a player to
    look for their number (num_to_find) in a list (boxes_list) with
    a limited number of tries (num_tries). The function
    returns True if the number is found, False otherwise.
    The algorithm treats boxes[i] as a permtuation and
    looks through the cycle containing i = person. """
    count = 0
    idx = num_to_find
    while count < num_tries :
        curr = boxes[idx]
        if curr == num_to_find :
            return True
        idx = curr
        count += 1
    return False
