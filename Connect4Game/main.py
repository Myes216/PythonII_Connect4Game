import Connect4Game
import DanielBatyrevAI as DanielAI
import copy
import func_timeout
import ShmulyStudentAI as ShmulyAI
import YosefBirnbaumAI as YosefAI

# list of AI oppponents in Connect4 tournament
competitor_list = [ShmulyAI.NotRandomStrategy(), YosefAI.AI_strategy()]

MAX_WAIT_TIME = 1  # maximum time allowed each move
winners = list()  # tracks the winners of all games
random_choice = DanielAI.RandomStrategy()  # fallback strategy for timeouts

# simulate 1000 Connect4 games
for game_nr in range(1000):
    """
    simulates Connect4 game between two AIs
    alternates starting players and uses fallback strategy in case of timeouts
    updates winners list with outcome of each game
    """
    print(game_nr + 1)
    tie = False  # flag if game ends in tie
    game = Connect4Game.Connect4Game()  # create new Connect4 game instance

    # play until there is a winner or board is full
    while game.winner is None:
        game_safety_copy = copy.deepcopy(game)  # create safe copy of game 

        try:
            # attempt to get move from current player's strategy within time limit
            move = func_timeout.func_timeout(
                MAX_WAIT_TIME, competitor_list[game.current_player - 1].strategy, [game_safety_copy]
            )
        except func_timeout.FunctionTimedOut:
            # handle timeout by falling back to random move
            print(f'time out limit exceeded: {competitor_list[game.current_player - 1].name} performs random move')
            move = random_choice.strategy(game_safety_copy)

        game.make_move(move)  # perform selected move

        # check for tie
        if 0 == sum(map(game.is_valid_move, range(7))):  # if no valid moves left
            tie = True
            break

    # determine and record outcome
    if tie:
        winners.append("tie")
    else:
        winners.append(competitor_list[game.current_player - 1].name)

    competitor_list.reverse()  # alternate starting players for next game

# compile statistics from winners list
dictionary = {}
for item in winners:
    dictionary[item] = dictionary.get(item, 0) + 1

print(dictionary)

