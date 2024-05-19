from fastapi import FastAPI
from app.api.routes.v3_1.v3_1 import v3_1_app  
import logging

logging.basicConfig(filename="Log",
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

logging.info("Running Urban Planning")

logger = logging.getLogger('__main__')

app = FastAPI()

app.mount(path="/api/v3_1",app=v3_1_app)

if __name__ == "__main__":
    logger.info("Starting Exection of Project")
    
    import uvicorn

    uvicorn.run("main:app",host="127.0.0.1",port=8000, reload=True)