from datetime import datetime
from pydantic import BaseModel, errors, Field, field_validator, EmailStr
from typing import Optional
import re

# Создаём модель данных, которая обычно располагается в файле models.py
class User(BaseModel):
    name: str
    age: int


class UserResponse(User):
    is_adult: bool | None = None

class Contact(BaseModel):
    email: EmailStr
    phone: str = Field(
        None,
        pattern=r"^\d{7,15}$",
        description="Опциональный телефон (только цифры, 7-15 символов)"
    )

class Feedback(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    message: str = Field(..., min_length=10, max_length=500)
    contact: Contact  # Вложенная модель

    @field_validator('message')
    def validate_message(cls, message):
        # Недопустимые слова
        bad_words = ["редиска", "бяка", "козявка"]

        # Создаем регулярное выражение для проверки наличия слов в разных падежах
        pattern = r'\b(?:' + '|'.join(w[:-1] for w in bad_words) + '(а|и|е|у|ой|ою)' + r')\w*\b'

        if re.search(pattern, message, re.IGNORECASE):
            raise ValueError(f'Использование недопустимых слов.')

        return message
