from fastapi import FastAPI
from fastapi.responses import FileResponse

from .models import User, UserResponse, Feedback

app = FastAPI()


@app.get('/')
def index():
    return FileResponse("app/index.html")

@app.post('/calculate')
def new(num1: int, num2: int):
    return {"result": num1+num2}

@app.get('/users')
def user(user: User):
    return user

@app.post("/user", response_model=UserResponse)
def post_user(user: User):
    return {**user.dict(), "is_adult": user.age >= 18}

db = []

# bad_words = ["редиска", "бяка", "козявка"]

@app.post("/feedback")
def post_feedback(model: Feedback, is_premium: bool):
    result = "Ваш отзыв сохранён."
    if is_premium:
        result = "Ваш отзыв будет рассмотрен в приоритетном порядке"
    db.append({
        "name": model.name,
        "message": model.message,
    })
    return {
        "message": f"Спасибо, {model.name}! {result}"
    }
