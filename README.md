# Convert_CSV_to_PDF:
I am doing smarter chatbot for covid19 sentiment analysis, for that I have to convert the csv file data to pdf <br/>
 to import the data into Watson discovery. For that I followed the very simple way, that is below <br/>
-	1) Install the required libraries
-	2) Install the wkhtmltopdf software
-	3) Convert csv to html
-	4) Convert html to pdf

# Install the required libraries:
To convert the csv file to pdf we need pandas and pdfkit libraries of python. You can download it by pip install <br/>
> pip3 install pandas <br/>
> pip install  pdfkit

# Install the wkhtmltopdf software:
        We can convert the CSV file directly to PDF format, but the easier way than that is covert the <br/>
CSV to HTML and then convert the HTML to PDF file. While converting the HTML to PDF we need one software namely wkhtmltopdf.<br/>
Wkhtmltopdf is an open source software that need to be installed and added to system variable before use. <br />

- 1)Go to wkhtmltopdf.org and click download on the top

- 2)	Based on your OS download the installer 
- 3)	Setting system variable for window
  - Go to this pc properties
  - click” advanced system settings”
  - click “Environment Variable”
  - Copy the “bin folder” path of wkhtmltopdf 
  - select the “path system variable” and click on edit
  - at the end of the path variables add “;” for separation and then paste the “bin folder path”
  -click ok

- 4) after this you can use the wkhtmltopdf software any where from the sytem
# Convert csv to html:
	Read the CSV using the pandas read_csv function and convert to html using the df.to_html(path) function
# Convert HTML to PDF:
	Then convert the HTML to PDF using the pdfkit library of python.
