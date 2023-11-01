import json
import uuid

GET_RAW_PATH = "/getPerson"
CREATE_RAW_PATH = "/createPerson"


def lambda_handler(event, context):
    print(event)
    if event['rawPath'] == GET_RAW_PATH:
        print("Start Request for GetPerson")
        personId = event['queryStringParameters']['personId']
        print(f"Request received with personID: {personId}")
        return ({"firstname": "Jason", "lastname": "Bourne",
                "email": "email@email.com"})

    elif event['rawPath'] == CREATE_RAW_PATH:
        print("Start request to CreatePerson")
        decodedEvent = json.loads(event['body'])
        firstName = decodedEvent['firstName']
        lastName = decodedEvent['lastName']
        email = decodedEvent['email']
        print(
            f"Received request with firstName: {firstName} lastName: {lastName} and email: {email}")
