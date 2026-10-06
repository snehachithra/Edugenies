"""EduGenie - FastAPI application entry point.
Run with:  uvicorn main:app --reload
"""
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from qna import get_answer
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations

app = FastAPI(title="EduGenie", description="Gemini powered learning assistant")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request, "index.html")


@app.post("/qa")
async def qa(text: str = Form(...)):
    return JSONResponse({"result": get_answer(text)})


@app.post("/explain")
async def explain(text: str = Form(...)):
    from explanation_module import explain_concept  # lazy import: heavy model
    return JSONResponse({"result": explain_concept(text)})


@app.post("/quiz")
async def quiz(text: str = Form(...)):
    return JSONResponse({"result": generate_quiz(text)})


@app.post("/summarize")
async def summarize(text: str = Form(...)):
    return JSONResponse({"result": summarize_text(text)})


@app.post("/learn/recommendations")
async def recommendations(text: str = Form(...)):
    return JSONResponse({"result": get_learning_recommendations(text)})
