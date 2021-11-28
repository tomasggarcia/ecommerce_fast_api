from typing import Optional, List
from uuid import uuid4
from fastapi import FastAPI, APIRouter


from routes.users import user

app = FastAPI()


app.include_router(user)

@app.get('/health')
def health():
    return {"Status": "ok"}

