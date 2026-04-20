from pydantic import BaseModel, Field


class SwingInput(BaseModel):
    club: str = Field(..., examples=["7-iron", "driver"])
    swing_speed: float = Field(..., gt=0, description="Swing speed in mph")
    launch_angle: float = Field(..., description="Launch angle in degrees")
    face_angle: float = Field(..., description="Face angle in degrees")


class SwingFeedback(BaseModel):
    feedback: str
    consistency_score: int = Field(..., ge=0, le=100)
    recommendations: list[str]
