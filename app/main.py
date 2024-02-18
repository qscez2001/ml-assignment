from fastapi import FastAPI, HTTPException
from models import Payload, TranslationResult, TranslatedRecord
from translation import translate

app = FastAPI()
    
@app.post("/translation", response_model=TranslationResult)
def translation(payload: Payload):
    translated_records = []
    payload = payload.payload
    records = payload.records
    for record in records:
        id = record.id
        text = record.text
    
        translated_text = translate(text, payload.fromLang, payload.toLang)
        translated_record = TranslatedRecord(id=id, text=translated_text)
        translated_records.append(translated_record)
    
    return TranslationResult(result=translated_records)
