import pandas as pd




def preprocess(bf,cf):
    # filtering for summer olympics
    bf = bf[bf['Season'] == 'Summer']
    # merge with cf
    bf = bf.merge(cf,on='NOC', how='left')
    # Dropping duplicates
    bf.drop_duplicates(inplace=True)
    # One HOt Encoding Medals
    bf = pd.concat([bf, pd.get_dummies(bf['Medal'])], axis=1)
    return bf

