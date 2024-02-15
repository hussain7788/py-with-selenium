# '''
# terface for working with tabular data, such as spreadsheets or CSV files. It is designed to make it easy to import, manipulate, and export data in various formats. Some key features and use cases of tablib include:

# Data Import/Export: tablib supports importing and exporting data in various formats, including Excel, JSON, YAML, CSV, and others. This makes it convenient to work with data in different environments or with different tools.

# Tabular Data Handling: tablib allows you to work with tabular data in a programmatic way. You can create datasets, add rows and columns, manipulate data, and perform operations on tabular structures.

# Integration with Pandas: tablib can be used in conjunction with Pandas. You can convert tablib datasets to Pandas DataFrames and vice versa, providing flexibility in data analysis and manipulation.

# Export to Different Formats: You can easily convert datasets to various formats, allowing you to export data in the format that best suits your needs.

# Here's a simple example demonstrating the basic usage of tablib:
# '''

from tablib import Dataset

# Create a dataset
dataset = Dataset()
dataset.headers = ['Name', 'Age', 'City']
dataset.append(['Alice', 28, 'New York'])
dataset.append(['Bob', 35, 'San Francisco'])
dataset.title = 'My Sheet'

# Export to CSV
csv_data = dataset.csv
print(csv_data)

# Export to Excel
excel_data = dataset.export('xlsx')
print(excel_data, type(excel_data))
with open('output.xlsx', 'wb') as f:
    f.write(excel_data)

# dt = tablib.Dataset()
# dt.headers = ['Name', 'age']
# dt.append(['Hussain', 27])
# dt.append(['Valli', 28])

# xl_data = dt.xlsx
# print(xl_data)
# with open('test.xlsx', 'wb') as f:
#     f.write(xl_data)


