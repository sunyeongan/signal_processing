from IPython.display import display
import matplotlib.pyplot as plt
%matplotlib inline
import numpy as np
import os
import shutil
import posixpath
import wfdb

 #https://physionet.org/content/cdb/1.0.0/

record = wfdb.rdrecord('08730_01',pn_dir = 'cdb', sampfrom=1, sampto = 5119) # 위의 사이트에서 08730_01.hea파일을 불러옴 
wfdb.plot_wfdb(record=record) 
display(record.__dict__)

signals, fields = wfdb.rdsamp('08730_01' ,pn_dir = 'cdb')

print(type(signals))

print(type(fields))

print(signals.shape)

print(fields)

chid = 0
data = record.p_signal
channel = data[:,0]

sample_su = 2000

times = np.arange(sample_su, dtype='float')/record.fs
plt.plot(times, channel[:sample_su])
plt.xlabel('Time [s]')
plt.show()

data.shape
