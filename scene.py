from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.elevenlabs import ElevenLabsService
from manim_voiceover.services.gtts import GTTSService
from content import Content
from dotenv import load_dotenv
import os
import argparse

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
        # Load environment variables
        load_dotenv()

        # Check required voice service selection
        voice_service = os.getenv('VOICE_SERVICE')
        if not voice_service:
            raise ValueError("VOICE_SERVICE environment variable must be set to 'gtts' or 'elevenlabs'")
        
        voice_service = voice_service.lower()
        if voice_service not in ['gtts', 'elevenlabs']:
            raise ValueError("VOICE_SERVICE must be either 'gtts' or 'elevenlabs'")

        # Initialize speech service based on selection
        if voice_service == 'gtts':
            self.set_speech_service(GTTSService(lang="en", tld="com"))
        else:
            api_key = os.getenv('ELEVEN_API_KEY')
            if not api_key:
                raise ValueError("ELEVEN_API_KEY environment variable is required when using elevenlabs service")
            
            self.set_speech_service(
                ElevenLabsService(
                    api_key=api_key,
                    voice_id="nPczCjzI2devNBz1zQrb"  # Brian voice ID for testing
                )
            )


    def create_text_block(self, text, opacity=1, margin=0.2):
        # Transform display text
        display_text = text.replace("|||", "").replace("***", "")  # Remove all markers

        text_obj = Text(
            display_text,
            font="Spectral",
            font_size=56,  # Default base size that will scale automatically
            color=WHITE,
            weight="NORMAL",
            fill_opacity=opacity,
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
                run_time=0.5
            )
            self.wait(tracker.duration - 0.5)
            
        # Add pause before starting passages
        self.wait(1.0)

        current_text = None
        for passage in self.content.passages:
            next_text = self.create_text_block(passage.text)

            # Transform text for voice service
            voice_text = (passage.text
                         .replace("|||", " . . . ")  # Add pause for marker
                         .replace("...", " . . . ")  # Regular ellipsis handling
                         .replace("***", ' "" ')  # Add emphasis markers
            )
            with self.voiceover(text=voice_text) as tracker:
                # Quick fade transition at the start (0.5 seconds)
                if current_text is None:
                    self.play(
                        FadeOut(title, shift=UP),
                        FadeOut(subtitle, shift=UP),
                        FadeIn(next_text, shift=UP * 0.3),
                        run_time=0.5
                    )
                else:
                    self.play(
                        FadeOut(current_text, shift=UP * 0.3),
                        FadeIn(next_text, shift=UP * 0.3),
                        run_time=0.5
                    )

                # Wait for the voiceover to complete plus extra pause
                self.wait(tracker.duration - 0.5)
                # Add brief pause between passages
                self.wait(0.5)  # 0.5 second pause between passages

            current_text = next_text

        # Fade to black
        self.play(
            FadeOut(current_text, run_time=2)
        )


if __name__ == "__main__":
    # manim -pql scene.py KanpurgatoryVideo
    pass
