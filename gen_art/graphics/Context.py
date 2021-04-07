import cairo
from gen_art.graphics.Helpers import open_file


class DrawContext:
    def __init__(self, width, height, output_path, open_bool):
        self.open_bool = open_bool
        self.width = width
        self.height = height
        self.output_path = output_path
        self.init()

    def init(self):
        self.cairo_context = self.setup_png()

    def setup_png(self):
        self.surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, self.width, self.height)
        return cairo.Context(self.surface)

    def export_png(self):
        self.surface.write_to_png(self.output_path)
        print("INFO: Saving file to {}".format(self.output_path))
        if self.open_bool:
            print("INFO: Opening file {}".format(self.output_path))
            open_file(self.output_path)

    def export(self):
        self.export_png()

    @property
    def context(self):
        return self.cairo_context

    @context.setter
    def context(self, context):
        self.context = context

    def get_output_path(self):
        return self.output_path
