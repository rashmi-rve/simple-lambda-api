import json


def lambda_handler(event, context):
    """
    This function runs every time someone calls our API.
    'event' contains details about the incoming HTTP request
    (like query parameters), and API Gateway passes it in automatically.
    """

    # Get the "name" query parameter from the URL, e.g. ?name=Riya
    # If no name is given, default to "Guest"
    query_params = event.get("queryStringParameters") or {}
    name = query_params.get("name", "Guest")

    # Build the message we want to send back
    message = f"Hello, {name}! Welcome to your first Lambda-powered API."

    # API Gateway expects a response in this exact shape
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "message": message
        })
    }
