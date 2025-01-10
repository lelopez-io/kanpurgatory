# kanpurgatory

A Manim animation project that explores the liminal space of Kansas through poetry and animation.

## Voice Configuration

ElevenLabs voice IDs:

Production voice (planned):
```
hyqpbxvsDwE0hQA0TcGB
```
Voice: "Zig"
- Deep, serious, young, soothing male voice
- Midwest American accent
- Ideal for audiobooks and narrative content
- Character count: 143
- Training size: 845K samples

Development/testing voice:
```
nPczCjzI2devNBz1zQrb
```
Voice: "Brian"
- Default voice profile
- Deep, middle-aged male voice
- American accent
- Suitable for narration

## Setup

### System Dependencies
```bash
# Install system dependencies (macOS)
brew install py3cairo ffmpeg pango pkg-config scipy sox llvm
```

### Environment Setup
```bash
# Add LLVM to your path and set required environment variables
export PATH="/opt/homebrew/opt/llvm/bin:$PATH"
export LDFLAGS="-L/opt/homebrew/opt/llvm/lib"
export CPPFLAGS="-I/opt/homebrew/opt/llvm/include"
```

### Development Environment
```bash
# Install Python, Poetry, and Rust via mise
mise install

# Install project dependencies
poetry install

# Activate the virtual environment
poetry env shell
```

### Configuration
1. Create a `.env` file in the project root
2. Add your ElevenLabs API key:
```
ELEVENLABS_API_KEY=your_api_key_here
```

### Font Requirements
- Spectral font family (specifically Spectral-ExtraLight.ttf)
- Place font file in `font/` directory

## Usage

Generate the video:
```bash
manim -pql scene.py KanpurgatoryVideo
```

## Development Notes

### Voice Configuration

ElevenLabs voice IDs:

Production voice (planned):
```
hyqpbxvsDwE0hQA0TcGB
```
Voice: "Zig"
- Deep, serious, young, soothing male voice
- Midwest American accent
- Ideal for audiobooks and narrative content
- Character count: 143
- Training size: 845K samples

Development/testing voice:
```
nPczCjzI2devNBz1zQrb
```
Voice: "Brian"
- Default voice profile
- Deep, middle-aged male voice
- American accent
- Suitable for narration
