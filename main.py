from fastapi import FastAPI


app = FastAPI()


@app.get('/index')
async def index() -> dict:
    return {'message': 'hello world'}