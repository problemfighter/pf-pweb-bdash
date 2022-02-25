from bdash.form.lib.jinja2_tag_helper import StandaloneTag
from bdash.form.pweb_form import pweb_form
from bdash.form.pweb_table import pweb_table


class ShowInput(StandaloneTag):
    tags = {"show_input"}

    def render(self, field, *args, **kwargs):
        return pweb_form.show_input(field, **kwargs)


class ShowErrorMessage(StandaloneTag):
    tags = {"show_error_message"}

    def render(self, field, *args, **kwargs):
        return pweb_form.show_error_message(field, **kwargs)


class AddErrorClass(StandaloneTag):
    tags = {"add_error_class"}

    def render(self, field, *args, **kwargs):
        return pweb_form.add_error_class(field, **kwargs)


class SortableHeader(StandaloneTag):
    tags = {"sortable_header"}

    def render(self, name, *args, **kwargs):
        return pweb_table.sortable_header(name, **kwargs)
