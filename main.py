from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates



app=FastAPI()

tpl  = Jinja2Templates(directory="./templates")
#static = app.mount("/static", StaticFiles(directory="./static"), name="static")



@app.get("/")
async def index(request: Request):
  return tpl.TemplateResponse("index.html",{"request":request})

