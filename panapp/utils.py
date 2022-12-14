import cv2
import numpy as np
import pytesseract
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image
import re
from django.conf import settings
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

   
# def get_computed(img):
#     img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#     mypan=pytesseract.image_to_string(img, lang ="eng+hin")
#     l=[]
#     l=mypan.splitlines()
#     for i in len(l):
#         if(bool(re.match('((?=.*\d)(?=.*[A-Z]).{10})', l[i]))==True):
#             pan_id=l[i]
#     return pan_id
    
def get_computedagain(img):
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    mypan=pytesseract.image_to_string(img, lang ="eng+hin")
    pan_details=mypan
    return pan_details
