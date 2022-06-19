# importing required libraries

import numpy as np
from PIL import Image
import os
import string
from pickle import dump
from pickle import load
from keras.applications.xception import Xception
from keras.applications.xception import preprocess_input
from keras_preprocessing.image import load_img
from keras_preprocessing.image import img_to_array
from keras_preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
from keras.layers.merging import add
from keras.layers import Input, Dense
from keras.layers import LSTM, Dropout, Embedding
from keras.models import Model, load_model
from tqdm import tqdm_notebook as tqdm


# loading the document file into memory
def load_fp(filename):
    file = open(filename, 'r')
    text = file.read()
    file.close()
    return text


# get all images with their captions
def img_capt(filename):
    file = open(filename)
    captions = file.split('n')
    print(captions)
    exit()


if __name__ == '__main__':
    img_capt('Flickr8k.token.txt')
