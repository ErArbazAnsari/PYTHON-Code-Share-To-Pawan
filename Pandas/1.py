# import pandas as pd

# try:
#     df = pd.read_csv("D:\PROFESSIONAL DATA\CODING LIFE\PYTHON\Pandas\file.csv")
#     print(df.head())
# except FileNotFoundError:
#     print("File not found.")
# except pd.errors.ParserError:
#     print("Error reading the file.")
with open("D:\PROFESSIONAL DATA\CODING LIFE\PYTHON\Pandas\file.csv") as file:
    data = file.readlines()
    print(data)