# -*- coding: utf-8 -*-

#Import necessary libraries
from flask import Flask, render_template, request
import pickle
import numpy as np
import os
import sklearn
 
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import load_model
 
#load model
tmodel =load_model("model/tomato_pred.h5")
cmodel =load_model("model/corn_pred.h5")
pmodel =load_model("model/pt_disease.h5")
gmodel =load_model("model/Gp_disease.h5")


#pesticide prediction





print('@@ Model loaded')
 
 
def pred_tom(tomato,fer):
  test_image = load_img(tomato, target_size = (150, 150)) # load image 
  print("@@ Got Image for prediction")
   
  test_image = img_to_array(test_image)/255 # convert image to np array and normalize
  test_image = np.expand_dims(test_image, axis = 0) # change dimention 3D to 4D
   
  result = tmodel.predict(test_image).round(3) # predict diseased palnt or not
  print('@@ Raw result = ', result)
   
  pred = np.argmax(result) # get the index of max value
  
  
  
  
  filename="model/RandomForest.pkl"
  loadm=pickle.load(open(filename,'rb'))
  data = np.array([[fer[0],fer[1],fer[2],fer[3],fer[4],fer[5],fer[6]]])
  prediction = loadm.predict(data)
  print(prediction[0])
  res=prediction[0]
 
    
 
    
  if pred == 0:
    return "Tomato___Bacterial_spot", 'tBacterial_spot.html',res # if index 0 burned leaf
  elif pred == 1:
      return 'Tomato___Early_blight', 'tEarly_blight.html',res # # if index 1
  elif pred == 2:
      return 'Tomato___Late_blight', 'tLate_blight.html',res  # if index 2  fresh leaf
  else:
    return "Tomato___healthy", 'Tomato___healthy.html',res # if index 3
 
    
 
def pred_corn(corn,fer):
  test_image = load_img(corn, target_size = (150, 150)) # load image 
  print("@@ Got Image for prediction")
   
  test_image = img_to_array(test_image)/255 # convert image to np array and normalize
  test_image = np.expand_dims(test_image, axis = 0) # change dimention 3D to 4D
   
  result = cmodel.predict(test_image).round(3) # predict diseased palnt or not
  print('@@ Raw result = ', result)
   
  pred = np.argmax(result) # get the index of max value
  
  
  
  
  filename="model/RandomForest.pkl"
  loadm=pickle.load(open(filename,'rb'))
  data = np.array([[fer[0],fer[1],fer[2],fer[3],fer[4],fer[5],fer[6]]])
  prediction = loadm.predict(data)
  print(prediction[0])
  res=prediction[0]
 
  if pred == 0:
    return "Corn_Blight", 'Corn_Blight.html',res # if index 0 burned leaf
  elif pred == 1:
      return 'Corn_Common_Rust', 'Corn_Common_Rust.html',res # # if index 1
  elif pred == 2:
      return 'Corn_Gray_Leaf_Spot', 'Corn_Gray_Leaf_Spot.html',res  # if index 2  fresh leaf
  else:
    return "Corn_Healthy", 'Corn_Healthy.html',res  # if index 3  
 
    
 
    
 
    
 
  
def pred_pot(potato,fer):
  test_image = load_img(potato, target_size = (150, 150)) # load image 
  print("@@ Got Image for prediction")
   
  test_image = img_to_array(test_image)/255 # convert image to np array and normalize
  test_image = np.expand_dims(test_image, axis = 0) # change dimention 3D to 4D
   
  result = pmodel.predict(test_image).round(3) # predict diseased palnt or not
  print('@@ Raw result = ', result)
   
  pred = np.argmax(result) # get the index of max value
  
  
  
  
  filename="model/RandomForest.pkl"
  loadm=pickle.load(open(filename,'rb'))
  data = np.array([[fer[0],fer[1],fer[2],fer[3],fer[4],fer[5],fer[6]]])
  prediction = loadm.predict(data)
  print(prediction[0])
  res=prediction[0]
     
 
    
  if pred == 0:
    return "Potato___Early_blight", 'Potato___Early_blight.html',res # if index 0 burned leaf
  elif pred == 1:
      return "Potato___Late_blight", 'Potato___Late_blight.html',res # # if index 1
  else:
    return  'Potato___healthy', 'Potato___healthy.html',res # if index 3  
 
    
  
def pred_grapes(grapes,fer):
  test_image = load_img(grapes, target_size = (150, 150)) # load image 
  print("@@ Got Image for prediction")
   
  test_image = img_to_array(test_image)/255 # convert image to np array and normalize
  test_image = np.expand_dims(test_image, axis = 0) # change dimention 3D to 4D
   
  result = gmodel.predict(test_image).round(3) # predict diseased palnt or not
  print('@@ Raw result = ', result)
   
  pred = np.argmax(result) # get the index of max value
  
  
  
  
  filename="model/RandomForest.pkl"
  loadm=pickle.load(open(filename,'rb'))
  data = np.array([[fer[0],fer[1],fer[2],fer[3],fer[4],fer[5],fer[6]]])
  prediction = loadm.predict(data)
  print(prediction[0])
  res=prediction[0]
     
 
    
  if pred == 0:
    return "Grape___Black_rot", 'Grape___Black_rot.html',res # if index 0 burned leaf
  elif pred == 1:
      return 'Grape___Esca', 'Grape___Esca.html',res # # if index 1
  elif pred == 2:
      return "Grape___Leaf_blight", 'Grape___Leaf_blight.html',res  # if index 2  fresh leaf
  else:
    return 'Grape___healthy', 'Grape___healthy.html',res # if index 3   
    
 
    
 
    
 
    
 
 #------------>>pred_cot_dieas<<--end
     
 
# Create flask instance
app = Flask(__name__)
 



# render index.html page
@app.route("/", methods=['GET', 'POST'])
def home():
        return render_template('index.html')


@app.route("/tomato", methods=['GET', 'POST'])
def tomato():
        return render_template('tomato.html')
    
    
@app.route("/corn", methods=['GET', 'POST'])
def corn():
        return render_template('corn.html')
    
        
@app.route("/potato", methods=['GET', 'POST'])
def potato():
        return render_template('potato.html')
 
    
@app.route("/grapes", methods=['GET', 'POST'])
def grapes():
        return render_template('grapes.html')    
  
       
  
# get input image from client then predict class and render respective .html page for solution
@app.route("/tpredict", methods = ['GET','POST'])
def predict():
     if request.method == 'POST':
        file = request.files['image'] # fet input
        filename = file.filename        
        print("@@ Input posted = ", filename)
        
        pest1=[]
        
        nitro = request.form.get("nitro")
        n=float(nitro)
        pest1.append(n)
        
        
        phos = request.form.get("phos")
        p=float(phos)
        pest1.append(p)
        
        
        pot = request.form.get("pot")
        k=float(pot)
        pest1.append(k)
        
        temp = request.form.get("temp")
        t=float(temp)
        pest1.append(t)
        
        
        mos = request.form.get("mos")
        m=float(mos)
        pest1.append(m)
        
        ph = request.form.get("ph")
        p1=float(ph)
        pest1.append(p1)
        
        
        rain = request.form.get("rain")
        r=float(rain)
        pest1.append(r)
        
        
        print("@@ nitro = ", nitro)
        n=float(nitro)
        print(type(n))
        file_path = os.path.join('static/user uploaded', filename)
        file.save(file_path)
 
        print("@@ Predicting class......")
        pred, output_page,res1= pred_tom(tomato=file_path,fer=pest1)
        
        
        
        pl1=["1.PNG","2.PNG"]
        pl2=["3.PNG","4.PNG"]
        pl3=["5.PNG","6.PNG"]
        pl4=["7.PNG","8.PNG"]
        pl5=["9.PNG","10.PNG"]
        pl6=["11.PNG","12.PNG"]
        pl7=["13.PNG","14.PNG"]
        pl8=["15.PNG","16.PNG"]
        pl9=["17.PNG","18.PNG"]
        pl10=["19.PNG","20.PNG"]
        pl11=["21.PNG","22.PNG"]
        pl12=["23.PNG","24.PNG"]
        pl13=["25.PNG","26.PNG"]
        pl14=["27.PNG","28.PNG"]
        pl15=["29.PNG","30.PNG"]
        pl16=["31.PNG","32.PNG"]
        pl17=["33.PNG","34.PNG"]
        pl18=["35.PNG","36.PNG"]
        pl19=["37.PNG","38.PNG"]
        pl20=["39.PNG","40.PNG"]
        pl21=["41.PNG","42.PNG"]
        pl22=["43.PNG","44.PNG"]
        
        
        pestList={"pest1":pl1,"pest2":pl2,"pest3":pl3,"pest4":pl4,"pest5":pl5,"pest6":pl6,"pest7":pl7,"pest8":pl8,"pest9":pl9,"pest10":pl10,"pest11":pl11,"pest12":pl12,"pest13":pl13,"pest14":pl14,"pest15":pl15,"pest16":pl16,"pest17":pl17,"pest18":pl18,"pest19":pl19,"pest20":pl20,"pest21":pl21,"pest22":pl22 }
        
        if res1 in pestList:
            pestr=pestList[res1]
       
        print(pestr[0]) 
        
        
        
        
        
        
               
        return render_template(output_page, pred_output = pred, user_image = file_path,pestres=pestr)
 
        
 
@app.route("/cpredict", methods = ['GET','POST'])
def cpredict():
     if request.method == 'POST':
        file = request.files['image'] # fet input
        filename = file.filename        
        print("@@ Input posted = ", filename)
        
        pest1=[]
        
        nitro = request.form.get("nitro")
        n=float(nitro)
        pest1.append(n)
        
        
        phos = request.form.get("phos")
        p=float(phos)
        pest1.append(p)
        
        
        pot = request.form.get("pot")
        k=float(pot)
        pest1.append(k)
        
        temp = request.form.get("temp")
        t=float(temp)
        pest1.append(t)
        
        
        mos = request.form.get("mos")
        m=float(mos)
        pest1.append(m)
        
        ph = request.form.get("ph")
        p1=float(ph)
        pest1.append(p1)
        
        
        rain = request.form.get("rain")
        r=float(rain)
        pest1.append(r)
        
        
        print("@@ nitro = ", nitro)
        n=float(nitro)
        print(type(n))
        file_path = os.path.join('static/user uploaded', filename)
        file.save(file_path)
 
        print("@@ Predicting class......")
        pred, output_page,res1= pred_corn(corn=file_path,fer=pest1)
        
        
        
        pl1=["1.PNG","2.PNG"]
        pl2=["3.PNG","4.PNG"]
        pl3=["5.PNG","6.PNG"]
        pl4=["7.PNG","8.PNG"]
        pl5=["9.PNG","10.PNG"]
        pl6=["11.PNG","12.PNG"]
        pl7=["13.PNG","14.PNG"]
        pl8=["15.PNG","16.PNG"]
        pl9=["17.PNG","18.PNG"]
        pl10=["19.PNG","20.PNG"]
        pl11=["21.PNG","22.PNG"]
        pl12=["23.PNG","24.PNG"]
        pl13=["25.PNG","26.PNG"]
        pl14=["27.PNG","28.PNG"]
        pl15=["29.PNG","30.PNG"]
        pl16=["31.PNG","32.PNG"]
        pl17=["33.PNG","34.PNG"]
        pl18=["35.PNG","36.PNG"]
        pl19=["37.PNG","38.PNG"]
        pl20=["39.PNG","40.PNG"]
        pl21=["41.PNG","42.PNG"]
        pl22=["43.PNG","44.PNG"]
        
        
        pestList={"pest1":pl1,"pest2":pl2,"pest3":pl3,"pest4":pl4,"pest5":pl5,"pest6":pl6,"pest7":pl7,"pest8":pl8,"pest9":pl9,"pest10":pl10,"pest11":pl11,"pest12":pl12,"pest13":pl13,"pest14":pl14,"pest15":pl15,"pest16":pl16,"pest17":pl17,"pest18":pl18,"pest19":pl19,"pest20":pl20,"pest21":pl21,"pest22":pl22 }
        
        if res1 in pestList:
            pestr=pestList[res1]
       
        print(pestr[0]) 
          
        
        return render_template(output_page, pred_output = pred, user_image = file_path,pestres=pestr)    
    
 

@app.route("/ppredict", methods = ['GET','POST'])
def ppredict():
     if request.method == 'POST':
        file = request.files['image'] # fet input
        filename = file.filename        
        print("@@ Input posted = ", filename)
        
        pest1=[]
        
        nitro = request.form.get("nitro")
        n=float(nitro)
        pest1.append(n)
        
        
        phos = request.form.get("phos")
        p=float(phos)
        pest1.append(p)
        
        
        pot = request.form.get("pot")
        k=float(pot)
        pest1.append(k)
        
        temp = request.form.get("temp")
        t=float(temp)
        pest1.append(t)
        
        
        mos = request.form.get("mos")
        m=float(mos)
        pest1.append(m)
        
        ph = request.form.get("ph")
        p1=float(ph)
        pest1.append(p1)
        
        
        rain = request.form.get("rain")
        r=float(rain)
        pest1.append(r)
        
        
        print("@@ nitro = ", nitro)
        n=float(nitro)
        print(type(n))
        file_path = os.path.join('static/user uploaded', filename)
        file.save(file_path)
 
        print("@@ Predicting class......")
        pred, output_page,res1= pred_pot(potato=file_path,fer=pest1)
               
        
        
        pl1=["1.PNG","2.PNG"]
        pl2=["3.PNG","4.PNG"]
        pl3=["5.PNG","6.PNG"]
        pl4=["7.PNG","8.PNG"]
        pl5=["9.PNG","10.PNG"]
        pl6=["11.PNG","12.PNG"]
        pl7=["13.PNG","14.PNG"]
        pl8=["15.PNG","16.PNG"]
        pl9=["17.PNG","18.PNG"]
        pl10=["19.PNG","20.PNG"]
        pl11=["21.PNG","22.PNG"]
        pl12=["23.PNG","24.PNG"]
        pl13=["25.PNG","26.PNG"]
        pl14=["27.PNG","28.PNG"]
        pl15=["29.PNG","30.PNG"]
        pl16=["31.PNG","32.PNG"]
        pl17=["33.PNG","34.PNG"]
        pl18=["35.PNG","36.PNG"]
        pl19=["37.PNG","38.PNG"]
        pl20=["39.PNG","40.PNG"]
        pl21=["41.PNG","42.PNG"]
        pl22=["43.PNG","44.PNG"]
        
        
        pestList={"pest1":pl1,"pest2":pl2,"pest3":pl3,"pest4":pl4,"pest5":pl5,"pest6":pl6,"pest7":pl7,"pest8":pl8,"pest9":pl9,"pest10":pl10,"pest11":pl11,"pest12":pl12,"pest13":pl13,"pest14":pl14,"pest15":pl15,"pest16":pl16,"pest17":pl17,"pest18":pl18,"pest19":pl19,"pest20":pl20,"pest21":pl21,"pest22":pl22 }
        
        if res1 in pestList:
            pestr=pestList[res1]
       
        print(pestr[0]) 
        
        return render_template(output_page, pred_output = pred, user_image = file_path,pestres=res1)    
 

   
@app.route("/gpredict", methods = ['GET','POST'])
def gpredict():
     if request.method == 'POST':
        file = request.files['image'] # fet input
        filename = file.filename        
        print("@@ Input posted = ", filename)
        
        pest1=[]
        
        nitro = request.form.get("nitro")
        n=float(nitro)
        pest1.append(n)
        
        
        phos = request.form.get("phos")
        p=float(phos)
        pest1.append(p)
        
        
        pot = request.form.get("pot")
        k=float(pot)
        pest1.append(k)
        
        temp = request.form.get("temp")
        t=float(temp)
        pest1.append(t)
        
        
        mos = request.form.get("mos")
        m=float(mos)
        pest1.append(m)
        
        ph = request.form.get("ph")
        p1=float(ph)
        pest1.append(p1)
        
        
        rain = request.form.get("rain")
        r=float(rain)
        pest1.append(r)
        
        
        print("@@ nitro = ", nitro)
        n=float(nitro)
        print(type(n))
        file_path = os.path.join('static/user uploaded', filename)
        file.save(file_path)
 
        print("@@ Predicting class......")
        pred, output_page,res1= pred_grapes(grapes=file_path,fer=pest1)
               
        
        
        pl1=["1.PNG","2.PNG"]
        pl2=["3.PNG","4.PNG"]
        pl3=["5.PNG","6.PNG"]
        pl4=["7.PNG","8.PNG"]
        pl5=["9.PNG","10.PNG"]
        pl6=["11.PNG","12.PNG"]
        pl7=["13.PNG","14.PNG"]
        pl8=["15.PNG","16.PNG"]
        pl9=["17.PNG","18.PNG"]
        pl10=["19.PNG","20.PNG"]
        pl11=["21.PNG","22.PNG"]
        pl12=["23.PNG","24.PNG"]
        pl13=["25.PNG","26.PNG"]
        pl14=["27.PNG","28.PNG"]
        pl15=["29.PNG","30.PNG"]
        pl16=["31.PNG","32.PNG"]
        pl17=["33.PNG","34.PNG"]
        pl18=["35.PNG","36.PNG"]
        pl19=["37.PNG","38.PNG"]
        pl20=["39.PNG","40.PNG"]
        pl21=["41.PNG","42.PNG"]
        pl22=["43.PNG","44.PNG"]
        
        
        pestList={"pest1":pl1,"pest2":pl2,"pest3":pl3,"pest4":pl4,"pest5":pl5,"pest6":pl6,"pest7":pl7,"pest8":pl8,"pest9":pl9,"pest10":pl10,"pest11":pl11,"pest12":pl12,"pest13":pl13,"pest14":pl14,"pest15":pl15,"pest16":pl16,"pest17":pl17,"pest18":pl18,"pest19":pl19,"pest20":pl20,"pest21":pl21,"pest22":pl22 }
        
        if res1 in pestList:
            pestr=pestList[res1]
       
        print(pestr[0]) 
        
    
        return render_template(output_page, pred_output = pred, user_image = file_path,pestres=res1)
    
 
# For local system &amp; cloud
if __name__ == "__main__":
    app.run(threaded=False) 