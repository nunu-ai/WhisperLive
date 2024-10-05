from whisper_live.client import TranscriptionClient
import sys

def example_callback(result):
    """
    Example callback function to process transcription results.
    
    :param result: A dictionary containing transcription information
    """
    print("result: ", result)
    # sys.exit()
    
client = TranscriptionClient(
  "localhost",
  9090,
  lang="en",
  translate=False,
  model="tiny",
  use_vad=False,
  save_output_recording=False,                         # Only used for microphone input, False by Default
  output_recording_filename="./output_recording.wav",  # Only used for microphone input
  callback=example_callback  # Add the callback function here
)

client(hls_url="http://as-hls-ww-live.akamaized.net/pool_904/live/ww/bbc_1xtra/bbc_1xtra.isml/bbc_1xtra-audio%3d96000.norewind.m3u8")