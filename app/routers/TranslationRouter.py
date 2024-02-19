from fastapi import APIRouter, Depends, status
from schemas.TranslationSchema import Payload, TranslationResult
from services.TranslationService import TranslationService

router = APIRouter()


@router.post(
    "/translation/",
    response_model=TranslationResult,
    status_code=status.HTTP_200_OK,
)
def translation(
        payload: Payload,
        translationService: TranslationService = Depends()):

    return translationService.translate(payload)
