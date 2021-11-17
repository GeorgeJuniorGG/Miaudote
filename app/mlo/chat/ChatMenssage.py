from pydantic import BaseModel, Field,  validator
from datetime import datetime, timezone

def get_date():
    date = datetime.now(timezone.utc)
    return date

class ChatMessage(BaseModel):
    content: str
    sentBy: str
    sentAt: datetime = Field(default_factory = lambda: datetime.now(timezone.utc))

    # Exemplo de Validação
    # @validator('sentBy')
    # def message_must_be_sent_by_python(cls, user):
    #     if user != 'Python':
    #         raise ValueError(f'The user {user} is not Python!')
    #     return user
