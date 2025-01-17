from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.elevenlabs import ElevenLabsService
from manim_voiceover.services.gtts import GTTSService
from content import Content
from dotenv import load_dotenv
import os
from pathlib import Path
import argparse

class KanpurgatoryVideo(VoiceoverScene):
    content: Content
    def __init__(self):
        # Set assets directory before any other configuration
        project_root = Path(__file__).parent
        config.assets_dir = str(project_root / "assets")

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

        # Print asset directory location for debugging
        print(f"Assets directory: {config.get_dir('assets_dir')}")
        
        # Check if SVG exists
        svg_path = Path(config.get_dir('assets_dir')) / "progress-gradient.svg"
        print(f"Looking for SVG at: {svg_path}")
        print(f"SVG exists: {svg_path.exists()}")

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
                    voice_id="hyqpbxvsDwE0hQA0TcGB"
                )
            )

    def create_progress_bar(self):
        bar_height = 0.2
        bar_width = config.frame_width
        
        try:
            # Get absolute path to SVG file
            svg_path = os.path.abspath(os.path.join(
                config.get_dir('assets_dir'),
                "progress-gradient.svg"
            ))
            print(f"Loading SVG from absolute path: {svg_path}")
            
            # Verify file exists before attempting to load
            if not os.path.exists(svg_path):
                raise FileNotFoundError(f"SVG file not found at {svg_path}")
                
            # Load SVG with explicit settings
            gradient_bar = SVGMobject(
                file_name=svg_path,
                should_center=True,
                height=bar_height,
                width=bar_width,
                fill_opacity=1,
                stroke_width=0
            ).set_z_index(1)
            
            # Ensure the SVG loaded properly
            print(f"SVG loaded with dimensions: {gradient_bar.width} x {gradient_bar.height}")
            
            if gradient_bar.width == 0 or gradient_bar.height == 0:
                raise ValueError("SVG loaded with zero dimensions")
                
        except Exception as e:
            print(f"Error loading SVG: {e}")
            # Fall back to the simple three-rectangle version
            gradient_bar = VGroup()
            colors = ["#1E3D59", "#4B2D84", "#9B4DCA"]
            sections = len(colors)
            section_width = bar_width / sections
            
            for i, color in enumerate(colors):
                section = Rectangle(
                    width=section_width,
                    height=bar_height,
                    fill_color=color,
                    fill_opacity=1,
                    stroke_width=0
                ).move_to([
                    -bar_width/2 + section_width/2 + i*section_width,
                    0,
                    0
                ])
                gradient_bar.add(section)
        
        # Create black overlay
        black_bar = Rectangle(
            width=bar_width,
            height=bar_height,
            fill_color=BLACK,
            fill_opacity=1,
            stroke_width=0
        ).set_z_index(2)
        
        # Create group and position it
        bar_group = VGroup(gradient_bar, black_bar)
        bar_group.move_to([0, config.frame_height/2 - bar_height/2, 0])
        
        return bar_group

    def create_passage_counter(self):
        # Create counter text in top right
        return Text(
            f"{self.current_passage + 1} / {self.total_passages}",
            font_size=24,
            font="Spectral"
        ).to_edge(RIGHT, buff=0.5).to_edge(UP, buff=0.5)

    def create_text_block(self, text, opacity=1, margin=0.2):
        text_obj = Text(
            text,
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
            
            # Get black overlay bar for animation
            black_overlay = progress_bar[1]  # Second element is the black bar
            next_text = self.create_text_block(passage.display_text)
            
            with self.voiceover(text=passage.voice_text) as tracker:
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

                # Animate the black overlay shrinking to reveal gradient bar
                self.play(
                    black_overlay.animate.stretch_to_fit_width(0).align_to(progress_bar, RIGHT),
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