from fastapi import FastAPI
from settings import settings
from api import router
from fastapp.api.auth import router as auth_router

app = FastAPI()
app.include_router(router)
app.include_router(auth_router)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app:app",
        host=settings.server_host,
        port=settings.server_port,
        reload=True,
    )