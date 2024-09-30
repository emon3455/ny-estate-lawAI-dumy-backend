from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def getChatbotMessage(inputText: str):
  return "I have received your message this features is under build we will reach you soon"

@app.get("/")
def home():
    return JSONResponse("Object Detection Server Is Running")

@app.post("/message")
async def get_message_from_whatsapp_sms(request: Request):

    body = await request.json()

    return JSONResponse(content={"body": body})

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
