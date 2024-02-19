from fastapi import FastAPI
from routers import TranslationRouter

app = FastAPI()

app.include_router(TranslationRouter.router)
