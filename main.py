import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse

from API.database import SessionLocal, engine
from API.Routers.user_routes import router_user
from API.Routers.lost_item_routes import items

app = FastAPI(title='Lost and found App', description='APIs for lost and found item', version='1.0')

app.include_router(router_user)
app.include_router(items)

@app.get('/')
async def home():
    return RedirectResponse(url="/docs/")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)