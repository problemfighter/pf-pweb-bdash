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


class FormSelect(StandaloneTag):
    tags = {"form_select"}

    def render(self, name, options: list, *args, **kwargs):
        return pweb_form.form_select(name, options, **kwargs)


class SortableHeader(StandaloneTag):
    tags = {"sortable_header"}

    def render(self, name, *args, **kwargs):
        return pweb_table.sortable_header(name, **kwargs)


class Pagination(StandaloneTag):
    tags = {"pagination"}

    def render(self, current_page: int, total_page: int, *args, **kwargs):
        return pweb_table.pagination(current_page, total_page, **kwargs)


class SearchNameValue(StandaloneTag):
    tags = {"search_name_value"}

    def render(self, *args, **kwargs):
        return pweb_table.search_name_value()
