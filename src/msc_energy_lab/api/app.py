from fastapi import FastAPI

app = FastAPI(title="MSC Cruise Energy Lab API", version="0.1.0")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/version")
def version() -> dict:
    return {"version": "0.1.0"}
