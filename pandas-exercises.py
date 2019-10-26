import pandas as pd
import os
import os.path


insurance = pd.read_csv(filepath_or_buffer='\Users\zachz\Desktop\insurance.csv', sep=',', header=0)
print(insurance)