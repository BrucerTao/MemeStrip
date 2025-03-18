from fastapi import FastAPI
from examples.game.test_agent import chaos_agent

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/doAgent")
def read_item():
    chaos_agent.compile()
    chaos_agent.run()
    return {"test"}