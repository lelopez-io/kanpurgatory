# kanpurgatory

A Manim animation project that explores the liminal space of Kansas through poetry and animation.

## Quick Start

### 1. Initial Setup

```bash
# Install mise and system dependencies (macOS)
brew install mise py3cairo ffmpeg pango pkg-config scipy sox llvm

# Install font
cp assets/fonts/Spectral-ExtraLight.ttf ~/Library/Fonts/

# Trust and install development tools (Python, Poetry, etc.)
mise trust
mise install
```

### 2. Environment Configuration

```bash
# Set Python build configuration
export PYTHON_CONFIGURE_OPTS="--enable-shared"
export PYTHON_INCLUDE_DIR=$(mise where python)/include/python3.11
export PYTHON_LIBRARY=$(mise where python)/lib/libpython3.11.dylib
export PKG_CONFIG_PATH="$(mise where python)/lib/pkgconfig:/opt/homebrew/lib/pkgconfig"
export CFLAGS="-I$(mise where python)/include/python3.11"

# Add LLVM to your path and set required environment variables
export PATH="/opt/homebrew/opt/llvm/bin:$PATH"
export LDFLAGS="-L/opt/homebrew/opt/llvm/lib -L/opt/homebrew/lib"
export CPPFLAGS="-I/opt/homebrew/opt/llvm/include -I/opt/homebrew/include"
```

### 3. Project Setup

```bash
# Install project dependencies
poetry install

# Activate the virtual environment
source $(poetry env info --path)/bin/activate
```

### 4. Configuration

Create a `.env` file in the project root with your ElevenLabs API key:

```
ELEVEN_API_KEY=your_api_key_here
```

## Usage

Generate the video:

```bash
# Production mode (uses ElevenLabs API)
VOICE_SERVICE=elevenlabs poetry run manim -pql scene.py KanpurgatoryVideo

# Development mode (uses gTTS, no API calls)
VOICE_SERVICE=gtts poetry run manim -pql scene.py KanpurgatoryVideo
```

Note: VOICE_SERVICE environment variable is required and must be set to either 'gtts' or 'elevenlabs'.
When using 'elevenlabs':

-   The ELEVEN_API_KEY environment variable must be set
-   You'll need to allow interactive pip installation of additional dependencies when prompted
-   After the first run installs dependencies, you'll need to run the command again

## Troubleshooting

### Font Changes Not Appearing

If font changes aren't visible after updating fonts, clear Manim's cache:

```bash
# Remove cached renders
rm -rf media/
```

Then re-render the video.

## Development Notes

### Content Formatting

The project uses a structured format for content in `content.py`:

#### Title & Subtitle

Simple strings that form the opening sequence:

```python
title: str = "Kanpurgatory:"
subtitle: str = "Field Notes from the In-Between"
```

#### Story Structure

The story is composed of passages, each containing lines of text. Special markers can be used within the text:

-   `|||` - Adds a dramatic pause (converts to " . . . " in voiceover)
-   `...` - Ellipsis (converts to " . . . " in voiceover)
-   `***` - Adds emphasis (converts to quoted text in voiceover)

Example:

```python
story = (
    (
        "Not quite damnation,|||",  # Pause after "damnation"
        "not quite salvation.",
        "",
        "***Just***... Kansas."     # Emphasis on "Just"
    ),
)
```

### Voice Configuration

#### Production Voice (Zig)

```
hyqpbxvsDwE0hQA0TcGB
```

-   Deep, serious, young, soothing male voice
-   Midwest American accent
-   Ideal for audiobooks and narrative content
-   Character count: 143
-   Training size: 845K samples

#### Development Voice (Brian)

```
nPczCjzI2devNBz1zQrb
```

-   Default voice profile
-   Deep, middle-aged male voice
-   American accent
-   Suitable for narration
