import os
import pandas as pd

all_df_list = []

for filename in os.listdir('/Users/baltasarsalamonwelwert/Downloads/DataFamilySearch'):
    os.chdir("/Users/baltasarsalamonwelwert/Downloads/DataFamilySearch") 
    print(os.listdir())
    tmpfile = pd.read_excel(filename)
    all_df_list.append(tmpfile)

appended_df = pd.concat(all_df_list)
appended_df.to_excel("NewFile.xlsx", index=False)

# Write the appended dataframe to an excel file
# Add index=False parameter to not include row numbers
#appended_df.to_excel("AllCompanyNames.xlsx", index=False)