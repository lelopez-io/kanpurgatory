# kanpurgatory

A Manim animation project that explores the liminal space of Kansas through poetry and animation.

## Voice Configuration

ElevenLabs voice IDs:

Production voice (planned):

```
hyqpbxvsDwE0hQA0TcGB
```

Voice: "Zig"

-   Deep, serious, young, soothing male voice
-   Midwest American accent
-   Ideal for audiobooks and narrative content
-   Character count: 143
-   Training size: 845K samples

Development/testing voice:

```
nPczCjzI2devNBz1zQrb
```

Voice: "Brian"

-   Default voice profile
-   Deep, middle-aged male voice
-   American accent
-   Suitable for narration

## Setup

### Initial Setup

```bash
# Install mise and system dependencies (macOS)
brew install mise py3cairo ffmpeg pango pkg-config scipy sox llvm

# Trust and install development tools (Python, Poetry, etc.)
mise trust
mise install

```

### Environment Configuration

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

### Development Environment

```bash
# Install project dependencies
poetry install

# Activate the virtual environment
source $(poetry env info --path)/bin/activate
```

### Configuration

1. Create a `.env` file in the project root
2. Add your ElevenLabs API key:

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
When using 'elevenlabs', the ELEVEN_API_KEY environment variable must also be set.

## Development Notes

### Voice Configuration

ElevenLabs voice IDs:

Production voice (planned):

```
hyqpbxvsDwE0hQA0TcGB
```

Voice: "Zig"

-   Deep, serious, young, soothing male voice
-   Midwest American accent
-   Ideal for audiobooks and narrative content
-   Character count: 143
-   Training size: 845K samples

Development/testing voice:

```
nPczCjzI2devNBz1zQrb
```

Voice: "Brian"

-   Default voice profile
-   Deep, middle-aged male voice
-   American accent
-   Suitable for narration
