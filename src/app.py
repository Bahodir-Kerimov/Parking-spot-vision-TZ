from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(title="Parking Spot Vision API", version="0.1.0")

@app.get("/api/v1/health")
def health():
    return JSONResponse({"status": "ok"})
