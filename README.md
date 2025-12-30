# BPL Win Probability Predictor 🏏

This is a Machine Learning project that predicts the win probability of the chasing team in the Bangladesh Premier League (BPL). Based on historical match data, the model achieves an **82.76% accuracy** using Logistic Regression.

## 📁 Project Structure
* `bpl_analysis.ipynb`: The full data cleaning and model training process.
* `bpl_model.pkl`: The trained model (the "brain").
* `predict.py`: A simple script to get live match predictions.

## 📋 Data Input Rules (City Names Only)
This model was trained using simplified city-based names. When entering data into the `predict_live` function, **do not use full franchise names**. 

| Category | Format to Use | Examples |
| :--- | :--- | :--- |
| **Teams** | **City Name Only** | `Dhaka`, `Comilla`, `Sylhet`, `Rangpur`, `Chattogram`, `Khulna`, `Rajshahi` |
| **Venues** | **City Name Only** | `Dhaka`, `Chattogram`, `Sylhet` |

*Example:* Use `'Dhaka'`, NOT `'Dhaka Dominators'`. Use `'Chattogram'`, NOT `'Zahur Ahmed Chowdhury Stadium'`.

## 🚀 How to Run
1. Install dependencies: `pip install pandas scikit-learn`
2. Open `predict.py` and update the parameters at the bottom.
3. Run: `predict.py`



## Example 
##### (batting_team, bowling_team, venue, target, current_score, wickets_lost, current_over, current_ball)
predict_live('Dhaka', 'Rajshahi', 'Sylhet', 133, 98, 5, 16, 0)



##### Caution
Pathway should be checked on your computer.
