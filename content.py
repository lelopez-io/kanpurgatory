from dataclasses import dataclass
from typing import Optional

@dataclass
class Passage:
    text: str
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
    passages: tuple[Passage, ...] = tuple(
        Passage(
            "\n".join(lines),
            next=None if i == len(story) - 1 else Passage("\n".join(story[i + 1]))
        )
        for i, lines in enumerate(story)
    )
