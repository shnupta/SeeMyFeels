import os

from music_analysis.analyse import analyse
from gen_art.generate_art import generate
from definitions import ROOT_DIR

if __name__ == '__main__':
    songs = os.listdir(os.path.join(ROOT_DIR, 'test/audios'))
    for song in songs:
        happy, dance, aggressive, chill, acoustic = analyse(os.path.join(ROOT_DIR, 'test/audios/' + song))
        print(song + ":")
        print("  happy - " + str(happy))
        print("  dance - " + str(dance))
        print("  aggressive - " + str(aggressive))
        print("  chill - " + str(chill))
        print("  acoustic - " + str(acoustic))

        generate(os.path.join(ROOT_DIR, "test/images/" + song + ".png"), happy, dance, aggressive, chill, acoustic)
