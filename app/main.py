from typing import List
from pydantic import BaseModel
from fastapi import FastAPI
from translation_example import translate

app = FastAPI()

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
    
@app.post("/translation", response_model=TranslationResult)
def translation(payload: Payload):
    translated_records = []
    payload = payload.payload
    records = payload.records
    for record in records:
        id = record.id
        text = record.text
    
        translated_text = translate(text, payload.fromLang, payload.toLang)
        translated_record = TranslatedRecord(id="123", text=translated_text)
        translated_records.append(translated_record)
    
    return TranslationResult(result=translated_records)
