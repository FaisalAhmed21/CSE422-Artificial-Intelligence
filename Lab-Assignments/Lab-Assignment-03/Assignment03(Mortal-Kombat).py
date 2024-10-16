# -*- coding: utf-8 -*-
"""Part_1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GfoZ-SIPLurg_-8J6ngKOeqCfzcFRg9D
"""

result_tree = []
p_tracker = 0
while p_tracker < 32:
    result_tree.append(-1 if p_tracker % 2 != 0 else 1)
    p_tracker += 1

def decide_best_move(tree_position, current_leaf_, alpha_limit, beta_limit, is_max_turn):
    if current_leaf_ == 0:
        return result_tree[tree_position]
    if is_max_turn:
        highest_outcome = float('-inf')
        move_count = 0
        while move_count < 2:
            evaluated_outcome = decide_best_move(tree_position * 2 + move_count, current_leaf_ - 1, alpha_limit, beta_limit, False)
            highest_outcome = max(highest_outcome, evaluated_outcome)
            alpha_limit = max(alpha_limit, highest_outcome)
            if beta_limit <= alpha_limit:
                break
            move_count += 1
        return highest_outcome
    else:
        lowest_outcome = float('inf')
        move_count = 0
        while move_count < 2:
            evaluated_outcome = decide_best_move(tree_position * 2 + move_count, current_leaf_ - 1, alpha_limit, beta_limit, True)
            lowest_outcome = min(lowest_outcome, evaluated_outcome)
            beta_limit = min(beta_limit, lowest_outcome)
            if beta_limit <= alpha_limit:
                break
            move_count += 1
        return lowest_outcome


def battle_simulation(starting_turn):
    active_player = starting_turn
    rounds_completed = 0
    round_results = []
    scorpion_outcome = 0
    subzero_outcome = 0

    for current_round in range(3):
        round_outcome = decide_best_move(0, 5, float('-inf'), float('inf'), active_player == 1)
        if round_outcome == 1:
            subzero_outcome += 1
            round_results.append('Sub-Zero')
        else:
            scorpion_outcome += 1
            round_results.append('Scorpion')

        active_player = 1 - active_player
        rounds_completed += 1


    final_winner = 'Sub-Zero' if subzero_outcome > scorpion_outcome else 'Scorpion'
    return round_results, final_winner, rounds_completed

first_turn = int(input("Select the first fighter: Enter 0 for Scorpion or 1 for Sub-Zero: "))
round_history, match_winner, total_rounds_played = battle_simulation(first_turn)


output_message = f"""Match Winner: {match_winner}
Total Rounds Fought: {total_rounds_played}
"""

round_counter = 1
for victor in round_history:
    output_message += f"Winner of Round {round_counter}: {victor}\n"
    round_counter += 1

print(output_message)
