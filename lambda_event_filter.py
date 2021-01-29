import boto3
import json
import logging
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)
 
# load cloudtrail eventname allowed list
configPath = os.environ['LAMBDA_TASK_ROOT'] + "/allowed_events.txt"
configContents = open(configPath).read()

ALLOWED_APIS = configContents

BLOCKED_APIS = ["ConsoleLogin"]
ALLOWED_CATEGORIES = ["Management"]


def evaluate_compliance(event):
    event_name = event["detail"]["eventName"]
    event_category = event["detail"]["eventCategory"]
    
    # clean the source ip address from the logs
    del event["detail"]["sourceIPAddress"]
    
    if event_name in BLOCKED_APIS:
        print("EventName is on the BLOCKED list:", event_name, ".")
        
    elif event_name in ALLOWED_APIS and event_category in ALLOWED_CATEGORIES:
        
        return  event
        
    else:
        print("EventName is NOT on the allowed list:", event_name, ".")


def lambda_handler(event, context):
    
    clean_log = evaluate_compliance(event)
    logger.info(clean_log)
