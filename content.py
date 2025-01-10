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
    passages: list[Passage] = None

    def __post_init__(self):
        if self.passages is None:
            # Create linked list of passages
            p1 = Passage("The endless horizon stretches\nbefore me like judgment day\nitself - flat, unforgiving,\neternal.")
            p2 = Passage("What should have been a\nsingle day's passage through\nKansas, transformed into a\nfour-day sentence in\nwinter's prison.")
            p3 = Passage("Here in this liminal space,\nwhere heaven meets earth\nin a razor-thin line,\nI discovered that purgatory\nisn't just a theological concept\n- it's a state of being.")
            p4 = Passage("Not quite damnation,\nnot quite salvation.\n\nJust... Kansas.")
            
            # Link the passages
            p1.next = p2
            p2.next = p3
            p3.next = p4
            
            self.passages = [p1, p2, p3, p4]
