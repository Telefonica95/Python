# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 10:27:18 2021

@author: dimabors
"""
import numpy as np
import pandas as pa


def computeLanguageError(freq):
    l_frequency = pa.read_csv("letter_frequencies.csv")
    arraySize =0;
    E = np.zeros(arraySize)
    headerArray=['English','French','German', 'Spanish','Portuguese','Esperanto','Italian','Turkish','Swedish','Polish','Dutch','Danish','Icelandic','Finnish','Czech']

    for i in range(0, len(headerArray), 1):
            h=headerArray[i]
            subtotal=(np.array(l_frequency[h])-freq)**2
            z=sum(subtotal)
            E = np.append(E, z)
       
    return E


print(computeLanguageError(np.array([8.101852, 2.237654,
                                     2.469136, 4.552469, 12.345679, 2.006173, 1.929012,
                                     6.712963, 7.175926, 0.077160, 1.157407, 3.395062,
                                     1.080247, 6.712963, 7.870370, 1.466049, 0.077160,
                                     6.018519, 5.401235, 10.956790, 2.854938, 0.925926,
                                     2.932099, 0.000000, 1.543210, 0.000000])))
