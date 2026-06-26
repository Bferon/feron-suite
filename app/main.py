from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Feron Suite")


@app.get("/", response_class=HTMLResponse)
def dashboard():
    with open("app/templates/dashboard.html", "r", encoding="utf-8") as f:
        return f.read()