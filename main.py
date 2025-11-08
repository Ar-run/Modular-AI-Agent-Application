from fastapi import FastAPI

app = FastAPI(name="multi-model-application")

@app.get("/health")

async def health_check():
    return {"status" : "website is healthy"}

def main():
    print("Hello from multi-model-application!")


if __name__ == "__main__":
    main()
