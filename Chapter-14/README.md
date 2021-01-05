##### 1. What three files do you need for EZSheets to access Google Sheets?
Credentials file\
Token for Google Sheets\
Token for Google Drive

##### 2. What two types of objects does EZSheets have?
Spreadsheet and Sheet object

##### 3. How can you create an Excel file from a Google Sheet spreadsheet?
By using downloadAsExcel()

##### 4. How can you create a Google Sheet spreadsheet from an Excel file?
By using ezsheets.upload('demo.xlsx')

##### 5. The ss variable contains a Spreadsheet object. What code will read data from the cell B2 in a sheet titled “Students”?
```
ss['Students']['B2']
```

##### 6. How can you find the column letters for column 999?
```
ezsheets.getColumnLetterof(999)
```

##### 7. How can you find out how many rows and columns a sheet has?
sheet.rowCount\
sheet.columnCount

##### 8. How do you delete a spreadsheet? Is this deletion permanent?
```python
ss.delete() #not permanent delete
ss.delete(permanent=True)  # permanent delete
```

##### 9. What functions will create a new Spreadsheet object and a new Sheet object, respectively?
createSpreadsheet()\
createSheet()

##### 10. What will happen if, by making frequent read and write requests with EZSheets, you exceed your Google account’s quota?
Attempting to exceed this quota will raise the googleapiclient.errors.HttpError “Quota exceeded for quota group” exception.

