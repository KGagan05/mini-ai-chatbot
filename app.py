from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from chatbot import get_response

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/chat", response_class=HTMLResponse)
def chat(request: Request, message: str = Form(...)):

    response = get_response(message)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "message": message,
        "response": response
    })