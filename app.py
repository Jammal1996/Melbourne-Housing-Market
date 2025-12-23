from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import joblib
import os
from suburbs import SUBURBS   # list of 314 suburbs

app = Flask(__name__)

MODEL_PATH = "melb_price_model.pkl"

# ---------- Load model ----------
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError("Model file not found")

model = joblib.load(MODEL_PATH)
print("✅ Model loaded successfully")


# ---------- Route ----------
@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    error = None

    if request.method == "POST":
        try:
            suburb = request.form["suburb"]

            rooms = float(request.form["rooms"])
            distance = float(request.form["distance"])
            landsize = float(request.form["landsize"])
            building_area = float(request.form["building_area"])
            year_built = float(request.form["year_built"])

            # Full feature set — MUST match training columns exactly
            input_data = {
                "Suburb": suburb,
                "Rooms": rooms,
                "Distance": distance,
                "Landsize": landsize,
                "BuildingArea": building_area,
                "YearBuilt": year_built,

                # numerical (imputed)
                "Bedroom2": np.nan,
                "Bathroom": np.nan,
                "Car": np.nan,
                "Propertycount": np.nan,
                "Postcode": np.nan,

                # ⚠️ spelling must match training
                "Lattitude": np.nan,
                "Longtitude": np.nan,

                # sale date features
                "SaleYear": np.nan,
                "SaleMonth": np.nan,

                # categorical (imputed / encoded)
                "Type": np.nan,
                "Method": np.nan,
                "SellerG": np.nan,
                "CouncilArea": np.nan,
                "Regionname": np.nan,
            }

            X = pd.DataFrame([input_data])
            prediction = float(model.predict(X)[0])

        except Exception as e:
            error = str(e)

    return render_template(
        "index.html",
        suburbs=SUBURBS,
        prediction=prediction,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)
