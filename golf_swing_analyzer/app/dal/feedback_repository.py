class FeedbackRepository:
    """Data access layer for swing benchmarks and coaching snippets."""

    _club_benchmarks = {
        "driver": {"swing_speed": 100.0, "launch_angle": 12.0, "face_angle": 0.0},
        "3-wood": {"swing_speed": 92.0, "launch_angle": 13.0, "face_angle": 0.0},
        "5-iron": {"swing_speed": 86.0, "launch_angle": 16.0, "face_angle": 0.0},
        "7-iron": {"swing_speed": 80.0, "launch_angle": 18.0, "face_angle": 0.0},
        "pitching wedge": {"swing_speed": 72.0, "launch_angle": 24.0, "face_angle": 0.0},
    }

    def get_benchmark(self, club: str) -> dict[str, float]:
        normalized = club.strip().lower()
        return self._club_benchmarks.get(
            normalized,
            {"swing_speed": 85.0, "launch_angle": 17.0, "face_angle": 0.0},
        )
