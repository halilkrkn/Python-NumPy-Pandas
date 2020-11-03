# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np


data = np.array(["halil","ElifGul","Goktug"])
s = pd.Series(data, index=[1,2,3])
print(s)
print(s[1])
print("*************")

data2 = {"matematik":10, "fizik":20,"beden eğitimi":100}
s2 = pd.Series(data2, index = ["fizik","matematik","beden eğitimi"])
print(s2)

print(s2[0])
print("*************")

s3 = pd.Series(5,index = [1,2,3])
print(s3)