import torch
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from model import ModelV2

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


def predict(array):
    scaled = torch.tensor(array) / 255
    inp = scaled.reshape(1, 28, 28).unsqueeze(0)

    model = ModelV2(1, 10)
    model.load_state_dict(torch.load('model.pth'))
    model.eval()
    with torch.inference_mode():
        result = model(inp)
    predicted = result[0].argmax(0)
    return int(predicted)
