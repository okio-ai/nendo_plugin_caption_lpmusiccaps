# Nendo Plugin Caption LP-MusicCaps

<br>
<p align="left">
    <img src="https://okio.ai/docs/assets/nendo_core_logo.png" width="350" alt="nendo core">
</p>
<br>

<p align="left">
<a href="https://okio.ai" target="_blank">
    <img src="https://img.shields.io/website/https/okio.ai" alt="Website">
</a>
<a href="https://twitter.com/okio_ai" target="_blank">
    <img src="https://img.shields.io/twitter/url/https/twitter.com/okio_ai.svg?style=social&label=Follow%20%40okio_ai" alt="Twitter">
</a>
<a href="https://discord.gg/gaZMZKzScj" target="_blank">
    <img src="https://dcbadge.vercel.app/api/server/XpkUsjwXTp?compact=true&style=flat" alt="Discord">
</a>
</p>

---

An audio captioning plugin based on LP-MusicCaps.

## Features 

- Generate captions for all types of audio
- Caption your audio library and make it searchable by using the other nendo search plugins

## Requirements

This plugin requires the manual installation of the `LP-MusicCaps` repository from git, run:

```bash
git clone https://github.com/seungheondoh/lp-music-caps.git
cd lp-music-caps
pip install -e .
```

For more information, please refer to the [LP-MusicCaps repository](https://github.com/seungheondoh/lp-music-caps.git).

## Installation

1. [Install Nendo](https://github.com/okio-ai/nendo#installation)
2. `pip install nendo-plugin-caption-lpmusiccaps`

## Usage

Take a look at a basic usage example below.
For more detailed information, please refer to the [documentation](https://okio.ai/docs/plugins).

```pycon
>>> from nendo import Nendo
>>> nd = Nendo(plugins=["nendo_plugin_caption_lpmusiccaps"])
>>> track = nd.library.add_track(file_path="path/to/file.mp3")

>>> nd.plugins.caption_lpmusiccaps(track=track)
>>> track.get_plugin_value("caption")
```


## Contributing
Visit our docs to learn all about how to contribute to Nendo: [Contributing](https://okio.ai/docs/contributing/)


## License
Nendo: MIT License

LP-MusicCaps: CC-BY-NC 4.0 license.

Pretrained models: The weights are released under the CC-BY-NC 4.0 license
