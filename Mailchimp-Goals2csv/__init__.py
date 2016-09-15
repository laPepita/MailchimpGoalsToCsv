import RootCall
import subprocess
import sys
import os
import shutil
import time
#!/usr/bin/python

# ********
# How to call this function from the command line:
# ********
#
# 1. From the correct directory call __init__.py
# 2. Make sure the first parameter is the API key
#     a. The API key must be 37 characters long
# 3. All other parameters after that should be the List ID's' \
#                                                         '' \
# For example:
#     __init__.py 5b4bcc3a087b70803401ddddf4da05d1-us14 6564931f32 6567931f32 6564931f52 6564931h32
# will use the API Key 5b4bcc3a087b70803401ddddf4da05d1-us14 and get the goals for the 4 lists provided.


def main():
    # print command line arguments

    #If no arguments were entered
    if len(sys.argv) == 1:
        APIKey = raw_input("Enter API Key : ")
        arg = raw_input("Enter List Id : ")
        try:
            # # Call the goal method and pass in the API key and the list ID number
            names = RootCall.goal(APIKey, arg)
            # names[0] = Name of the member specific JSON file
            # names[1] = Name of the overview data

            ##############################
            # Trigger the Json 2 CSV maker
            ##############################
            # Build the CSV file for the member specific data
            subprocess.call(['python', 'Json2csv-master/json2csv.py', names[0], "master.outline.json"])

            # Build the CSV file for the Goal overview data
            subprocess.call(['python', 'Json2csv-master/json2csv.py', names[1], "masterOverview.outline.json"])
        except:
            e = sys.exc_info()[0]
            print ("Error: %s" % e)
            print "LIST ID is not valid for this Argument....."

        exit()

    if len(sys.argv[1]) == 37:
        APIKey = sys.argv[1]
        print "API Key set"
    else:
        print "#"*100
        print "ERROR"
        print "The API Key was not 37 characters long or not in the first parameter...."
        print "This will cause the program to fail... please supply the API key correctly"
        print "\n**Please supply in this format:\n\t Function APIKey ListID1 ListID2 ListID...\n An example:\n\t__init__.py 5b4bcc3a087b70803401ddddf4da05d1-us14 6564931f32 6567931f32"
        print "ERROR"
        print "#" * 100
        exit()

    current = " " + str(time.strftime("%c")).replace('/','-')
    current = current.replace(':', '')

    path = "../GoalCSVFolder" + current
    if not os.path.exists(path):
        os.makedirs(path)

    path = "../GoalJSONFolder" + current
    if not os.path.exists(path):
        os.makedirs(path)


    for arg in sys.argv[2:]:
        print arg
        if len(arg) > 8 & len(arg) < 12:
            try:
                # # Call the goal method and pass in the API key and the list ID number
                names = RootCall.goal(APIKey, arg)
                # names[0] = Name of the member specific JSON file
                # names[1] = Name of the overview data

                ##############################
                # Trigger the Json 2 CSV maker
                ##############################

                #Change Directory to output folder

                # Build the CSV file for the member specific data
                subprocess.call(['python', 'Json2csv-master/json2csv.py', names[0], "master.outline.json"])

                try:
                    shutil.move(names[0],"../GoalJSONFolder" + current)
                    a = names[0].rstrip(names[0][-4:])
                    shutil.move(a + "csv","../GoalCSVFolder" + current)
                except:
                    print " Files could not be replaced... There are already files existing with the same name... Please move or delete them"

                # Build the CSV file for the Goal overview data
                subprocess.call(['python', 'Json2csv-master/json2csv.py', names[1], "masterOverview.outline.json"])

                try:
                    shutil.move(names[1], "../GoalJSONFolder" + current)
                    a = names[1].rstrip(names[0][-4:])
                    shutil.move(a + "csv", "../GoalCSVFolder" +  current)
                except:
                    print " Files could not be replaced... There are already files existing with the same name... Please move or delete them"
            except:
                e = sys.exc_info()[0]
                print ("Error: %s" % e)
                print "LIST ID is not valid for this Argument....."

    print "\nFull function is done running"
    pass

if __name__ == "__main__":
    main()
