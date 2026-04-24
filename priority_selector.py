def priority_selector(current_score, previous_score, time_since_last_action):
    """
    This function determines the priority of actions based on score increases,
    implementing a 30-second firing window to increase aggressiveness.
    """  
    firing_window = 30  # 30 seconds

    if time_since_last_action < firing_window:
        # Consider prioritizing score increases
        if current_score > previous_score:
            # Calculate potential score gain
            score_gain = current_score - previous_score
            return f'Increase score by {score_gain} points.'
        else:
            return 'No score increase detected.'
    else:
        return 'Wait for firing window to reset.'

# Refine target scoring to maximize point gains while minimizing wasted shots

def optimize_target_scoring(target_scores, max_wasted_shots):
    optimized_scores = []
    for score in target_scores:
        if score < max_wasted_shots:
            optimized_scores.append(score)
    return optimized_scores

# Example usages:
# score = priority_selector(current_score, previous_score, time_since_last_action)
# optimized_targets = optimize_target_scoring([10, 20, 30, 25], 25)