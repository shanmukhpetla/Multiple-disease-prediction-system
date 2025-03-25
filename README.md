# Multiple Disease Prediction System

## Overview
This is a **Streamlit-based web application** that predicts the likelihood of **heart disease** and **diabetes** using machine learning models. The system takes user inputs for various health parameters and provides predictions based on trained models.

## Features
- 🏥 **Heart Disease Prediction** using key health indicators.
- 🍬 **Diabetes Prediction** based on glucose levels, BMI, and other metrics.
- 📊 **User-Friendly Interface** with an interactive sidebar.
- 🔍 **Machine Learning Models** trained on medical datasets.
- 🚀 **Fast Predictions** using pre-trained models.

## Tech Stack
- **Python** 🐍
- **Streamlit** 🎨 (For UI)
- **scikit-learn** 🤖 (For ML Models)
- **Pickle** (For model storage)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/multiple-disease-prediction.git
   cd multiple-disease-prediction
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run multiple_disease_prediction.py
   ```

## File Structure
```
|-- multiple_disease_prediction.py   # Main Streamlit application
|-- Saved Models/
|   |-- heart_disease_model.sav      # Trained heart disease model
|   |-- diabetes_model.sav           # Trained diabetes model
|-- requirements.txt                 # Required dependencies
|-- README.md                        # Project documentation
```

## Usage
- Open the application in your browser.
- Select **Heart Disease Prediction** or **Diabetes Prediction** from the sidebar.
- Enter the required health parameters.
- Click the prediction button to get results.

## Notes
- Ensure that `heart_disease_model.sav` and `diabetes_model.sav` are in the **Saved Models** folder.
- Use numeric inputs to avoid errors.

## Deployment
You can deploy this app using **Streamlit Cloud, Heroku, or AWS**.

## Contributing
Feel free to fork this repository and submit pull requests!

## License
This project is open-source under the **MIT License**.

