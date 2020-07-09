
import keras
import tensorflow as tf
from keras.models import load_model
from keras.utils import CustomObjectScope
from keras.initializers import glorot_uniform
from pyimagesearch.images.imageProcess import *


labelNames = ["top", "trouser", "pullover", "dress", "coat",
	"sandal", "shirt", "sneaker", "bag", "ankle boot"]

loaded_model = tf.keras.models.load_model('model.h5')
img = imageTests()
print(img.shape)
for i in range(84):
	# classify the clothing
    probs = loaded_model.predict(img[np.newaxis,i])
    prediction = probs.argmax(axis=1)
    label = labelNames[prediction[0]]
    index = 10000 + i
    print('image: '+str(index)+'================'+label+'=================')