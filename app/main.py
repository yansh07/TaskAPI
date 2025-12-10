from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
# from uvicorn.middleware.proxy_headers import ProxyHeadersMiddleware

app = FastAPI(title="Task API")
# app.add_middleware(ProxyHeadersMiddleware, trusted_hosts=[*])

# STATIC FILES
app.mount("/static", StaticFiles(directory="static"), name="static")

# TEMPLATE FILES
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})