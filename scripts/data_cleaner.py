import pandas as pd
import os

ryan_file = 'data/{}'.format(pd.read_csv('../file_names.txt', header=0)['Ryan'].iloc[0])
vance_file = 'data/{}'.format(pd.read_csv('../file_names.txt', header=0)['Vance'].iloc[0])
os.remove('../file_names.txt')

def convert_string(x):
    if not x:
        return ''
    try:
        return str(x)   
    except:        
        return ''

def convert_int(x):
    if not x:
        return ''
    try:
        return str(x)   
    except:        
        return ''

convert_dict = {10:convert_string, 18:convert_string, 22:convert_int, 27:convert_string, 28:convert_string, 29:convert_string, 30:convert_string, 32:convert_string, 33:convert_string, 34:convert_string, 41:convert_string}

ryan = pd.read_csv(ryan_file, converters=convert_dict, header=1)
vance = pd.read_csv(vance_file, converters=convert_dict, header=1)

os.remove(ryan_file)
os.remove(vance_file)

ryan_details = pd.DataFrame()
ryan_details['Type'] = ryan.iloc[:,5]
ryan_details['Address'] = ryan.iloc[:,12]
ryan_details['City'] = ryan.iloc[:,14]
ryan_details['State'] = ryan.iloc[:,15]
ryan_details['Amount'] = ryan.fillna(0).iloc[:,20]
ryan_details = ryan_details.iloc[1:]

vance_details = pd.DataFrame()
vance_details['Type'] = vance.iloc[:,5]
vance_details['Address'] = vance.iloc[:,12]
vance_details['City'] = vance.iloc[:,14]
vance_details['State'] = vance.iloc[:,15]
vance_details['Amount'] = vance.fillna(0).iloc[:,20]
vance_details = vance_details.iloc[3:]

ryan_details.to_csv('data/tim_ryan.csv')
vance_details.to_csv('data/jd_vance.csv')