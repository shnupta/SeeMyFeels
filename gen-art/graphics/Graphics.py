from os import environ as env
import graphics.Config as config
from graphics.Context import DrawContext


def setup(width, height, filename, **kwargs):
    config.DrawContext = DrawContext(
                                     width,
                                     height,
                                     filename,
                                     kwargs.get('file_format', config.file_format),
                                     kwargs.get('image_folder', config.image_folder),
                                     kwargs.get('script_name', config.script_name),
                                     kwargs.get('open_file', config.open_file)
                                    )
    config.Context = config.DrawContext.context
    log_info()


def export():
    config.DrawContext.export()


def log_info():
    print("INFO: Generating image for {}".format(config.script_name))
    print("INFO: Images being saved to directory {}".format(config.image_folder))