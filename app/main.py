from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Feron Suite")


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Feron Suite</title>

        <style>

            body{
                font-family: Arial;
                background:#f2f5f8;
                margin:40px;
            }

            h1{
                color:#0B3D91;
            }

            .kaart{

                background:white;
                padding:20px;
                border-radius:10px;
                width:400px;
                box-shadow:0px 0px 10px lightgray;

            }

            ul{

                font-size:20px;

            }

        </style>

    </head>

    <body>

        <div class="kaart">

            <h1>⚡ Feron Suite</h1>

            <h2>Dashboard</h2>

            <ul>

                <li>👤 Klanten</li>

                <li>📁 Projecten</li>

                <li>🔋 ESS Calculator</li>

                <li>⚡ Meterkast Calculator</li>

                <li>📋 IBS Checklist</li>

                <li>🛠 Onderhoud</li>

            </ul>

        </div>

    </body>

    </html>

    """