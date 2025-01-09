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
        # Example script segments optimized for TikTok
        script = [
            {
                "text": "Did you know?",
                "duration": 1.5,
                "position": UP * 5,  # Position near top of vertical frame
                "style": "title"
            },
            {
                "text": "Here's something\ninteresting...",
                "duration": 2,
                "position": ORIGIN,  # Center of frame
                "style": "body"
            },
            {
                "text": "#learnontiktok",
                "duration": 1.5,
                "position": DOWN * 6,  # Position near bottom for hashtags
                "style": "hashtag"
            }
        ]

        # Define text styles for mobile viewing
        styles = {
            "title": {
                "font_size": 96,
                "color": "#FFFFFF",
                "weight": "BOLD"
            },
            "body": {
                "font_size": 72,
                "color": "#FFFFFF",
                "weight": "NORMAL"
            },
            "hashtag": {
                "font_size": 48,
                "color": "#00F5FF",  # Bright cyan for hashtags
                "weight": "NORMAL"
            }
        }

        # Create and animate each segment
        for segment in script:
            # Apply style based on segment type
            style = styles[segment["style"]]

            # Create text with mobile-optimized styling
            text = Text(
                segment["text"],
                font_size=style["font_size"],
                color=style["color"],
                weight=style["weight"]
            )
            text.move_to(segment["position"])

            # Create background for this segment
            background = self.create_mobile_background(segment["style"])

            # Animate sequence
            self.play(
                FadeIn(background),
                Write(text),
                run_time=0.5  # Faster animations for TikTok
            )
            self.wait(segment["duration"])
            self.play(
                FadeOut(background),
                Unwrite(text),
                run_time=0.3
            )

    def create_mobile_background(self, style):
        """Create backgrounds optimized for mobile viewing"""
        if style == "title":
            # Gradient background for titles
            background = VGroup()
            rect = Rectangle(
                width=config.frame_width,
                height=config.frame_height/3,
                fill_opacity=0.3,
                fill_color="#FF0080",  # Hot pink
                stroke_width=0
            ).move_to(UP * 5)
            # Add gradient overlay
            gradient = Rectangle(
                width=config.frame_width,
                height=config.frame_height/3,
                fill_opacity=0.4,
                stroke_width=0
            ).move_to(UP * 5)
            gradient.set_color_by_gradient(RED, BLUE)
            background.add(rect, gradient)
            return background
        elif style == "hashtag":
            # Subtle background for hashtags
            return Rectangle(
                width=config.frame_width,
                height=config.frame_height/4,
                fill_opacity=0.2,
                fill_color="#1D2B53",  # Dark blue
                stroke_width=0
            ).move_to(DOWN * 6)
        else:
            # Default background for body text
            return Rectangle(
                width=config.frame_width,
                height=config.frame_height/2,
                fill_opacity=0.25,
                fill_color="#2B2B2B",
                stroke_width=0
            )

class TikTokTransitions(Scene):
    """Additional class for TikTok-specific transitions"""
    def __init__(self):
        config.frame_width = 9.0
        config.frame_height = 16.0
        config.pixel_width = 1080
        config.pixel_height = 1920
        super().__init__()

    def construct(self):
        # Example of a trending TikTok-style text reveal
        text = Text("Trending\nTip!", font_size=120)
        text.arrange(DOWN, aligned_edge=LEFT)

        # Create individual letters for the text reveal effect
        letters = VGroup(*[Text(letter, font_size=120) for letter in "Trending"])
        letters.arrange(RIGHT, buff=0.1)
        letters.move_to(text[0])

        # Animate letters appearing with bounce effect
        for letter in letters:
            self.play(
                Create(letter),
                letter.animate.scale(1.2).shift(UP*0.5),
                run_time=0.15
            )
            self.play(
                letter.animate.scale(1/1.2).shift(DOWN*0.5),
                run_time=0.1
            )

        self.wait(0.5)

        # Quick fade out
        self.play(FadeOut(letters), run_time=0.3)

# Usage:
if __name__ == "__main__":
    # Command to render TikTok video:
    # manim -pql scene.py TikTokVideo
    # For transitions test:
    # manim -pql scene.py TikTokTransitions
    pass
