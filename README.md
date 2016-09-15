# MailchimpGoalsToCsv
access the mailchimp API you can pull the goals out as a CSV file. 

###Writen in Python 2.7

## How to use
run `$~ __init__.py Mailchimp-APIKey ListID1 ListID2 ListID3 ..... ListIDx`

It outputs 2 CSV files for each list input:
  1. Overview of all goal triggered 
  2. Person specific data

## Requirements
The API Key should be on us14. (If you want to change this you need to change the code in   `rootcall.py`
Python 2.7
You must pass an API key in
You must pass at least 1 List ID in


Thanks to json2csv for the conversion : @evidens

https://github.com/evidens/json2csv

It is integrated as part of the program
