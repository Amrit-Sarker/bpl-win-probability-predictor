# BPL Win Probability Predictor 🏏

This is a Machine Learning project that predicts the win probability of the chasing team in the Bangladesh Premier League (BPL). Based on historical match data, the model achieves an **82.28% accuracy** using Logistic Regression.

## Data
* Collected from **Cricsheet**.
* Includes ball by ball information from **2012** to **2025**.
  

## 📁 Project Structure
* `bpl_win_predictor.ipynb`: The full data cleaning and model training process.
* `bpl_predictor.pkl`: The trained model (the "brain").
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
**User Inputs:**
* Batting Team
* Bowling Team
* Venue
* Target, Current run, Wicket gone, Over, Ball

`predict_live('Dhaka', 'Rajshahi', 'Sylhet', 133, 98, 5, 16, 0)`

## Informal Validation:
The model’s ball-by-ball win probability outputs were informally sanity-checked during live matches by comparing them with **ESPN Cricinfo**, where the values showed close agreement in typical match situations.


##### Caution
Pathway should be checked on your computer.
