from fastapi import Body
from fastapi.responses import HTMLResponse

from type import Image
from utils import model, app


@app.get('/', response_class=HTMLResponse)
async def index():
    return open('templates/index.html', 'r').read()


@app.post('/predict')
async def predict(body: Image = Body()):
    return {"prediction": model(body.data)}
