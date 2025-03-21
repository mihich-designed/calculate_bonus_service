from fastapi import FastAPI
from fastapi.responses import FileResponse
from app.api import endpoints
from app import config
import uvicorn, logging
#from .logging import configure_logging # Задел под логирование

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
log = logging.getLogger(__name__)

# configure_logging() # Конфигурация логирования

app = FastAPI()

app.include_router(endpoints.router)


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=7777)
    # log.info(f' [x] Started __main__')