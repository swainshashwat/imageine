from keras import backend as keras
from keras.applications.vgg16 import preprocess_input
from keras.preprocessing.image import load_img, img_to_array

# paths
c_im_path = 'data/megan_fox.jpg'
s_im_path = 'data/melodyonight.jpg'

# target dims
targetHeight = 512
targetWidth = 512
targetSize = (targetHeight, targetWidth)

# loadin and preprocessing images
cImage = load_img(path)
