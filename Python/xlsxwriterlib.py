'''
XlsxWriter is a Python library for creating Excel files in the .xlsx format. It allows you to generate Excel files with various formatting, charts, images, and other features. Unlike some other libraries that support reading and manipulating existing Excel files, XlsxWriter is specifically designed for creating new Excel files from scratch.

Some key features of XlsxWriter include:

Creating Worksheets and Cells: You can add worksheets to your Excel file and populate them with data by adding cells. XlsxWriter provides functions for formatting cells, setting values, and applying various styles.

Cell Formatting: You can apply different formatting options to cells, such as fonts, colors, borders, alignment, and number formats.

Charts and Graphs: XlsxWriter supports the creation of various types of charts and graphs within your Excel file.

Images and Drawings: You can embed images and drawings into your Excel file using XlsxWriter.

Conditional Formatting: Apply conditional formatting rules to cells based on specified criteria.

Here's a simple example demonstrating the basic usage of XlsxWriter:
'''



#### Xlsxwriter is mainly used for creating xl files only if we want to read or modify 
#### excel data then use 'openpyxl' or 'pandas' libraries

import xlsxwriter

# Create a new Excel workbook and add a worksheet
workbook = xlsxwriter.Workbook('example.xlsx')
import pdb;pdb.set_trace()
worksheet = workbook.add_worksheet()

# Write some data to the worksheet
worksheet.write(0, 0, 'Name')
worksheet.write(0, 1, 'Age')
worksheet.write(0, 2, 'Salary')
worksheet.write(1, 0, 'Hussain')
worksheet.write(1, 1, '26')
worksheet.write(1, 2, '40000')
worksheet.write(2, 0, 'Valli')
worksheet.write(2, 1, '27')
worksheet.write(2, 2, '30000')


# Add a chart
chart = workbook.add_chart({'type': 'column'})
chart.add_series({'values': '=Sheet1!$A$1:$A$2'})

# Insert the chart into the worksheet
worksheet.insert_chart('C1', chart)

# Close the workbook
workbook.close()

import pandas as pd
with open('example.xlsx', 'rb') as f:
    data = pd.read_excel(f)
    print(data)
