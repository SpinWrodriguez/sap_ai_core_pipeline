from fastapi import FastAPI

from app.controllers.v2026r1.swing_controller import router as swing_router

app = FastAPI(title="Golf Swing Analyzer API", version="2026.R1")
app.include_router(swing_router)


@app.get("/")
def healthcheck() -> dict[str, str]:
    return {"status": "ok", "service": "golf-swing-analyzer"}
