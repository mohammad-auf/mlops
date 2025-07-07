from flask import Flask ,request ,render_template
import pandas as pd
import numpy as np 
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData ,PredictedPipeline



application = Flask(__name__)
app = application

#Route for home page

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/predicted",methods=['GET','POST'])
def predicted_data():
    if  request.method =="GET":
        return render_template("home.html")
    else:
        data = CustomData(
            gender= request.form.get("gender"),
            race= request.form.get("ethnicity"),
            parental_level_education=request.form.get("parental_level_of_education"),
            lunch_type= request.form.get("lunch"),
            test_preparation =request.form.get("test_preparation_course"),
            reading_score=request.form.get("reading_score"),
            writing_score=request.form.get("writing_score"),
            
        )

        input_df = data.get_data_as_data_frame()
        print(input_df)
        print("Before Prediction")
        prediction = PredictedPipeline()
        print("Mid Prediction")
        try:
            results = prediction.predicted(input_df)
            print("after Prediction")
            print(results[0])
            return render_template("home.html", results=results[0])
        except Exception as e:
            print(f"Prediction error: {e}")
            return render_template("home.html", results="Error occurred during prediction")
    


if __name__ == '__main__':
    app.run(host="0.0.0.0")



