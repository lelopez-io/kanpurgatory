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
        self.total_passages = len(self.content.passages)
        self.current_passage = 0
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


    def create_progress_bar(self):
        # Create progress bar at the very top
        bar_height = 0.1
        
        # Background bar
        bg = Rectangle(
            width=config.frame_width,
            height=bar_height,
            fill_color=BLACK,
            fill_opacity=1,
            stroke_width=0
        ).to_edge(UP, buff=0)
        
        # Progress fill
        fill = Rectangle(
            width=0,
            height=bar_height,
            fill_color="#2B7CD4",
            fill_opacity=1,
            stroke_width=0
        ).to_edge(UP, buff=0).to_edge(LEFT, buff=0)
        
        return VGroup(bg, fill)
    
    def create_passage_counter(self):
        # Create counter text in top right
        return Text(
            f"{self.current_passage + 1} / {self.total_passages}",
            font_size=24,
            font="Spectral"
        ).to_edge(RIGHT, buff=0.5).to_edge(UP, buff=0.5)

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
        progress_group = None
        
        for passage in self.content.passages:
            # Update progress elements
            if 'progress_bar' in locals():
                self.remove(progress_bar)
            if 'passage_counter' in locals():
                self.remove(passage_counter)
                
            progress_bar = self.create_progress_bar()
            passage_counter = self.create_passage_counter()
            
            self.add(progress_bar)
            self.add(passage_counter)
            
            # Get progress fill for animation
            progress_fill = progress_bar[1]
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

                # Animate the progress bar filling
                bar_width = config.frame_width
                progress_fill.set_width(0)  # Reset width
                self.play(
                    progress_fill.animate.set_width(bar_width),
                    rate_func=linear,
                    run_time=tracker.duration - 0.5
                )
                
                # Add brief pause between passages
                self.wait(0.5)  # 0.5 second pause between passages
                
                # Update passage counter for next iteration
                self.current_passage += 1

            current_text = next_text

        # Fade to black
        self.play(
            FadeOut(current_text, run_time=2)
        )


if __name__ == "__main__":
    # manim -pql scene.py KanpurgatoryVideo
    pass
