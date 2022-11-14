from flask import Flask
from flask import request
from joblib import load
from flask import render_template,flash, request
# import numpy as np
# from numpy import asarray
# from PIL import Image

app = Flask(__name__)
model_path = "svm_gamma=0.0002_C=5.joblib"
model = load(model_path)


@app.route("/mydocker")
def hello_world():
    return '''<!-- hello --> <b> Hello, world!</b>
    <br><b> This App running on docker</b></br>'''


@app.route("/predict", methods=['POST'])
def predict_digit():
    image1 = request.json['image1']
    image2 = request.json['image2']
    print("done loading both image")
    predicted1 = model.predict([image1])
    predicted2 = model.predict([image2])

    if predicted1==predicted1:
        issame="Yes"
    else:
        issame="No"
    #return {"Image 1 was: { }".format ((int(predicted1[0]))) }
    my_result = "Image 1 digit: " + (str(predicted1[0]) + " and Image 2 digit: " +str (predicted2[0]) + " Predict image digit are same: " + str (issame))
    return {"Result":str(my_result)}


@app.route('/',methods=['GET','POST'])
def home():
    return render_template('index.html')

# IMAGE_FOLDER='static/'
# app.config['UPLOAD_FOLDER']=IMAGE_FOLDER
@app.route('/predictweb',methods=['GET','POST'])
def predict_digit_web():
    predicted1="8"
    predicted2="8"
    my_prediction = True

    return render_template('predict.html', prediction1=predicted1, prediction2=predicted2, predictResult=my_prediction)
   

if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000)