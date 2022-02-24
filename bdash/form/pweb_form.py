import codecs
import os.path
import pathlib
from flask import render_template_string
from pf_flask_rest.form.common.pffr_field_data import FieldData


class PWebForm:

    def get_own_path(self):
        return pathlib.Path(__file__).parent.resolve()

    def get_template(self, template_name):
        path = os.path.join(self.get_own_path(), "html", template_name + ".html")
        if os.path.exists(path):
            html_file = codecs.open(path, 'r', 'utf-8')
            return html_file.read()
        return ""

    def show_input(self, field: FieldData, **kwargs):
        template = self.get_template("text-input")
        return render_template_string(template)


pweb_form = PWebForm()
