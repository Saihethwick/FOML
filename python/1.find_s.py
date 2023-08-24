import pandas as pd
import numpy as np
d = pd.read_csv("ws.csv") 
print(d)
a = np.array(d)[:,:-1] 
t = np.array(d)[:,-1] 
def train(c, t):
    for i, val in enumerate(t):
        if val == "Yes":
            specific_hypothesis = c[i].copy()
            break
    for i, val in enumerate(c):
        if t[i] == "Yes":
            for x in range(len(specific_hypothesis)):
                if val[x] != specific_hypothesis[x]:
                    specific_hypothesis[x] = '?'
                else:
                    pass
    return specific_hypothesis
print(" The final hypothesis is:",train(a,t))
