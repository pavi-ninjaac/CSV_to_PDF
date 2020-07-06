# import the required libraries
import pdfkit as pdf
import pandas as pd
# i  am considering the  current working derectory as path but youhave to set the whole path 
#read the csv file as dataframe
csv_file=pd.read_csv('emotion.csv')

#convert the csv to html file
html_file=csv_file.to_html('emotion.html')

#define the path for pdf file
html_file_path='emotion.html'
pdf_file_path='emotion.pdf'

# convert the html to pdf
pdf.from_file(html_file_path,pdf_file_path)
