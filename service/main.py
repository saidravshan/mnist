from fastapi import Body
from fastapi.responses import HTMLResponse

from type import Image
from utils import predict, app


@app.get('/', response_class=HTMLResponse)
async def index():
    return open('templates/index.html', 'r').read()


@app.post('/predict')
async def prediction(body: Image = Body()):
    return {"prediction": predict(body.data)}
