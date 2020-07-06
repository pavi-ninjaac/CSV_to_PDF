# import the required libraries
import pdfkit as pdf
import pandas as pd

#read the csv file as dataframe
csv_file=pd.read_csv(r'F:\dash_app\dash_ibm_app\dataset\emotion.csv')

#convert the csv to html file
html_file=csv_file.to_html(r'F:\dash_app\dash_ibm_app\dataset\emotion.html')

#define the path for pdf file
html_file_path=r'F:\dash_app\dash_ibm_app\dataset\emotion.html'
pdf_file_path=r'F:\dash_app\dash_ibm_app\dataset\emotion.pdf'

# convert the html to pdf
pdf.from_file(html_file_path,pdf_file_path)
