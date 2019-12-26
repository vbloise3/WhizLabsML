import pandas as pd

read_file = pd.read_excel (r'CensusIncomeDataset.xlsx')
read_file.to_csv (r'CensusIncomeDataset.csv', index = None, header=False)
