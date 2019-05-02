#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 15:25:13 2019

@author: yizhang
"""

import pandas as pd
import numpy as np
import glob
import errno
import os
import re


folder = r"/Users/yizhang/Downloads/GPS Test Data/Total"

filepaths = glob.glob(os.path.join(folder, '2018*.txt'))

headers = []

for fp in filepaths:

    with open(fp, 'r') as f:
       first_line = f.readlines()
       headers.append(first_line)
       



searchRegex = {'Date':'(\d\d\d\d-\d\d-\d\d)',
               'Time':'(?<=\d\d\d\d-\d\d-\d\d )(\d\d:\d\d:\d\d)',
               'InputSN':'(?<=Input SN : )(\w+-\w+-\w+)',
               'Enabletime':'(?<=Enable GPS Module OK! Use time = )(\d+.\d+)',
               'TTFF':'(?<=TTFF = )(\d+.\d+)',
               'SNR1':'(?<=SNR1 = )(\d+)',
               'SNR2':'(?<=SNR2 = )(\d+)',
               'SNR3':'(?<=SNR3 = )(\d+)',
               'SNR4':'(?<=SNR4 = )(\d+)',
               'SNR5':'(?<=SNR5 = )(\d+)',
               'SNR6':'(?<=SNR6 = )(\d+)',
               'SNR7':'(?<=SNR7 = )(\d+)',
               'SNR8':'(?<=SNR8 = )(\d+)',
               'Singletime':'(?<=GPS Signal Test PASS! Use time = )(\d+.\d+)',
               'Totaltime':'(?<=Total Time )(\d\d:\d\d:\d\d)',
               'Detecttime':'(?<=Detect OK! Use time = )(\d+.\d+)'
               }

OutPutDict = {'SNR1':[],
              'SNR2':[],
              'SNR3':[],
              'SNR4':[],
              'SNR5':[],
              'SNR6':[],
              'SNR7':[],
              'SNR8':[],
              'Time':[],
              'Date':[],
              'InputSN':[],
              'Enabletime':[],
              'TTFF':[],
              'Singletime':[],
              'Totaltime':[],
              'Detecttime':[]
              }

for key in searchRegex:
    for file in headers:
        found = False
        
        for line in file:
            t = re.search(searchRegex[key], line)
            if t:
                OutPutDict[key].append(t[0])
                found = True
        if found == False:
            OutPutDict[key].append('')
            

OutputDF = pd.DataFrame(OutPutDict)

OutputDF.to_csv('Total.csv')
