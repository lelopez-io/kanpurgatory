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
    story: tuple[str, ...] = (
        "The endless horizon stretches\nbefore me like judgment day\nitself - flat, unforgiving,\neternal.",
        "What should have been a\nsingle day's passage through\nKansas, transformed into a\nfour-day sentence in\nwinter's prison.", 
        "Here in this liminal space,\nwhere heaven meets earth\nin a razor-thin line,\nI discovered that purgatory\nisn't just a theological concept\n- it's a state of being.",
        "Not quite damnation,\nnot quite salvation.\n\nJust... Kansas."
    )
    passages: tuple[Passage, ...] = tuple(
        Passage(text, next=None if i == len(story) - 1 else Passage(story[i + 1]))
        for i, text in enumerate(story)
    )
