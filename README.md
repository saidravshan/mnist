# Handwritten Digits Recognition Neural Network with PyTorch

-------

## Technical stack
- PyTorch
- FastAPI
- NumPy 
- ONNX
- Docker


You can find Docker image [here](https://hub.docker.com/r/greentag/mnist).


## Running via docker

Make sure you already installed [docker](https://docker.com) on your machine and run:
```commandline
docker run -d -p 80:80 greentag/mnist
```
Now user interface is available on http://localhost.


## Running without docker
Go to `service` folder and run (first time):
```commandline
pip install -r requirements.txt
```

Then:
```commandline
uvicorn main:app --reload  
```
Check http://localhost:8000 

## API / Documentation
After running docker image, API documentation will be available on http://localhost/docs

