from pydantic import BaseModel


class QuestionRequest(BaseModel):
    """аннотация типов при запросе количества вопросов"""
    questions_num: int

    class Config:
        from_attributes = True

