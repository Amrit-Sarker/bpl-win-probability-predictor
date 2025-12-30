import pickle
import pandas as pd

model = pickle.load(open("C:/Users/LENOVO/Downloads/bpl_predictor.pkl", 'rb'))


def predict_live(batting, bowling, venue, target, score, wickets_lost, over, ball):
    balls_delivered = (over * 6) + ball
    balls_left = 120 - balls_delivered
    runs_left = target - score
    wickets_left = 10 - wickets_lost  # We calculate how many are REMAINING

    input_df = pd.DataFrame({
        'batting_team': [batting],
        'bowling_team': [bowling],
        'venue': [venue],
        'runs_left': [runs_left],
        'balls_left': [balls_left],
        'wickets_left': [wickets_left],
        'target_score': [target],
        'crr': [score / (balls_delivered/6) if balls_delivered > 0 else 0],
        'rrr': [runs_left / (balls_left/6) if balls_left > 0 else 0]
    })

    win = model.predict_proba(input_df)[0][1]

    print(f"--- BPL Match Status ---")
    print(f"{batting} needs {runs_left} runs in {balls_left} balls with {wickets_left} wickets in hand at {venue}.")
    print(f"Win Probability: {win:.1%} | Loss Probability: {1-win:.1%}")


predict_live('Dhaka', 'Comilla', 'Dhaka', 180, 120, 3, 15, 0)
