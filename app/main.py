from fastapi import FastAPI


from config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    # openapi_url=f"{settings.API_V1_STR}/openapi.json",
)


@app.get("/")
def health():
    return {"msg": "Hello World!"}