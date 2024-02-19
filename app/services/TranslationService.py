from schemas.TranslationSchema import Payload, TranslationResult, TranslatedRecord
from inferences import translation


class TranslationService:

    def __init__(self):
        pass

    def translate(self, payload: Payload) -> TranslationResult:
        translated_records = []
        payload = payload.payload
        records = payload.records
        for record in records:
            id = record.id
            text = record.text

            translated_text = translation.translate(
                text, payload.fromLang, payload.toLang)
            translated_record = TranslatedRecord(id=id, text=translated_text)
            translated_records.append(translated_record)

        return TranslationResult(result=translated_records)
