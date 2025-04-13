from api.server import app

# Optional - Entry point when deploying with render
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api.server:app", host="0.0.0.0", port=10000)
