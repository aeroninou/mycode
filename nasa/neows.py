#!/usr/bin/python3
import requests

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# this function grabs our credentials
# it is easily recycled from our previous script
def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()
    
    startdate = ""
    while startdate == "":
        startdate = input("Enter Date YYYY-MM-DD? ")


    ## update the date below, if you like
    startdate = "start_date=" + startdate

    ## the value below is not being used in this
    ## version of the script

    enddate = input("End date? YYYY-MM-DD: ")
    enddate = "end_date=" + enddate

    urltolookup = f'{NEOURL}{startdate}&{nasacreds}'

    if enddate:
        urltolookup = f'{urltolookup}&{enddate}'

    # make a request with the request library
    neowrequest = requests.get(urltolookup)

    # strip off json attachment from our response
    neodata = neowrequest.json()

    ## display NASAs NEOW data
    print(neodata)

if __name__ == "__main__":
    main()

