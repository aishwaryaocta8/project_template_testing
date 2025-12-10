"""FastAPI application."""

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI(title="LLM Application API")

# class PromptRequest(BaseModel):
#     text: str

# class PromptResponse(BaseModel):
#     response: str

# @app.post("/generate", response_model=PromptResponse)
# async def generate_response(request: PromptRequest):
#     """Generate LLM response for given prompt."""
#     from pipeline import run_pipeline
#     response = run_pipeline(request.text)
#     return PromptResponse(response=response)

# @app.get("/health")
# async def health_check():
#     """Health check endpoint."""
#     return {"status": "healthy"}

