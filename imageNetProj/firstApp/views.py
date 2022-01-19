from django.shortcuts import render
#from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import os

# Create your views here.


import pytesseract
import ftfy
import easyocr
import json
import pytesseract
import cv2
import numpy as np
import sys
import re
import os
from PIL import Image
import ftfy
import io
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
from imutils.object_detection import non_max_suppression
import regex as re
import json
import pickle



model = 'abc'
model = list(model)
model=pd.read_pickle('./models/Extract_D.pkl')




def index(request):
    context={'a':1}
    return render(request,'index.html', context)

def predictImage(request):
    print(request)
    print(request.POST.dict())
    fileObj=request.FILES['filePath']
    fs=FileSystemStorage()
    filePathName=fs.save(fileObj.name,fileObj)
    filePathName=fs.url(filePathName)

    testimage='.'+filePathName

    img = cv2.imread(testimage)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # CHANGE VALUE HERE
    n = 170
    th, threshed = cv2.threshold(gray, n, 255, cv2.THRESH_TRUNC)
    t1 = pytesseract.image_to_data(threshed, output_type='data.frame')
    pd.set_option('max_columns', None)
    t2 = pytesseract.image_to_string(threshed)
    text = t1[t1.conf != -1]
    lines = text.groupby('block_num')['text']
    conf = text.groupby(['block_num'])['conf'].mean()
    t3 = str(t2)
    rough = t2
    L = t3
    string = t3
    bas = t3
    s1 = 'abc'
    s1 = str(s1)
    s1 = string
    s1 = str(s1)
    s2 = []
    dob = None
    x = 'abc'
    x = str(x)
    x = s1.split("\n")
    prices = []
    for i in range(0, len(x)):
        if x[i].isupper():
            price = x[i]
            prices.append(price)
    string = []
    for i in range(1, len(prices)):
        price = prices[i]
        string.append(price)
    t4 = prices
    string = t4
    Tosort1 = []
    for i in range(len(string) - 1, -1, -1):
        price = string[i]
        Tosort1.append(price)
    Tosort2 = []
    for i in range(len(Tosort1)):
        res = True if next((chr for chr in Tosort1[i] if chr.isdigit()), None) else False
        if res == True:
            continue
        else:
            Tosort = Tosort1[i]
            Tosort2.append(Tosort)
    for i in range(len(Tosort2)):
        if i == 0:
            Fname = Tosort2[i]
            #print("Father Name : ", Fname)
        elif i == 1:
            Hname = Tosort2[i]
            #print("Name : ", Hname)
    Tosort3 = []
    for i in range(len(Tosort1)):
        res = True if next((chr for chr in Tosort1[i] if chr.isdigit()), None) else False
        if res == True:
            if Tosort1[i].isupper():
                Pn = Tosort1[i]
                #print("Pan Number : ", Pn)
        else:
            continue
    test_string = bas
    temp = re.findall(r'\d+', test_string)
    res = list(map(int, temp))
    prices = []
    year = 'abc'
    for i in range(0, len(res)):
        price = res[i]
        prices.append(price)
        value = price
        if value < 31:
            da = value
            price = res[i + 1]
            value = price
            if value < 12:
                month = value
                price = res[i + 2]
                value = price
                if value > 1947:
                    if value < 2022:
                        year = value
                        break
        else:
            continue
    #print("Date of birth :", da, "/", month, "/", year)

    predictedName = Hname
    predictedFatherName = Fname
    predictedPanNumber = Pn
    predictedDate = da
    predictedMonth = month
    predictedYear = year
    context = {'filePathName':filePathName,'predictedName':predictedName,'predictedFatherName':predictedFatherName,
               'predictedPanNumber':predictedPanNumber,'predictedDate':predictedDate,'predictedMonth':predictedMonth,
               'predictedYear':predictedYear}
    return render(request,'index.html',context)

#Hello

