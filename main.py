from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse

app= FastAPI()
inprogress_orders = {}
@app.get('/')

async def handle_request(request: Request):
    # Retrieve the JSON data from the request
    payload = await request.json()

    # Extract the necessary information from the payload
    # based on the structure of the WebhookRequest from Dialogflow
    intent = payload['queryResult']['intent']['displayName']
    parameters = payload['queryResult']['parameters']
    output_contexts = payload['queryResult']['outputContexts']

    if intent == "track.order - context: ongoing-tracking":
        track_order(parameters)


def track_order(parameters: dict):
    order_id = parameters['number']

    if order_status:
        fulfillment_text = f"The order status for order id : {order_id} is :"
    else:
        fulfillment_text = (f"The order {order_id} is not found")
    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })
