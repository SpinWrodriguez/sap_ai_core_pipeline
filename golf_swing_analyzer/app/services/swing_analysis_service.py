from app.dal.ai_inference_dal import AICoachDAL
from app.dal.feedback_repository import FeedbackRepository
from app.schemas.swing import SwingFeedback, SwingInput


class SwingAnalysisService:
    """Service layer orchestrating domain analysis and DAL-backed AI feedback."""

    def __init__(self, repository: FeedbackRepository, ai_coach_dal: AICoachDAL) -> None:
        self.repository = repository
        self.ai_coach_dal = ai_coach_dal

    def analyze(self, swing_input: SwingInput) -> SwingFeedback:
        benchmark = self.repository.get_benchmark(swing_input.club)

        speed_delta = swing_input.swing_speed - benchmark["swing_speed"]
        launch_delta = swing_input.launch_angle - benchmark["launch_angle"]
        face_delta = swing_input.face_angle - benchmark["face_angle"]

        consistency_penalty = int(
            min(
                100,
                abs(speed_delta) * 1.8 + abs(launch_delta) * 2.5 + abs(face_delta) * 6.0,
            )
        )
        consistency_score = max(0, 100 - consistency_penalty)

        feedback, recommendations, _prompt = self.ai_coach_dal.simulate_ai_call(
            swing_input=swing_input,
            benchmark=benchmark,
        )

        return SwingFeedback(
            feedback=feedback,
            consistency_score=consistency_score,
            recommendations=recommendations,
        )
