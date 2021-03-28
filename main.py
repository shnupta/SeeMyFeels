# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import matplotlib.pyplot as plt
from musicnn.extractor import extractor


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
#
#
# Press the green button in the gutter to run the script.
def calculate_net_happy(happy_value, sad_value):
    return happy_value - sad_value


def calculate_chillness(chillout, mellow, chill, ambient, acoustic):
    return (chillout + mellow + chill + ambient + acoustic) / 5


def calculate_danceable(dance, hip_hop, party, easy, sexy, funk):
    return (dance + hip_hop + party + easy + sexy + funk) / 6


def calculate_aggressiveness(heavy, metal, hard, punk):
    return (heavy + metal + hard + punk) / 4


def calculate_retro(val_60s, val_70s, val_80s, val_90s, oldies):
    return (val_60s + val_70s + val_80s + val_90s + oldies) / 5


if __name__ == '__main__':
    taggram, tags = extractor("musicnn/audio/happy.mp3",
                              model='MSD_musicnn', extract_features=False)
    # in_length = 5  # seconds  by default, the model takes inputs of 3 seconds with no overlap

    # plt.rcParams["figure.figsize"] = (10, 8)  # set size of the figures
    fontsize = 12  # set figures font size
    # fig, ax = plt.subplots()
    #
    # # title
    # ax.title.set_text('Taggram')
    # ax.title.set_fontsize(fontsize)
    #
    # # x-axis title
    # ax.set_xlabel('(seconds)', fontsize=fontsize)
    #
    # # y-axis
    # y_pos = np.arange(len(tags))
    # ax.set_yticks(y_pos)
    # ax.set_yticklabels(tags, fontsize=fontsize - 1)
    #
    # # x-axis
    # x_pos = np.arange(taggram.shape[0])
    # x_label = np.arange(in_length / 2, in_length * taggram.shape[0], 5)
    # ax.set_xticks(x_pos)
    # ax.set_xticklabels(x_label, fontsize=fontsize)
    #
    # # depict taggram
    # ax.imshow(taggram.T, interpolation=None, aspect="auto")
    # plt.show()

    tags_likelihood_mean = np.mean(taggram, axis=0)
    fig, ax = plt.subplots()

    # title
    ax.title.set_text('Tags likelihood (mean of the taggram)')
    ax.title.set_fontsize(fontsize)

    # y-axis title
    ax.set_ylabel('(likelihood)', fontsize=fontsize)

    # y-axis
    ax.set_ylim((0, 100))
    ax.tick_params(axis="y", labelsize=fontsize)

    # x-axis
    ax.tick_params(axis="x", labelsize=fontsize - 1)
    pos = np.arange(len(tags))
    ax.set_xticks(pos)
    ax.set_xticklabels(tags, rotation=90)

    # depict song-level tags likelihood
    ax.bar(pos, tags_likelihood_mean * 100)

    options = ['net_happy', 'chillness', 'danceable', 'aggressiveness', 'retro']
    values = [0, 0, 0, 0, 0]

    happy_index = list(tags).index('happy')
    sad_index = list(tags).index('sad')
    values[0] = calculate_net_happy(tags_likelihood_mean[happy_index], tags_likelihood_mean[sad_index])

    chillout_index = list(tags).index('chillout')
    mellow_index = list(tags).index('Mellow')
    chill_index = list(tags).index('chill')
    ambient_index = list(tags).index('ambient')
    acoustic_index = list(tags).index('acoustic')
    values[1] = calculate_chillness(tags_likelihood_mean[chillout_index],
                                    tags_likelihood_mean[mellow_index],
                                    tags_likelihood_mean[chill_index],
                                    tags_likelihood_mean[ambient_index],
                                    tags_likelihood_mean[acoustic_index])

    dance_index = list(tags).index('dance')
    hip_hop_index = list(tags).index('Hip-Hop')
    party_index = list(tags).index('party')
    easy_index = list(tags).index('easy listening')
    sexy_index = list(tags).index('sexy')
    funk_index = list(tags).index('funk')
    values[2] = calculate_danceable(tags_likelihood_mean[dance_index],
                                    tags_likelihood_mean[hip_hop_index],
                                    tags_likelihood_mean[party_index],
                                    tags_likelihood_mean[easy_index],
                                    tags_likelihood_mean[sexy_index],
                                    tags_likelihood_mean[funk_index])

    heavy_index = list(tags).index('heavy metal')
    metal_index = list(tags).index('metal')
    hard_rock_index = list(tags).index('hard rock')
    punk_index = list(tags).index('punk')
    values[3] = calculate_aggressiveness(tags_likelihood_mean[heavy_index],
                                         tags_likelihood_mean[metal_index],
                                         tags_likelihood_mean[hard_rock_index],
                                         tags_likelihood_mean[punk_index])

    index_60s = list(tags).index('60s')
    index_70s = list(tags).index('70s')
    index_80s = list(tags).index('80s')
    index_90s = list(tags).index('90s')
    oldies_index = list(tags).index('oldies')
    values[4] = calculate_retro(tags_likelihood_mean[index_60s],
                                tags_likelihood_mean[index_70s],
                                tags_likelihood_mean[index_80s],
                                tags_likelihood_mean[index_90s],
                                tags_likelihood_mean[oldies_index])

    for i in range(len(values)):
        print(options[i])
        print(values[i])

    # plt.show()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
