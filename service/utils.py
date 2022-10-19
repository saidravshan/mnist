import numpy as np
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

import onnxruntime

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


def model(array):
    scaled = (np.array(array) / 255).astype(np.float32)
    inp = scaled.reshape(1, 28, 28)
    session = onnxruntime.InferenceSession('model.onnx', None)
    input_name = session.get_inputs()[0].name
    output_name = session.get_outputs()[0].name

    result, = session.run([output_name], {input_name: inp})
    predicted = result[0].argmax(0)
    return int(predicted)
