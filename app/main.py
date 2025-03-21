from fastapi import FastAPI
from fastapi.responses import FileResponse
from app.api import endpoints
from app import config
import uvicorn


app = FastAPI()

app.include_router(endpoints.router)


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=7777)