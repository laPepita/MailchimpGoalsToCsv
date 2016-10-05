# MailchimpGoalsToCsv
accesses the mailchimp API and pulls user's goals out from a list and outputs them as a CSV file. 

###Works with Python 3.5.2 (But should work with all Python 3.X)

## How to use
On Windows with Python already installed
- open `CMD`
- Navigate to the correct directory
- run `$~ python __init__.py Mailchimp-APIKey ListID1 ListID2 ListID3 ..... ListIDx`
- The files will be output in the folder location `..` from where you call the script.

It outputs 2 CSV files for each list input:
  1. Overview of all goal triggered 
  2. Person specific data

## Requirements
The API Key should be on us14. (If you want to change this you need to change the code in   `rootcall.py`
Python 3.X
You must pass an API key in
You must pass at least 1 List ID in


Thanks to json2csv for the conversion : @evidens

https://github.com/evidens/json2csv

It is integrated as part of the program
