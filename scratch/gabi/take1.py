#from sugar import *
import os, sys, pandas as pd, numpy as np
def shuffle(x):
    y = x.copy()
    np.random.shuffle(y)
    return y
path = '../../data'
fname = 'spxs.csv'
x = pd.read_csv(os.path.join(path, fname))
x.columns = map(str.strip, x.columns)
#x = qselect(x, 't: Date, c: Close/Last')[::-1]
x = x.rename(columns={'Date': 't', 'Close/Last': 'c'})[['t','c']][::-1]
x['m']=x.c.rolling(100).mean()
x['s']=x.c > x.m
x['rPast'] = x.c.pct_change()
x['rFuture'] = x.c.pct_change().shift(-1)
x=x.dropna()
a=np.prod(1+x.rFuture)-1
b=np.prod(1+x.rFuture[x.s])-1
y=np.array([np.prod(1+x.rFuture[shuffle(x.s.values)])-1 for i in range(1000)])
print(a, b, np.mean(b>=y))
