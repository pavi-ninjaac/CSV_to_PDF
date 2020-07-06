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

![Screenshot (129)](https://user-images.githubusercontent.com/51699297/86623199-c4958680-bfde-11ea-8ef5-e05c29eefb62.png)
- 2)	Based on your OS download the installer 
- 3)	Setting system variable for window
  - Go to this pc properties
  - click” advanced system settings”
![Screenshot (130)](https://user-images.githubusercontent.com/51699297/86623217-ccedc180-bfde-11ea-9ff4-5a03ed58015f.png)
  - click “Environment Variable”
![Screenshot (132)](https://user-images.githubusercontent.com/51699297/86623223-d119df00-bfde-11ea-9292-8497b3521e62.png)  
  - Copy the “bin folder” path of wkhtmltopdf 
![Screenshot (141)](https://user-images.githubusercontent.com/51699297/86623259-e42caf00-bfde-11ea-938c-68c6c7131a4d.png)
  - select the “path system variable” and click on edit
![Screenshot (140)](https://user-images.githubusercontent.com/51699297/86623246-dd9e3780-bfde-11ea-9b3f-513b07338e19.png)
  - at the end of the path variables add “;” for separation and then paste the “bin folder path”
![Screenshot (139)](https://user-images.githubusercontent.com/51699297/86623234-d7a85680-bfde-11ea-8416-83b4cc05d400.png)  
  -click ok

- 4) after this you can use the wkhtmltopdf software any where from the sytem
# Convert csv to html:
	Read the CSV using the pandas read_csv function and convert to html using the df.to_html(path) function
# Convert HTML to PDF:
	Then convert the HTML to PDF using the pdfkit library of python.
