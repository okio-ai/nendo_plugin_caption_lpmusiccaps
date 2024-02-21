import random
import unittest

import numpy as np
import torch
from nendo import Nendo, NendoConfig

TEST_CAPTION = "[00:00-00:10]: This is the live performance of a Russian folk music piece. There is a female vocalist singing in a vibrant and cheerful manner. The melody is being played by the bagpipe and the rhythmic background is provided by the acoustic drums. The atmosphere is lively. This piece could be used in the soundtrack of a historical drama movie during wedding scenes.\n[00:10-00:20]: The low quality recording features a R&B song that consists of soft male vocals, alongside wide background female vocals, singing over punchy kick, claps, shimmering hi hats, tinny bells melody, synth lead melody and groovy bass. It sounds passionate, emotional and addictive - like something you would hear in clubs.\n[00:20-00:30]: This is a hip-hop music piece. There is a female vocalist singing melodically. The melody is being played by the piano and the electric guitar while a bass guitar is playing in the background. The rhythm is provided by a slow tempo acoustic drum beat. The atmosphere is chill and trippy. This piece could be used in the soundtrack of a crime movie that takes place in the big city.\n[00:30-00:40]: The low quality recording features a R&B song that consists of a passionate male vocal, alongside wide echoing female vocals, singing over punchy kick, snare hits, shimmering hi hats, synth lead melody and groovy bass. It sounds energetic and exciting.\n[00:40-00:50]: The low quality recording features a R&B song that consists of a passionate male vocal, alongside wide echoing female vocals, singing over punchy kick, snare hits, shimmering hi hats, synth lead melody and groovy bass. It sounds energetic and exciting.\n[00:50-01:00]: This is an electronic dance music piece. There is a male vocalist singing melodically in the lead. The melody is being played by the keyboard while the bass guitar is playing in the background. The rhythm is provided by a slow tempo acoustic drum beat. The atmosphere is energetic. This piece could be used in the soundtrack of a mobile car racing game.\n[01:00-01:10]: This is a live performance of a wedding music piece. There is a female vocalist singing melodically. The melody is being played by the accordion while the rhythmic background is provided by the acoustic drums. The atmosphere is vibrant. This piece could be used in the soundtrack of a historical drama movie during a scene of celebration.\n[01:10-01:20]: This is a hip-hop music piece. There is a male vocalist singing melodically in the lead. The melody is being played by the synth and the bass guitar while a synth sound is playing in the background. The rhythm is provided by a slow tempo electronic drum beat. The atmosphere is sentimental. This piece could be used in the soundtrack of a crime movie where a character is going through the city.\n[01:20-01:30]: This is a hip-hop music piece. There is a female vocalist singing melodically. The melody is being played by the electric guitar and the keyboard while the bass guitar is playing in the background. The rhythm is provided by a slow tempo acoustic drum beat. The atmosphere is sentimental. This piece could be used in the soundtrack of a crime movie that takes place in the big city.\n[01:30-01:40]: The low quality recording features a R&B song that consists of a passionate male vocal, alongside wide echoing female vocals, singing over punchy kick, snare hits, shimmering hi hats, synth lead melody and groovy bass. It sounds energetic and exciting.\n[01:40-01:50]: The low quality recording features a R&B song that consists of a passionate female vocal, alongside wide echoing female vocals, singing over punchy kick, snare hits, shimmering hi hats, synth lead melody and groovy bass. It sounds energetic and exciting.\n[01:50-02:00]: This is a hip-hop music piece. There is a male vocalist singing melodically in the lead. The melody is being played by the electric guitar and the keyboard while the bass guitar is playing in the background. The rhythm is provided by a slow tempo electronic drum beat. The atmosphere is urban. This piece could be used in the soundtrack of a crime movie that takes place in the big city.\n"

nd = Nendo(
    config=NendoConfig(
        log_level="INFO",
        plugins=["nendo_plugin_caption_lpmusiccaps"],
    ),
)


class CaptionLPMusicCapsTests(unittest.TestCase):
    def test_run_caption_lpmusiccaps(self):
        # fix seeds
        random.seed(42)
        np.random.seed(42)
        torch.manual_seed(42)

        nd.library.reset(force=True)
        track = nd.library.add_track(file_path="tests/assets/test.mp3")
        nd.plugins.caption_lpmusiccaps(track=track)
        self.assertEquals(
            TEST_CAPTION,
            track.get_plugin_value("caption"),
        )


if __name__ == "__main__":
    unittest.main()
