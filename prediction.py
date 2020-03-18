# from keras.preprocessing import image
import tensorflow as tf

from tensorflow.keras.preprocessing import image

import numpy as np

# from keras.models import load_model

model=tf.keras.models.load_model('C:\\Users\\KRITIK SHIVANSHU\\Desktop\\Pavement_condition_assessment-master\\testing_model_first.h5')


def pred(image_path):
    img = image.load_img(image_path, target_size=(250, 250))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    # images = np.vstack([x])
    classes = model.predict(x, batch_size=6)
    if(classes[0][0]>=0.5):
      classes[0][0]=1
    else:
      classes[0][0]=0
    if(classes[0][0])==0:
        return ("The road photograph is normal")
    else: 
        return ("The road photograph contains potholes")


# def pred(image_path):
#     path=image_path
#     type(path)
#     print("nihal")
#     classes=path
#     return classes
