from dataclasses import dataclass
from typing import Optional, Tuple
from audio import AudioGenerator

@dataclass
class Passage:
    text: str
    audio_file: str
    next: Optional['Passage'] = None

@dataclass
class Content:
    title: str = "Kanpurgatory:"
    subtitle: str = "Field Notes from the In-Between"
    story: tuple[tuple[str, ...], ...] = (
        (
            "The endless horizon stretches",
            "before me like judgment day",
            "itself - flat, unforgiving,",
            "eternal."
        ),
        (
            "What should have been a",
            "single day's passage through",
            "Kansas, transformed into a",
            "four-day sentence in",
            "winter's prison."
        ),
        (
            "Here in this liminal space,",
            "where heaven meets earth",
            "in a razor-thin line,",
            "I discovered that purgatory",
            "isn't just a theological concept",
            "- it's a state of being."
        ),
        (
            "Not quite damnation,",
            "not quite salvation.",
            "",
            "Just... Kansas."
        )
    )
    passages: tuple[Passage, ...] = None

    def __post_init__(self):
        audio_gen = AudioGenerator()
        tones = audio_gen.generate_passage_tones(len(self.story))
        
        self.passages = tuple(
            Passage(
                "\n".join(lines),
                audio_file=tone,
                next=None if i == len(self.story) - 1 else Passage(
                    "\n".join(self.story[i + 1]),
                    audio_file=tones[i + 1]
                )
            )
            for i, (lines, tone) in enumerate(zip(self.story, tones))
        )
