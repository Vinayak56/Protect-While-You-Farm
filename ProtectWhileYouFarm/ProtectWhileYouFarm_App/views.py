from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

from keras.models import load_model
from keras.preprocessing import image
import tensorflow as tf
import json
from tensorflow import Graph


img_height, img_width=150,150
with open('./models/image_class.json','r') as f:
    labelInfo=f.read()

labelInfo=json.loads(labelInfo)
    
model_graph = Graph()
with model_graph.as_default():
    tf_session = tf.compat.v1.Session()
    with tf_session.as_default():
        model=load_model('./models/Mymodel.h5')

def home(request):
    return render(request, 'home.html')

def addImage(request):
    return render(request,'addImage.html')

def predictDisease(request):
    print(request)
    print(request.POST.dict())
    fileObj=request.FILES['filePath']
    fs=FileSystemStorage()
    filePathName=fs.save(fileObj.name, fileObj)
    filePathName=fs.url(filePathName)
    context={'filePathName':filePathName}
    testimage='.'+filePathName
    img = image.load_img(testimage, target_size=(img_height, img_width))
    x = image.img_to_array(img)
    x=x/255
    x=x.reshape(1,img_height, img_width,3)
    with model_graph.as_default():
        with tf_session.as_default():
            predi=model.predict(x)
    print(predi)

    import numpy as np
    print(str(np.argmax(predi[0])))
    predictedLabel=labelInfo[str(np.argmax(predi[0]))]
    print(predictedLabel)
    context={'filePathName':filePathName,'predictedLabel':predictedLabel[1]}
    return render(request, 'addImage.html', context)
     