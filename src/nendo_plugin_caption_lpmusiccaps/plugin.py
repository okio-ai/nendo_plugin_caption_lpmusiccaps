"""Nendo plugin for captioning music using the LPMusicCaps model."""
import os.path
from typing import Any

import torch
from lpmc.music_captioning.captioning import get_audio
from lpmc.music_captioning.model.bart import BartCaptionModel
from nendo import Nendo, NendoAnalysisPlugin, NendoConfig, NendoTrack

from .config import CaptionLPMusicCapsConfig

settings = CaptionLPMusicCapsConfig()


def add_time_information(n_chunks: int, output: str) -> str:
    """Add time information to the output of the model.

    Args:
        n_chunks (int): Number of chunks in the input audio.
        output (str): Output of the model.

    Returns:
        str: Output of the model with time information.
    """
    inference = ""
    for chunk, text in zip(range(1, n_chunks + 1), output):
        start_minutes, start_seconds = divmod((chunk - 1) * 10, 60)
        end_minutes, end_seconds = divmod(chunk * 10, 60)
        time = f"[{start_minutes:02d}:{start_seconds:02d}-{end_minutes:02d}:{end_seconds:02d}]:"
        inference += f"{time} {text}\n"
    return inference


class CaptionLPMusicCaps(NendoAnalysisPlugin):
    """Nendo plugin for captioning music using the LPMusicCaps model.

    Examples
        ```python
        from nendo import Nendo, NendoConfig, NendoTrack

        nd = Nendo(
            config=NendoConfig(
                log_level="INFO",
                plugins=["nendo_plugin_caption_lpmusiccaps"],
            ),
        )

        track = nd.library.add_track(file_path="tests/assets/test.mp3")
        nd.plugins.caption_lpmusiccaps(track=track)
        print(track.get_plugin_value("caption"))
        ```

    """

    nendo_instance: Nendo = None
    config: NendoConfig = None
    model: BartCaptionModel = None
    device: str = None

    def __init__(self, **data: Any):
        """Initialize the plugin."""
        super().__init__(**data)
        self.device = "cuda:0" if torch.cuda.is_available() else "cpu"
        if not os.path.isfile(settings.model):
            os.makedirs("models", exist_ok=True)
            torch.hub.download_url_to_file(settings.download_url, settings.model)
        self.model = BartCaptionModel(max_length=settings.max_length)
        state_dict = torch.load(settings.model, map_location=self.device)["state_dict"]
        self.model.load_state_dict(state_dict)
        self.model.to(self.device)
        self.model.eval()

    @NendoAnalysisPlugin.run_track
    def run_plugin(self, track: NendoTrack) -> NendoTrack:
        """Run the plugin on the given track.

        Args:
            track (NendoTrack): The track to run the plugin on.

        Returns:
            NendoTrack: The track with the caption added to the `plugin_data`.

        """
        audio_tensor = get_audio(track.resource.src)
        audio_tensor = audio_tensor.to(self.device)

        with torch.no_grad():
            output = self.model.generate(
                samples=audio_tensor,
                num_beams=settings.num_beams,
            )
        return track.add_plugin_data(
            plugin_name="nendo_plugin_caption_lpmusiccaps",
            plugin_version="0.0.1",
            key="caption",
            value=add_time_information(audio_tensor.shape[0], output),
        )
