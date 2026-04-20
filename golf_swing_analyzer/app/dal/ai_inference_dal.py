from app.schemas.swing import SwingInput


class AICoachDAL:
    """DAL adapter that simulates an AI completion call using a prompt template."""

    PROMPT_TEMPLATE = """SYSTEM:
You are a golf performance coach running inside an enterprise AI pipeline.
Return concise, actionable coaching feedback.

CONTEXT:
- Club: {club}
- Swing speed (mph): {swing_speed}
- Launch angle (deg): {launch_angle}
- Face angle (deg): {face_angle}
- Benchmark speed (mph): {benchmark_speed}
- Benchmark launch angle (deg): {benchmark_launch_angle}

RULES:
1) If swing_speed < 90 -> suggest power improvement.
2) If face_angle is open (positive > 1.0) -> suggest grip/face control.
3) If launch_angle too high (>{high_launch_threshold}) -> suggest ball position adjustment.

OUTPUT FORMAT:
- summary: short paragraph
- recommendations: array of short bullets
"""

    def build_prompt(self, swing_input: SwingInput, benchmark: dict[str, float]) -> str:
        high_launch_threshold = max(benchmark["launch_angle"] + 3.0, 18.0)
        return self.PROMPT_TEMPLATE.format(
            club=swing_input.club,
            swing_speed=swing_input.swing_speed,
            launch_angle=swing_input.launch_angle,
            face_angle=swing_input.face_angle,
            benchmark_speed=benchmark["swing_speed"],
            benchmark_launch_angle=benchmark["launch_angle"],
            high_launch_threshold=high_launch_threshold,
        )

    def simulate_ai_call(
        self, swing_input: SwingInput, benchmark: dict[str, float]
    ) -> tuple[str, list[str], str]:
        """Simulated inference method, shaped for future SAP AI Core integration."""
        prompt = self.build_prompt(swing_input, benchmark)
        high_launch_threshold = max(benchmark["launch_angle"] + 3.0, 18.0)

        recommendations: list[str] = []

        if swing_input.swing_speed < 90:
            recommendations.append(
                "Power improvement: use stronger ground-force sequencing and faster hip rotation through impact."
            )
        else:
            recommendations.append("Power profile is strong; keep tempo stable for repeatable contact.")

        if swing_input.face_angle > 1.0:
            recommendations.append(
                "Face control: impact is open—slightly strengthen lead-hand grip and drill face-to-path awareness."
            )
        elif swing_input.face_angle < -1.0:
            recommendations.append(
                "Face control: impact is closed—reduce lead-hand tension and improve release timing."
            )
        else:
            recommendations.append("Face angle is neutral and controlled.")

        if swing_input.launch_angle > high_launch_threshold:
            recommendations.append(
                "Ball position adjustment: launch is high—move ball a fraction back to reduce delivered loft."
            )
        elif swing_input.launch_angle < benchmark["launch_angle"] - 3.0:
            recommendations.append(
                "Ball position adjustment: launch is low—move ball slightly forward and finish with chest up."
            )
        else:
            recommendations.append("Launch conditions are in a playable window.")

        summary = (
            f"Enterprise AI Coach ({swing_input.club}): speed={swing_input.swing_speed:.1f} mph, "
            f"launch={swing_input.launch_angle:.1f}°, face={swing_input.face_angle:.1f}°. "
            "Recommendations were generated from the enterprise prompt template and rule policy."
        )

        return summary, recommendations, prompt
