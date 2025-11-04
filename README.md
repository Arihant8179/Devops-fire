# Forest Fire Prediction System

## Introduction
Forest fires are one of the most devastating natural disasters, causing widespread damage to ecosystems, biodiversity, and the environment. This project aims to predict forest fire probability using machine learning techniques based on environmental factors such as temperature, humidity, and oxygen levels.



## Features
- Predicts the likelihood of forest fires using logistic regression.
- User-friendly web interface built with Flask.
- Accepts real-time input parameters like temperature, oxygen levels, and humidity.
- Displays prediction results dynamically.

## Technologies Used
- **Python**: For backend logic and machine learning model implementation.
- **Flask**: For building the web application.
- **HTML/CSS/JavaScript**: For creating a responsive user interface.
- **scikit-learn**: For logistic regression modeling.
- **NumPy & Pandas**: For data manipulation and preprocessing.

## Installation
### Prerequisites
Ensure you have Python 3.9 or higher installed on your system.

### Steps
Clone the repository:

```bash
git clone https://github.com/Ritinikhil/ForestFire.git
cd ForestFire
```

Install required dependencies:

```bash
pip install -r requirements.txt
```

Run the Flask application:

```bash
python app.py
```

Access the web application at:

```
http://127.0.0.1:5000
```

## Usage
1. Enter environmental parameters such as temperature (°C), oxygen level (ppm), and humidity (%).
2. Click on "Predict Probability" to get the likelihood of a forest fire.
3. View results dynamically displayed on the web interface.

## Project Structure
```
ForestFire/
├── app.py               # Main Flask application
├── forest_fire.py       # Machine learning logic
├── model.pkl            # Pre-trained logistic regression model
├── requirements.txt     # Python dependencies
├── templates/
│   └── forest_fire.html # HTML template for web interface
├── tests/
│   ├── __init__.py      # Test package initialization
│   └── test_app.py      # Unit tests for Flask app
```

## Dataset
The dataset used for training includes environmental variables such as temperature, humidity, and oxygen levels, along with binary labels indicating whether a forest fire occurred.

## Testing
Unit tests are included in the `tests/` directory. To run tests:

```bash
python -m unittest discover -s tests -p "test*.py"
```

## Future Enhancements
- Improve model accuracy by incorporating additional environmental factors.
- Explore advanced machine learning algorithms like Random Forest or Neural Networks.
- Deploy the application using Docker for scalability and ease of use.

## Contributors
- **Ritinikhil**
- **KCABHCAX**
