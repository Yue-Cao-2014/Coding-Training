from reader import read_csv_as_columns

data = read_csv_as_columns('Python_Mastery/Data/ctabus.csv', 
                            [str, str, str, int])
print(data)
print(data[1])