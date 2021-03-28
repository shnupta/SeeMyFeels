from os import environ as env
import gen_art.graphics.Config as config
from gen_art.graphics.Context import DrawContext


def setup(width, height, output_path):
    config.DrawContext = DrawContext(
                                     width,
                                     height,
                                     output_path,
                                     False
                                    )
    config.Context = config.DrawContext.context
    log_info()


def export():
    config.DrawContext.export()


def log_info():
    print("INFO: Generating image for {}".format(config.script_name))
    print("INFO: Images being saved to directory {}".format(config.image_folder))
