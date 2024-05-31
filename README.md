# Crime Analysis and Prediction

This project focuses on analyzing and predicting crime rates using data from 2021 to 2022. By leveraging various machine learning algorithms and data visualization techniques, it aims to provide insights and future trends in crime patterns.

## Features
**Data Analysis**: Utilizes historical crime data to uncover patterns and trends.
**Prediction Models**: Implements machine learning algorithms such as Linear Regression, Time Series Forecasting, Logistic Regression, SVM, Decision Tree, and Random Forest to predict future crime rates.
**Visualization**: Provides interactive visualizations to help understand the data and model predictions.
**Web Application**: Built using Python, Flask, HTML, and a bit of JavaScript to create an interactive web interface for users to explore the data and predictions.

## Technologies Used

- **Python**: For data processing, analysis, and machine learning model implementation.
- **Flask**: To develop the web application and handle server-side logic.
- **HTML & JavaScript**: For the front-end interface and interactive visualizations.
- **Machine Learning Libraries**: Scikit-learn, Pandas, NumPy, Matplotlib for implementing and visualizing machine learning models.

## Machine Learning Algorithms

- **Linear Regression**: For predicting crime trends based on historical data.
- **Time Series Forecasting**: To analyze and forecast future crime rates.
- **Logistic Regression**: For classification tasks within the dataset.
- **Support Vector Machine (SVM)**: To identify patterns and classify data points.
- **Decision Tree**: For classification and regression tasks, providing interpretability.
- **Random Forest**: An ensemble method for improving prediction accuracy and robustness.

## How to Run

1. Clone the repository.
2. Install the required Python packages using `pip install -r requirements.txt`.
3. Run the Flask application with `python app.py`.
4. Open your web browser and navigate to `http://127.0.0.1:5000/` to access the web interface.

## Dataset

The dataset includes crime records from various states in India for the years 2021 and 2022. It contains details such as the number of crimes committed in different categories like murder, theft, sexual harassment, etc.

## Project Structure

- `app.py`: The main Flask application file.
- `templates/`: Contains HTML templates for rendering web pages.
- `static/`: Contains static files like CSS, JavaScript, and images.
- `models/`: Machine learning models and scripts for training and prediction.
- `data/`: The dataset used for analysis and prediction.

## Acknowledgments

Special thanks to Usha Mittal Institute of Technology for their support and resources.

Feel free to explore the code, raise issues, and contribute to the project!
