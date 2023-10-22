import requests


def filter_questions_data(questions_data: list):
    """
    Функция - фильтр для отбора необходимых полей
    :param questions_data: список вопросов, которые необходимо отфилтровать
    :return: отфильтрованные данные
    """
    filtered_data = [{"id": item["id"],
                      "question": item["question"],
                      "answer": item["answer"],
                      "created_at": item["created_at"],
                      "saved_at": None
                      }
                     for item in questions_data]
    return filtered_data


def get_questions(questions_num: int):
    url = f"https://jservice.io/api/random?count={questions_num}"
    response = requests.get(url)
    questions_data = response.json()
    filtered_data = filter_questions_data(questions_data)
    return filtered_data
