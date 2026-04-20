from fastapi import APIRouter, Depends

from app.dal.ai_inference_dal import AICoachDAL
from app.dal.feedback_repository import FeedbackRepository
from app.schemas.swing import SwingFeedback, SwingInput
from app.services.swing_analysis_service import SwingAnalysisService

router = APIRouter(prefix="/v2026R1", tags=["Golf Swing Analyzer v2026R1"])


def get_swing_analysis_service() -> SwingAnalysisService:
    repository = FeedbackRepository()
    ai_coach_dal = AICoachDAL()
    return SwingAnalysisService(repository, ai_coach_dal)


@router.post("/analyze-swing", response_model=SwingFeedback)
def analyze_swing(
    swing_input: SwingInput,
    service: SwingAnalysisService = Depends(get_swing_analysis_service),
) -> SwingFeedback:
    return service.analyze(swing_input)
