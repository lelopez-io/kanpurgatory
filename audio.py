import numpy as np
from scipy.io import wavfile
import os

class AudioGenerator:
    def __init__(self, sample_rate=44100):
        self.sample_rate = sample_rate
        self.audio_dir = "audio"
        os.makedirs(self.audio_dir, exist_ok=True)

    def generate_tone(self, frequency, duration, index):
        """Generate a sine wave tone with given frequency and duration"""
        t = np.linspace(0, duration, int(self.sample_rate * duration))
        signal = np.sin(2 * np.pi * frequency * t)
        
        # Apply fade in/out
        fade_duration = 0.1  # seconds
        fade_length = int(fade_duration * self.sample_rate)
        fade_in = np.linspace(0, 1, fade_length)
        fade_out = np.linspace(1, 0, fade_length)
        
        signal[:fade_length] *= fade_in
        signal[-fade_length:] *= fade_out
        
        # Normalize
        signal = signal * 0.3  # Reduce volume to 30%
        
        # Save as WAV file
        filename = os.path.join(self.audio_dir, f"tone_{index}.wav")
        wavfile.write(filename, self.sample_rate, signal.astype(np.float32))
        return filename

    def generate_passage_tones(self, num_passages):
        """Generate unique tones for each passage"""
        base_freq = 440  # A4 note
        tones = []
        for i in range(num_passages):
            # Generate frequencies in a pleasing scale
            frequency = base_freq * (2 ** (i/12))  # Moving up by semitones
            filename = self.generate_tone(frequency, 2.0, i)
            tones.append(filename)
        return tones
