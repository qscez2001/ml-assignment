from typing import List
from pydantic import BaseModel
from fastapi import FastAPI
# from translation_example import translate

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
    # print(payload)
    # payload = payload.payload
    # print(payload)
    # records = payload.records
    # for record in records:
    #     print(record.text)
        
        # record.text = translate(record.text, payload.fromLang, payload.toLang)
    translated_record = TranslatedRecord(id="123", text="人生はチョコレートの箱のようなものだ。")
    return TranslationResult(result=[translated_record])
    # return {"result": "人生はチョコレートの箱のようなものだ。"}
