import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", dest="file", help="input data file")

args = parser.parse_args()
file = args.file

insurance = pd.read_csv(filepath_or_buffer=file, sep=',', header=0)
print(insurance)

#we have done it! this prints the data