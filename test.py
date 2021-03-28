import os
from music_analysis.analyse import analyse
from gen_art.generate_art import generate

if __name__ == '__main__':
    songs = os.listdir('audios')
    for song in songs:
        happy, dance, aggressive, chill, acoustic = analyse('audios/' + song)
        print(song + ":")
        print("  happy - " + str(happy))
        print("  dance - " + str(dance))
        print("  aggressive - " + str(aggressive))
        print("  chill - " + str(chill))
        print("  acoustic - " + str(acoustic))

        generate("images/" + song + ".png", happy, dance, aggressive, chill, acoustic)
