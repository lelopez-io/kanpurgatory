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
            "eternal. What should have",
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
            "***Just***... Kansas."
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
            "No salt for the ice, no side",
            "entrance - just a vague gesture",
            "toward illumination|||",
            "as if salvation could be",
            "found in its dim glow."
        ),
        # First casualty
        (
            "The rain crystallized upon",
            "impact, turning every surface",
            "into a mirror of our mounting",
            "uncertainty. Despite our careful",
            "choreography around the vehicle",
            "under the covered port,|||",
            "the ice claimed my wife as",
            "its first victim."
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
        # State contrast
        (
            "The contrast was stark - in",
            "the brief drive from Colorado's",
            "border to our home, we'd",
            "typically see more road",
            "treatment vehicles than Kansas",
            "managed to muster for its",
            "entire storm response.",
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
            "faces reflecting the warmth",
            "of family - parents, siblings,",
            "aunts, uncles, cousins - in",
            "this cold purgatory."
        ),
        # False hope
        (
            "Hope appeared briefly in the",
            "form of a mini dozer clearing",
            "snow at the neighboring",
            "restaurant. Yet when approached",
            "with our plea - several vehicles",
            "seeking liberation, with offers",
            "of payment for assistance -",
            "the operator revealed another",
            "layer of this purgatorial",
            "bureaucracy.",
            "",
            "He refused on principle|||",
            "citing past payment disputes."
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
            "cryptic forecasts, determined",
            "not to be caught in such",
            "limbo again."
        ),
        # Final escape
        (
            "Finally, four days after our",
            "journey began, we broke free",
            "of Kansas's grip. The first",
            "hours remained a trial - hands",
            "requiring rest each hour from",
            "the tension of navigating",
            "ice-slicked roads.",
            "",
            "Yet we'd timed our departure",
            "perfectly for once, arriving",
            "in Colorado just after their",
            "storm had passed, allowing their",
            "more vigilant road crews time",
            "to restore order."
        ),
        # The contrast
        (
            "The contrast was immediate",
            "and telling - smooth sailing",
            "all the way home, though by",
            "then exhaustion had settled",
            "deep in my bones from what",
            "had been the most stressful",
            "drive I'd ever experienced",
            "on essentially flat roads."
        ),
        # Final reflection
        (
            "Welcome to ***Kanpurgatory***",
            "- where every soul caught",
            "between where they've been",
            "and where they're meant to",
            "be learns the true meaning",
            "of limbo. In our case, it",
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
            "place of cleansing|||",
            "if so, we emerged from Kansas",
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
                                    .replace("|||", " . . . ")
                                    .replace("...", " . . . ")
                                    .replace("***", ' "" ')
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