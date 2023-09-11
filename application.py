from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os 
import tensorflow as tf
import cv2
import numpy as np
from pytesseract import pytesseract, Output
import keras_ocr


UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/', methods = ["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template('index.html')
    else: 
        # print(request.form)
        # print(request.files)
        if 'file' not in request.files:
            # print('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            # print('No selected file')
            return {"message": "No FIle"}
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # print(os.path)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            newmodel = tf.keras.models.load_model('imageClassificationModel 2.h5')
            testImages = []
            read = cv2.imread(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # print(read.shape)
            testImages.append(cv2.resize(read, (300,300)))
            # print(testImages)
            testImages = np.asarray(testImages)
            testImages = testImages / 255.0

            predictions = newmodel.predict(testImages)
            
            # print(predictions)
            # predicted_label = np.argmax(predictions_array)
            answer = np.argmax(predictions)
            if answer == 0:
                answer1 = "Router"
            elif answer ==1:
                answer1 = "AP"
            elif answer == 2:
                answer1 = "Switch" 

            text = pytesseract.image_to_string(read)
            pipeline = keras_ocr.pipeline.Pipeline()




# Get a set of three example images
            images = [read]

# Each list of predictions in prediction_groups is a list of
# (word, box) tuples.
            prediction_groups = pipeline.recognize(images)
            print(prediction_groups)
            for item in prediction_groups:
                newtext = item[0][0]
                print(item[0][0])
# Displaying the extracted text
            # print(text[:-1]  )
            # text1 = text[:-1]
         ##   return redirect(url_for("index",prediction = answer1))
            return {"message": "success", "prediction": answer1, "readtext":newtext}



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS




if __name__ == '__main__':
    ## app.debug = True
    app.run()



