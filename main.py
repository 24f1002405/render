from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    with open('data', 'r') as f:
        msg = f.read()
    return {'msg': msg}