__author__ = 'Fabrizio'
# Import the required Libraries
import urllib
import requests, sys, json

def goal(APIKey, ListID):
    print("Beginning the script now ....\n...\n")
    #try the below (For error handling)

    #############################################
    # Define Variables
    #############################################

    # Create new URL to make the call to Mailchimp and get back specific list data
    newURL = "https://us9.api.mailchimp.com/3.0/lists/" + ListID + "/members"
    print (newURL + '\n\n')

    # Define the base URL
    baseURL = newURL + "/"

    # Define blank Dictionary for the goals list
    GoalList = []
    goalListInJSON = []

    listName = getListName(ListID, APIKey)

    params = {
    'count': 5000
    }

    try:

        #Make the first call to get the response of the API call 'https://usX.api.mailchimp.com/3.0/lists/ListID/members'
        membersResponse = requests.get(newURL,params=params,auth=('APIuser', APIKey))


        for i, member in enumerate(membersResponse.json()["members"]):
            # print ("member Id : " + member["id"])
            # print ("member email address: " + member["email_address"])

            #make the API call for the currently selected user
            goalResponse = requests.get(baseURL + member["id"] + "/goals", auth=('APIuser', APIKey))
            print("---  Members processed = " + str(i + 1))
            # print member["email_client"]
            # print goalResponse.text

            #format the response in to JSON
            tet = goalResponse.json()

            # print member["email_client"]
            print member["merge_fields"]["FNAME"]
            # print "-=-=-=-=-=-=-=-=-=-=-=-=-="
            # print "-=-=-===============-=-=-="


            for j, goals in enumerate(goalResponse.json()["goals"]):
                appendMemberInfoToGoal(member["merge_fields"]["FNAME"],member["email_client"],member["email_address"], goals, goalListInJSON)

                NameOfGoal = goals['event']
                addToGoalList(NameOfGoal,GoalList)



        MasterJSON = ({'Full':goalListInJSON})

        # Write the Json data to a text file named "[listname].JSON" in the directory "."

        Overview = ({'Full':GoalList})

        #Build the JSON files then return the names of them to use in the runner
        return [buildJSONFile(listName, MasterJSON),buildJSONOverviewFile(listName,Overview)]
    except:
        e = sys.exc_info()[0]
        print ("Error: %s" % e)

    print ("\t" + str(GoalList))
    print ("The new JSON file")
    for items in goalListInJSON:
        print ('\t' + str(items["event"]))

    print ("\nRootcall Script finished")

# Get the name of ths list using the List ID that was provided
def getListName(ListID,APIKey):
    listName = "Not found"
    try:
        # Get the name of the list
        listDetails = requests.get("https://us9.api.mailchimp.com/3.0/lists/" + ListID, auth=('APIuser', APIKey))
        listName = listDetails.json()['name']
        print ('The list name is "' + str(listName) + '"')

    except:
        e = sys.exc_info()[0]
        print ("Error: %s" % e)
    return listName

#What the goals are and How many people clicked each goal
#This creates a dictionary with the key being the goal name and the index being the number of times triggered
def addToGoalList(GoalName,GoalList):

    flag = True

    if len(GoalList) == 0:
        GoalList.append({"Goal Name" : GoalName, "Times triggered": 1 })
    else:
        for j, items in enumerate(GoalList):

            if GoalName == items["Goal Name"]:
                # print ("in")

                a = GoalList[j]["Times triggered"]
                a = a + 1
                GoalList[j]["Times triggered"] = a
                # b = GoalList[j]["Times triggered"]
                flag = False
                break

        # If it is a new goal that hasn't been registered yet... Add it in.
        if flag:
            GoalList.append({"Goal Name": GoalName, "Times triggered": 1}.copy())

    # print (GoalList)

    return GoalList

    #Who clicked on what goal.

#Dump to a JSON file
def buildJSONFile(name,data):
    name = name + ".json"
    name = name.replace (" ", "_")
    with open(name, 'w') as outfile:
        (json.dump(data, outfile, sort_keys=False, indent=4, ensure_ascii=False))
    return name

#Build the new JSON file only containing goals etc...
def appendMemberInfoToGoal(name,client, email, goals, goalListInJSON):
    # append the email to the goal list
    # print (goals)
    # print (name)
    # print (client)
    goals["Email"] = email

    if not name:
        name = "Not Defined"
        goals["First Name"] = name
    else:
        goals["First Name"] = name

    if not client:
        client = "Not Defined"
        goals["Email Client"] = client
    else:
        goals["Email Client"] = client
    print (goals)
    #Append the goal (Containing the email field) to the goalListInJSON Master list
    goalListInJSON.append(goals)

    return goalListInJSON

#Dump to a JSON file
def buildJSONOverviewFile(name,data):
    print ("Dump to a JSON file")
    name = name + "Overview.json"
    name = name.replace (" ", "_")
    with open(name, 'w') as outfile:
        (json.dump(data, outfile, sort_keys=False, indent=4, ensure_ascii=False))
    return name


