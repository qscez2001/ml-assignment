from typing import List
from pydantic import BaseModel


class Record(BaseModel):
    id: str
    text: str


class TranslationPayload(BaseModel):
    fromLang: str
    records: List[Record]
    toLang: str


class Payload(BaseModel):
    payload: TranslationPayload


class TranslatedRecord(BaseModel):
    id: str
    text: str


class TranslationResult(BaseModel):
    result: List[TranslatedRecord]
