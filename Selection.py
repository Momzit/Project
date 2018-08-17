import os
import zipfile
import pandas as pd
import numpy as np
from os import rename
import datetime
# from astropy.io import ascii

#=====================USING PANDAS=====================
data=pd.read_csv('scanchamp20010101.dat',
         delim_whitespace=True,
         na_values='99999.0',
         parse_dates={'Timestamp':[0,1,2,3]},
         keep_date_col=True,
         # date_parser=lambda x: pd.datetime.strptime(x,'%Y %m %d %H %M'),
         # infer_datetime_format=True,
         # index_col='Timestamp',
         )

# format='%Y %m %d %H %M',
data['Timestamp'] = pd.to_datetime(data['Timestamp'], format='%Y %m %d %H')
data.index = data['Timestamp']
del data['Timestamp']

select = data.loc['2001-01-01 19:00:00']
# select = data.loc['2001 01 01 19:00:00' : '2001 01 01 23:00:00']

select.to_csv('testing.dat', sep=' ', na_rep='NaN', float_format='%.3f')
#=====================USING NUMPY=====================
#=====================USING BUILT-IN=====================
# with open("scanchamp20010101.dat", "r") as f:
#     for line in f:
#         data = line.split()
#         with open("testing.dat", "w+") as n_f:
#             n_f.write(str(data))
#             n_f.write("\n")
#=====================ASTROPY METHOD=====================
