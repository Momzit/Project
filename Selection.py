import os
import zipfile
import pandas as pd
import numpy as np
from os import rename
import datetime
# from astropy.io import ascii
os.chdir("/home/momentum/Downloads/MomentP/Project/data selection/2001")

# =====================USING PANDAS=====================
for folder, subfolders,files in os.walk('.'):
    for file in files:
        if file.startswith('scan'):
            ii = int(file[-6:-4])
            jj = int(file[-8:-6])
            data=pd.read_csv(file,
                            delim_whitespace=True,
                            na_values='99999.0',
                            parse_dates={'Timestamp':[0,1,2,3]},
                            keep_date_col=True,
                            # date_parser=lambda x: pd.datetime.strptime(x,'%Y %m %d %H %M'),
                            # infer_datetime_format=True,
                            # index_col='Timestamp',
                            encoding='cp1252',
                            )

            # format='%Y %m %d %H %M',
            data['Timestamp'] = pd.to_datetime(data['Timestamp'], format='%Y %m %d %H')
            data.index = data['Timestamp']
            del data['Timestamp']

            start = '2001-%02d-%02d 19:00:00' %(jj, ii)
            end =  '2001-%02d-%02d 23:00:00' %(jj, ii)
            # print(end)

            select = data.loc[start:end]
            # print(select)
            # select = data.loc['2001 01 01 19:00:00' : '2001 01 01 23:00:00']

            s = 'testing_%02d%02d'%(jj, ii)
            s1 = s + '.dat'
            # print(s1)
            select.to_csv(s1, sep=' ', na_rep='NaN', float_format='%.3f', index=False)
