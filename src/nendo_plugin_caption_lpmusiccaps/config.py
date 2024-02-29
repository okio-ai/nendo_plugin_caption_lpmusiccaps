"""Configuration for LP-Music-Caps model."""
from nendo import NendoConfig
from pydantic import Field


class CaptionLPMusicCapsConfig(NendoConfig):
    """Configuration for the LP-Music-Caps model.

    Attributes:
        model (str): The local path for the model. Defaults to "models/transfer.pth".
        download_url (str): The download url for the model. Defaults to "https://huggingface.co/seungheondoh/lp-music-caps/resolve/main/transfer.pth".
        num_beams (int): The number of beams to use. Defaults to 5.
        max_length (int): The maximum length of the caption. Defaults to 128.
    """

    model: str = Field("transfer.pth")
    download_url: str = Field(
        "https://huggingface.co/seungheondoh/lp-music-caps/resolve/main/transfer.pth",
    )
    num_beams: int = Field(5)
    max_length: int = Field(128)
