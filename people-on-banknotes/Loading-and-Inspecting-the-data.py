import pandas as pd

# Display the dataframe

banknotes = pd.read_csv('people-on-banknotes.csv')
banknotes # To display dataframe

# Utilizing the read_csv() parameters [specific columns and number of rows]
banknotes_parameters = pd.read_csv('people-on-banknotes.csv', usecols=["country", "name", "gender", "occupation", "value", "currency_code"], nrows=25)
banknotes_parameters

# Displaying the first 10 rows using head()
banknotes.head(10)

# Displaying the last 10 rows of the dataset using tail()
banknotes.tail(10)


# Displaying the structure of the dataset using info()
banknotes.info()

# Displaying the distribution of the dataset using describe()
banknotes.describe() # You can include all columns by using the include="all" argument

# Showing the number of rows and columns using shape
banknotes.shape

# Showing all columns/variables names in the dataset using columns
banknotes.columns

# Figuring out the datatype for each variable using dtypes
banknotes.dtypes

# Figuring the null count for per variable
banknotes.isnull().sum()

# Showing the count of the exact number of duplicated rows
banknotes.duplicated().sum()

# Showing the count of duplicated rows for a specific column
banknotes.duplicated(subset=["name"]).sum()





