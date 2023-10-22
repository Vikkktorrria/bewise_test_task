from fastapi import FastAPI
from database import Session, Question
from schemas import QuestionRequest
from helpers import get_questions
from datetime import datetime

app = FastAPI()


@app.post("/questions/")
def get_question(questions_request: QuestionRequest):
    last_added_question = Session().query(Question).order_by(Question.saved_at.desc()).first()

    questions_list = get_questions(questions_request.questions_num)
    # Проверка наличия идентификатора в таблице "question"
    for quest in questions_list:
        while Session().query(Question).filter_by(id=quest["id"]).first():
            quest = get_questions(1)[0]
        quest["saved_at"] = datetime.now()
        question_object = Question(**quest)
        cur_session = Session()
        cur_session.add(question_object)
        cur_session.commit()

    return last_added_question or {}
