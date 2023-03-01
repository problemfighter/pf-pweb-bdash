from flask import render_template_string
from bdash.form.pweb_form_common import PWebFormCommon
from pf_flask_rest.form.common.pffr_field_data import FieldData


class PWebForm:
    pweb_form_common = PWebFormCommon()

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

        if not field.value:
            field.value = ""

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

    def _get_select_option_html(self, options, **kwargs):
        option_html = kwargs.get("option_html")
        if not options and option_html:
            return option_html
        return ""

    def _get_select_options(self, field: FieldData):
        options = []
        for item in field.selectOptions:
            label = field.selectOptions[item]
            if field.selectOptionLabel == "value":
                label = item
            option = {
                "label": label,
                "value": item,
            }
            if field.value and str(field.value) == str(item):
                option['selected'] = True
            elif field.default and str(field.default) == str(item):
                option['selected'] = True
            options.append(option)
        return options

    def _process_override(self, field: FieldData, **kwargs):
        if "label" in kwargs:
            field.label = kwargs.get("label")
        if "type" in kwargs:
            field.inputType = kwargs.get("type")
        return field

    def _process_various_attrs(self, field: FieldData, **kwargs):
        ignore = ["class", "type", "label", "option_html"]
        for key, value in kwargs.items():
            if key in ignore:
                continue
            field.attributes += f"""{key}={value}"""
        return field

    def show_input(self, field: FieldData, wrapper=True, **kwargs):
        template = self.pweb_form_common.get_template("text-input")
        field = self._process_field_data(field)
        wrapper_klass = self._get_wrapper_class(field.topAttrClass, **kwargs)
        options = self._get_select_options(field)
        option_html = self._get_select_option_html(options, **kwargs)
        field = self._process_override(field, **kwargs)
        field = self._process_various_attrs(field, **kwargs)
        data = {
            "wrapperKlass": wrapper_klass,
            "wrapper": wrapper,
            "field": field,
            "selectFirstEntry": field.selectFirstEntry,
            "options": options,
            "option_html": option_html,
        }
        return render_template_string(template, conf=data)

    def show_error_message(self, field: FieldData):
        template = self.pweb_form_common.get_template("error-message")
        data = {
            "field": field,
        }
        return render_template_string(template, conf=data)

    def add_error_class(self, field: FieldData):
        if field.has_error:
            return "is-invalid"
        return ""

    def form_select(self, name, options: list, **kwargs):
        option_html = ""
        value = kwargs.get("value")
        klass = kwargs.get("class")
        attr_id = kwargs.get("id")
        parent_attr = kwargs.get("attr")
        if options:
            for option in options:
                attr = ""
                selected = ""
                if "attr" in option:
                    attr = option["attr"]
                option_value = option["value"]
                if value and value == option_value:
                    selected = "selected"
                option_html += f"""<option {selected} {attr} value="{option_value}">{option["label"]}</option>"""
        select_attr = ""
        if parent_attr:
            select_attr += parent_attr
        if attr_id:
            select_attr += f""" id="{attr_id}" """
        select_html = f"""<select class="form-select {klass}" name="{name}" {select_attr}>{option_html}</select>"""
        return select_html


pweb_form = PWebForm()
