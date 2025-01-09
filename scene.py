from manim import *
import manimpango
from pathlib import Path

# First register the font
FONT_PATH = "/Users/lelopez/Library/Fonts/Spectral-ExtraLight.ttf"
try:
    manimpango.register_font(FONT_PATH)
    print(f"Successfully registered font from {FONT_PATH}")
except Exception as e:
    print(f"Error registering font: {e}")

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

        # Print available fonts to debug
        print("\nAvailable fonts after registration:")
        for font in manimpango.list_fonts():
            print(f"- {font}")

        # Test text with different font specifications
        test_texts = [
            {"text": "Test 1 - Direct Path", "font": FONT_PATH},
            {"text": "Test 2 - Font Family", "font": "Spectral"},
            {"text": "Test 3 - Full Name", "font": "Spectral ExtraLight"},
            {"text": "Test 4 - Hyphenated", "font": "Spectral-ExtraLight"}
        ]

        current_pos = 3
        for test in test_texts:
            try:
                text = Text(
                    test["text"],
                    font=test["font"],
                    font_size=48,
                    color=WHITE
                ).move_to(UP * current_pos)

                print(f"\nSuccessfully created text with font: {test['font']}")

                # Create and display the text
                self.play(
                    Write(text),
                    run_time=1
                )

            except Exception as e:
                print(f"Failed to create text with font {test['font']}: {e}")

            current_pos -= 2

        self.wait(2)

# Usage:
if __name__ == "__main__":
    # manim -pql scene.py TikTokVideo
    pass
