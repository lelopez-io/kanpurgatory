from manim import *

class TikTokVideo(Scene):
    def __init__(self):
        # Configure for vertical video (9:16 aspect ratio)
        config.frame_width = 9.0
        config.frame_height = 16.0
        config.pixel_width = 1080
        config.pixel_height = 1920
        super().__init__()

    def construct(self):
        self.camera.background_color = BLACK

        # Example script segments with Spectral font
        script = [
            {
                "text": "Did you know?",
                "duration": 1.5,
                "position": UP * 5,
                "font_size": 96
            },
            {
                "text": "Here's something\ninteresting...",
                "duration": 2,
                "position": ORIGIN,
                "font_size": 72
            },
            {
                "text": "#learnontiktok",
                "duration": 1.5,
                "position": DOWN * 6,
                "font_size": 48
            }
        ]

        # Create and animate each segment
        for segment in script:
            # Create text with Spectral font
            text = Text(
                segment["text"],
                font="Spectral",  # Using the working font family name
                font_size=segment["font_size"],
                color=WHITE
            ).move_to(segment["position"])

            # Optional: Add slight shadow for better readability
            # Using a more subtle shadow for the elegant Spectral font
            text_shadow = text.copy().set_color(BLACK).set_opacity(0.3)
            text_shadow.shift(RIGHT * 0.015 + DOWN * 0.015)  # Smaller offset

            # Animate sequence
            self.play(
                FadeIn(text_shadow, run_time=0.3),
                FadeIn(text, run_time=0.3)
            )
            self.wait(segment["duration"])
            self.play(
                FadeOut(text_shadow, run_time=0.2),
                FadeOut(text, run_time=0.2)
            )

# Additional class for testing different text animations with Spectral
class TextAnimations(Scene):
    def __init__(self):
        config.frame_width = 9.0
        config.frame_height = 16.0
        config.pixel_width = 1080
        config.pixel_height = 1920
        super().__init__()

    def construct(self):
        self.camera.background_color = BLACK

        # Gentle fade up from bottom
        text1 = Text(
            "Fade from below",
            font="Spectral",
            font_size=72,
            color=WHITE
        ).move_to(UP * 2)

        self.play(
            FadeIn(text1, shift=UP * 0.5),
            run_time=0.8
        )

        # Letter by letter reveal
        text2 = Text(
            "Letter by letter",
            font="Spectral",
            font_size=72,
            color=WHITE
        )

        self.play(
            AddTextLetterByLetter(text2),
            run_time=1.5
        )

        # Scale reveal
        text3 = Text(
            "Scale reveal",
            font="Spectral",
            font_size=72,
            color=WHITE
        ).move_to(DOWN * 2)

        self.play(
            Create(text3, scale=1.2),
            run_time=1
        )

        self.wait(2)

# Usage:
if __name__ == "__main__":
    # For main video:
    # manim -pql scene.py TikTokVideo
    # For animation examples:
    # manim -pql scene.py TextAnimations
    pass
