import requests
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class MessageRequest(BaseModel):
    firstName: str
    lastName: str
    email: str
    phone: str
    smsBody: str
    sessionId: str
    modality: str

class EmailMessageRequest(BaseModel):
    firstName: str
    lastName: str
    email: str
    phone: str
    emailBody: str
    sessionId: str
    modality: str

def getChatbotMessage(inputText: str):
  return "I have received your message this features is under build we will reach you soon"

@app.get("/")
async def home():
    return JSONResponse("NY Estate Law.ai Server Is Running")

@app.post("/testBody")
async def get_body(request: Request):
    body = await request.json()
    return JSONResponse(content=body)

@app.post("/message")
async def get_message_from_whatsapp_sms(request: MessageRequest):

    sanitized_phone = request.phone.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
    chatbot_reply = getChatbotMessage(request.smsBody)

    post_data = {
        "firstName": request.firstName,
        "lastName": request.lastName,
        "phone": sanitized_phone,
        "email": request.email,
        "smsBody": chatbot_reply,
        "sessionId": request.sessionId,
        "modality": request.modality,
    }

    if(request.modality=="Whatsapp"):
      webhook_url = "https://services.leadconnectorhq.com/hooks/HdpmQEFcOyjCw9DFaIyF/webhook-trigger/9a029568-6db2-4a58-a5b5-d6fdd3e26bf8"
      response = requests.post(webhook_url, json=post_data)
      if response.status_code == 200:
        return JSONResponse(content={"status": "whatsapp message sent successfully!"})
      else:
        raise HTTPException(status_code=response.status_code, detail="Failed to send whatsapp message")


    elif(request.modality=="SMS"):
      webhook_url = "https://services.leadconnectorhq.com/hooks/HdpmQEFcOyjCw9DFaIyF/webhook-trigger/4f73a1ec-239a-499e-849e-44a8a6dd6ded"
      response = requests.post(webhook_url, json=post_data)
      if response.status_code == 200:
        return JSONResponse(content={"status": "sms sent successfully!"})
      else:
        raise HTTPException(status_code=response.status_code, detail="Failed to send sms")

@app.post("/email")
async def get_email_message(request: EmailMessageRequest):

    sanitized_phone = request.phone.replace(" ", "").replace("-", "")
    chatbot_reply = getChatbotMessage(request.emailBody)

    post_data = {
        "firstName": request.firstName,
        "lastName": request.lastName,
        "phone": sanitized_phone,
        "email": request.email,
        "emailBody": chatbot_reply,
        "sessionId": request.sessionId,
        "modality": request.modality,
    }

    webhook_url = "https://services.leadconnectorhq.com/hooks/HdpmQEFcOyjCw9DFaIyF/webhook-trigger/4c5c9280-32eb-45c7-8dc0-e40870005eb6"
    response = requests.post(webhook_url, json=post_data)
    if response.status_code == 200:
        return JSONResponse(content={"status": "Email sent successfully!"})
    else:
        raise HTTPException(status_code=response.status_code, detail="Failed to send Email")

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)
