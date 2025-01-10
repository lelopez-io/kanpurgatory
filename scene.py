from manim import *

class KanpurgatoryVideo(Scene):
    def __init__(self):
        # Vertical video configuration
        config.frame_width = 9.0
        config.frame_height = 16.0
        config.pixel_width = 1080
        config.pixel_height = 1920
        super().__init__()

    def create_text_block(self, text, opacity=1, margin=0.2):
        text_obj = Text(
            text,
            font="Spectral",
            font_size=56,  # Default base size that will scale automatically
            color=WHITE,
            weight="NORMAL",
            opacity=opacity,
            line_spacing=1.2  # Increased line spacing for readability
        )

        # Get frame dimensions with custom margin
        frame_width = config.frame_width * (1 - margin)
        frame_height = config.frame_height * (1 - margin)

        # Scale down if text is too large
        if text_obj.width > frame_width or text_obj.height > frame_height:
            scale_factor_w = frame_width / text_obj.width
            scale_factor_h = frame_height / text_obj.height
            scale_factor = min(scale_factor_w, scale_factor_h)
            text_obj.scale(scale_factor)

        return text_obj

    def fade_transform(self, old_text, new_text):
        """Smooth transition between text blocks"""
        self.play(
            FadeOut(old_text, shift=UP * 0.3, run_time=1),
            FadeIn(new_text, shift=UP * 0.3, run_time=1)
        )

    def construct(self):
        # Set background color
        self.camera.background_color = BLACK

        # Title sequence
        title = self.create_text_block("Kanpurgatory:")
        subtitle = self.create_text_block("Field Notes from the In-Between")

        title.move_to(UP * 2)
        subtitle.next_to(title, DOWN, buff=0.5)

        # Fade in title with letter reveal
        self.play(
            AddTextLetterByLetter(title, run_time=2),
            rate_func=linear
        )
        self.play(
            FadeIn(subtitle, shift=UP * 0.3),
            run_time=1.5
        )
        self.wait(2)

        # Opening paragraph
        opening = self.create_text_block(
            "The endless horizon stretches\nbefore me like judgment day\nitself - flat, unforgiving,\neternal."
        )

        # Transition from title to first text
        self.play(
            FadeOut(title, shift=UP),
            FadeOut(subtitle, shift=UP),
            FadeIn(opening, shift=UP * 0.3),
            run_time=1.5
        )
        self.wait(3)

        # First passage
        text1 = self.create_text_block(
            "What should have been a\nsingle day's passage through\nKansas, transformed into a\nfour-day sentence in\nwinter's prison."
        )

        # Gentle fade between texts
        self.fade_transform(opening, text1)
        self.wait(3)

        # Second passage with thematic emphasis
        text2 = self.create_text_block(
            "Here in this liminal space,\nwhere heaven meets earth\nin a razor-thin line,\nI discovered that purgatory\nisn't just a theological concept\n- it's a state of being."
        )

        self.fade_transform(text1, text2)
        self.wait(3)

        # Final contemplative line
        text3 = self.create_text_block(
            "Not quite damnation,\nnot quite salvation.\n\nJust... Kansas."
        )

        # Slower, more dramatic transition for the final revelation
        self.play(
            FadeOut(text2, shift=UP * 0.3, run_time=1.5),
            FadeIn(text3, shift=UP * 0.3, run_time=1.5)
        )
        self.wait(3)

        # Fade to black
        self.play(
            FadeOut(text3, run_time=2)
        )
        self.wait(1)

# Alternative version with different animation style
class KanpurgatoryAlt(Scene):
    def __init__(self):
        # Vertical video configuration
        config.frame_width = 9.0
        config.frame_height = 16.0
        config.pixel_width = 1080
        config.pixel_height = 1920
        super().__init__()

    def construct(self):
        self.camera.background_color = BLACK

        def create_text(text, size=56):
            return Text(
                text,
                font="Spectral",
                font_size=size,
                color=WHITE,
                weight="NORMAL",
                line_spacing=1.2
            )

        # Reveal text with a gentle typewriter effect and subtle scaling
        def reveal_text(text_obj):
            self.play(
                AddTextLetterByLetter(text_obj, time_per_char=0.05),
                text_obj.animate.scale(1.02),
                run_time=2
            )
            self.play(
                text_obj.animate.scale(1/1.02),
                run_time=0.5
            )

        # Create your scenes here with alternate animation style
        title = create_text("Kanpurgatory", size=72)
        reveal_text(title)
        self.wait(1)

# Usage:
if __name__ == "__main__":
    # For main version:
    # manim -pql scene.py KanpurgatoryVideo
    # For alternative style:
    # manim -pql scene.py KanpurgatoryAlt
    pass
