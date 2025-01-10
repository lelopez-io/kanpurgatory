from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
from content import Content

class KanpurgatoryVideo(VoiceoverScene):
    content: Content
    def __init__(self):
        # Vertical video configuration
        config.frame_width = 9.0
        config.frame_height = 16.0
        config.pixel_width = 1080
        config.pixel_height = 1920
        self.content = Content()
        super().__init__()
        self.set_speech_service(GTTSService(lang="en", tld="com"))

    def calculate_wait_time(self, text_content):
        """Calculate wait time based on text length and complexity"""
        # Base time of 2 seconds
        base_time = 2.2

        # Split into words (handling both spaces and newlines)
        words = [w for w in text_content.replace('\n', ' ').split(' ') if w.strip()]
        word_time = len(words) * 0.08

        # Count actual line breaks
        line_breaks = text_content.count('\n')
        break_time = line_breaks * 0.02

        total_time = min(base_time + word_time + break_time, 7.0)  # Cap at 7 seconds

        return total_time

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
        title = self.create_text_block(self.content.title)
        subtitle = self.create_text_block(self.content.subtitle)

        title.move_to(UP * 2)
        subtitle.next_to(title, DOWN, buff=0.5)

        with self.voiceover(text=self.content.title) as tracker:
            self.play(
                AddTextLetterByLetter(title),
                run_time=tracker.duration
            )

        with self.voiceover(text=self.content.subtitle) as tracker:
            self.play(
                FadeIn(subtitle, shift=UP * 0.3),
                run_time=tracker.duration
            )

        current_text = None
        for passage in self.content.passages:
            next_text = self.create_text_block(passage.text)

            with self.voiceover(text=passage.text) as tracker:
                if current_text is None:
                    # First passage - transition from title
                    self.play(
                        FadeOut(title, shift=UP),
                        FadeOut(subtitle, shift=UP),
                        FadeIn(next_text, shift=UP * 0.3),
                        run_time=tracker.duration
                    )
                elif passage.next is None:
                    # Last passage - slower transition
                    self.play(
                        FadeOut(current_text, shift=UP * 0.3),
                        FadeIn(next_text, shift=UP * 0.3),
                        run_time=tracker.duration
                    )
                else:
                    # Middle passages - normal fade transform
                    self.fade_transform(current_text, next_text)

            current_text = next_text

        # Fade to black
        self.play(
            FadeOut(current_text, run_time=2)
        )


if __name__ == "__main__":
    # manim -pql scene.py KanpurgatoryVideo
    pass
