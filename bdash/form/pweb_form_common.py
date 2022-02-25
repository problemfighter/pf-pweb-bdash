import codecs
import os
import pathlib


class PWebFormCommon:
    def get_own_path(self):
        return pathlib.Path(__file__).parent.resolve()

    def get_template(self, template_name):
        path = os.path.join(self.get_own_path(), "html", template_name + ".html")
        if os.path.exists(path):
            html_file = codecs.open(path, 'r', 'utf-8')
            return html_file.read()
        return ""
