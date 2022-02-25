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

    def _get_wrapper_class(self, klass="", **kwargs):
        if not klass:
            klass = ""
        custom = kwargs.get("class")
        if custom:
            klass = " " + custom
        klass = klass.strip()
        if klass and klass != "":
            return 'class="' + klass + '"'
        return ""

    def _process_field_data(self, field: FieldData):
        if field.default and (field.value == "" or not field.value):
            field.value = field.default

        if not field.inputType and field.dataType:
            data_type = field.dataType
            if data_type == "Integer" or data_type == "Float" or data_type == "Decimal":
                field.inputType = "number"
            elif data_type == "Email":
                field.inputType = "email"
            elif data_type == "EnumField":
                field.inputType = "select"
            else:
                field.inputType = "text"

        return field

    def _get_select_options(self, field: FieldData):
        options = []
        for item in field.selectOptions:
            option = {
                "label": field.selectOptions[item],
                "value": item,
            }
            if field.value and field.value == item:
                option['selected'] = True
            elif field.default and field.default == item:
                option['selected'] = True
            options.append(option)
        return options

    def show_input(self, field: FieldData, wrapper=True, **kwargs):
        template = self.get_template("text-input")
        field = self._process_field_data(field)
        wrapper_klass = self._get_wrapper_class(field.topAttrClass, **kwargs)
        options = self._get_select_options(field)
        data = {
            "wrapperKlass": wrapper_klass,
            "wrapper": wrapper,
            "field": field,
            "options": options,
        }
        return render_template_string(template, conf=data)

    def show_error_message(self, field: FieldData):
        template = self.get_template("error-message")
        data = {
            "field": field,
        }
        return render_template_string(template, conf=data)

    def add_error_class(self, field: FieldData):
        if field.has_error:
            return
        return "is-invalid"


pweb_form = PWebForm()
