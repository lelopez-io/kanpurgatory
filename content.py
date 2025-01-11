from dataclasses import dataclass
from typing import Optional

@dataclass
class Passage:
    display_text: str
    voice_text: str
    next: Optional['Passage'] = None

@dataclass
class Content:
    title: str = "Kanpurgatory:"
    subtitle: str = "Field Notes from the In-Between"
    story: tuple[tuple[str, ...], ...] = (
        # Opening - The vast expanse
        (
            "The endless horizon stretches",
            "before me like judgment day",
            "itself - flat, unforgiving,",
            "eternal.||| What should have",
            "been a single day's passage",
            "through Kansas, as we made",
            "our way from Houston to Boulder,",
            "transformed into a four-day",
            "sentence in winter's prison.",
            "Trapped between intention and",
            "arrival, freezing rain and",
            "blizzards conspired to hold us",
            "in this vast waiting room of",
            "the Great Plains."
        ),
        # The definition
        (
            "Here in this liminal space,",
            "where heaven meets earth in a",
            "razor-thin line, I discovered",
            "that purgatory isn't just a",
            "theological concept - it's a",
            "state of being.|||",
            "",
            "Not quite damnation,|||",
            "not quite salvation.",
            "",
            "***Just***... Kansas.|||"
        ),
        # The descent
        (
            "Our descent began with ice -",
            "treacherous and immediate.",
            "Despite our snow tires, the",
            "car began to lose traction,",
            "forcing us to take the first",
            "exit we could find. The hotel",
            "parking lot became our first",
            "trial, a glacial obstacle",
            "course that transformed each",
            "step into a gamble."
        ),
        # The false guide
        (
            "The front desk attendant,",
            "our supposed ***Virgil*** in",
            "this frozen realm, offered",
            "little guidance beyond pointing",
            "to a light post when pressed",
            "about safer parking options.",
            "No salt for the ice,||| no side",
            "entrance - just a vague gesture",
            "toward illumination|||",
            "as if salvation could be",
            "found in its dim glow."
        ),
        # First casualty
        (
            "The rain crystallized upon",
            "impact, each drop a betrayal",
            "of physics. Even under the",
            "covered port, our careful",
            "steps proved futile|||",
            "",
            "The ice claimed my wife",
            "with casual cruelty|||",
            "her fall shattering our",
            "illusion of control."
        ),
        # The thunder
        (
            "The second circle of our",
            "confinement announced itself",
            "with thunder that crashed",
            "through our room like the",
            "voices of angry gods, so",
            "violent it launched me from",
            "sleep, convinced an 18-wheeler",
            "had careened off the nearby",
            "highway."
        ),
        # Fellow travelers
        (
            "The morning brought us to a",
            "breakfast room full of fellow",
            "travelers, each with their own",
            "tale of narrowly escaped",
            "disaster from the previous",
            "night's treacherous journey.",
            "A sweet lady blessed us with",
            "good wishes after sharing",
            "stories of origins and",
            "destinations||| - all of us now",
            "united in our temporary",
            "imprisonment."
        ),
        # Digital purgatory
        (
            "Back in our room, the",
            "television became a special",
            "kind of torment. The same",
            "two-hour news broadcast played",
            "on endless loop, a cyclical",
            "punishment that drove us to",
            "seek truth from the digital",
            "prophets of TikTok and Twitter",
            "instead. Through our window,",
            "the highway stretched like an",
            "abandoned promise|||",
            "snow plows appeared less",
            "frequently than mirages",
            "in a desert."
        ),
        # State neglect
        (
            "The roads remained untamed,",
            "a testament to Kansas's",
            "indifference. In four days,",
            "we counted fewer plows than",
            "fingers on one hand - a",
            "pitiful showing for a state",
            "so familiar with winter's",
            "rage.",
            "",
            "The state had abandoned its",
            "people to weather's whims,|||",
            "a government's shrug in the",
            "face of nature's fury."
        ),
        # The deterioration
        (
            "By the third day, when",
            "breakfast deteriorated to",
            "biscuits, tots, and eggs -",
            "the absence of meat a final",
            "indignity - we knew we had",
            "to attempt our exodus. The",
            "parking lot had become a",
            "graveyard of vehicles, snow",
            "piled high as tire wells,",
            "with no hope of municipal",
            "salvation."
        ),
        # Unexpected allies
        (
            "As we plotted our escape,",
            "a community formed among",
            "the stranded. The Spanish-",
            "speaking travelers became",
            "unexpected allies, their",
            "determination inspiring.",
            "They were first to request",
            "shovels from the hotel staff,",
            "who dismissed our plight|||",
            "unwilling to brave the cold",
            "that imprisoned us all."
        ),
        # Community forms
        (
            "In their faces, I saw the",
            "warmth of family - parents,",
            "siblings, aunts, uncles,",
            "cousins - all united in this",
            "cold purgatory. Their spirit",
            "brought comfort.||| Then I",
            "spotted what seemed a gift -",
            "a mini dozer next door",
            "carving paths through drifts."
        ),
        # False salvation
        (
            "This mechanical savior at",
            "the neighboring restaurant",
            "seemed an answer to prayer.",
            "Wading through knee-deep",
            "drifts, we offered payment",
            "to free our vehicles.",
            "",
            "The operator's response cut",
            "deeper than the cold.|||",
            "",
            "He refused on principle,|||",
            "citing past payment disputes",
            "with the hotel owner."
        ),
        # Texas comparison
        (
            "The cold calculus of old",
            "grudges proved stronger than",
            "community need, echoing the",
            "hotel's earlier indifference.",
            "",
            "In twenty years of weathering",
            "hurricanes in Texas, I'd never",
            "encountered such reluctance to",
            "help fellow humans in distress|||",
            "- back home, we'd learned that",
            "surviving nature's fury required",
            "standing together."
        ),
        # Escape attempt
        (
            "After several cars managed to",
            "forge a path through the snow,",
            "we loaded our remaining",
            "belongings and began our own",
            "escape. The journey to Salina",
            "- a mere 56 miles that",
            "stretched into a two-hour",
            "pilgrimage - tested every nerve.",
            "",
            "The roads remained treacherous,",
            "as if Kansas itself was",
            "reluctant to release its grip",
            "on wayward souls."
        ),
        # Night in Salina
        (
            "Unwilling to transform the",
            "remaining seven-hour drive",
            "into fourteen hours of white-",
            "knuckle navigation, we",
            "surrendered to another night",
            "in Salina. There, I turned to",
            "meteorological divination,",
            "consulting AI to decipher the",
            "National Weather Service's",
            "cryptic forecasts. ***Determined***",
            "not to be caught in such",
            "limbo again."
        ),
        # The final attempt
        (
            "Finally, four days after our",
            "journey began, we attempted",
            "our escape. The first three",
            "hours remained a trial of",
            "ice-slicked roads and white-",
            "knuckled tension, each mile",
            "demanding complete focus.",
            "",
            "Only as we approached western",
            "Kansas did the ice begin to",
            "relent||| the sun having done",
            "its work at last."
        ),
        # The crossing
        (
            "The roads improved with each",
            "mile westward. Crossing into",
            "Colorado felt like entering",
            "another world - their crews",
            "had already tamed that",
            "morning's fresh snowfall|||",
            "leaving clear paths before us."
        ),
        # The aftermath
        (
            "The contrast was stark.",
            "Yet despite the clear roads",
            "ahead, exhaustion had settled",
            "deep in my bones. What should",
            "have been a simple drive|||",
            "became the most grueling",
            "journey I'd ever experienced|||",
            "defeated by the most",
            "unassuming terrain imaginable."
        ),
        # Final reflection
        (
            "Beware ***Kanpurgatory***",
            "- ***where every soul caught",
            "between departure and",
            "destination discovers the",
            "true meaning of limbo.***",
            "",
            "In our case, it",
            "was a four-day lesson in",
            "patience, community, and the",
            "peculiar helplessness that",
            "comes when nature and",
            "institutions alike seem to",
            "conspire against your progress."
        ),
        # Epilogue
        (
            "Some say purgatory is a",
            "place of cleansing.|||",
            "If so, we emerged from Kansas",
            "scrubbed clean of any illusions",
            "about winter travel through",
            "the Great Plains, with a",
            "newfound appreciation for the",
            "small kindnesses of fellow",
            "travelers caught in the same",
            "divine comedy."
        )
    )
    passages: tuple[Passage, ...] = None

    def __post_init__(self):
        def format_display_text(lines):
            # First join lines with newlines
            text = "\n".join(lines)
            # Remove all markers from display text
            return text.replace("|||", "").replace("***", "")

        def format_voice_text(lines):
            # Join lines with spaces, preserving intentional paragraph breaks
            text = ""
            for line in lines:
                if line == "":  # Keep empty lines as pauses
                    text += " . . . "
                else:
                    # Add space if not at start and not after a pause
                    if text and not text.endswith(" . . . "):
                        text += " "
                    # Process the line for voice text
                    processed_line = (line.strip()
                                    .replace("***", ' "" ')
                                    .replace("|||", " . . . ")
                                    .replace("...", " . . . ")
                                    .replace(" - ", " . . . ")
                                    
                    )
                    text += processed_line
            return text

        self.passages = tuple(
            Passage(
                display_text=format_display_text(lines),  # Cleanup formatting for display
                voice_text=format_voice_text(lines),  # Enhance format for voice
                next=None if i == len(self.story) - 1 else Passage(
                    display_text=format_display_text(self.story[i + 1]),
                    voice_text=format_voice_text(self.story[i + 1])
                )
            )
            for i, lines in enumerate(self.story)
        )
