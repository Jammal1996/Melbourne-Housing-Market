HOW TO RUN THE MELBOURNE HOUSE PRICE PREDICTION WEB APP
==================================================

This guide explains how to run the Melbourne House Price Prediction web
application locally on your machine.

--------------------------------------------------
1. PREREQUISITES
--------------------------------------------------

Make sure the following are installed:

- Python 3.11 (recommended)
- pip (comes with Python)
- A terminal / command prompt

Check your Python version:
python --version


--------------------------------------------------
2. PROJECT STRUCTURE
--------------------------------------------------

Ensure your project directory looks like this:

melb/
│
├── app.py
├── suburbs.py
├── melb_price_model.pkl
├── requirements.txt
│
└── templates/
    └── index.html


--------------------------------------------------
3. CREATE A VIRTUAL ENVIRONMENT
--------------------------------------------------

From the project root directory:

python -m venv melb


Activate the virtual environment:

Windows:
melb\Scripts\activate

macOS / Linux:
source melb/bin/activate


--------------------------------------------------
4. INSTALL DEPENDENCIES
--------------------------------------------------

Install all required packages:

pip install -r requirements.txt


--------------------------------------------------
5. RUN THE APPLICATION
--------------------------------------------------

Start the Flask web server:

python app.py

If successful, you will see:
Running on http://127.0.0.1:5000


--------------------------------------------------
6. OPEN THE APPLICATION
--------------------------------------------------

Open a web browser and go to:

http://127.0.0.1:5000


--------------------------------------------------
7. USING THE APPLICATION
--------------------------------------------------

1. Select a suburb from the dropdown list
2. Enter property details (rooms, land size, etc.)
3. Click "Predict Price"
4. View the estimated price in Australian Dollars (AUD)


--------------------------------------------------
8. STOPPING THE APPLICATION
--------------------------------------------------

To stop the server, press:

CTRL + C


--------------------------------------------------
NOTES
--------------------------------------------------

- The application runs locally and does not require internet access
- Predictions are estimates and not financial advice
- Ensure Python and scikit-learn versions match the training environment


==================================================
