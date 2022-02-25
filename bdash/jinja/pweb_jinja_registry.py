from bdash.jinja.pweb_jinja_basic_config import PwebJinjaBasicConfig

global_variables = {
    "pweb_app_name": PwebJinjaBasicConfig.get_app_name(),
    "loggedin_operator_name": PwebJinjaBasicConfig.get_operator_name,
}

extensions = [
    "bdash.form.tags.tag_definitions.ShowInput",
    "bdash.form.tags.tag_definitions.ShowErrorMessage",
    "bdash.form.tags.tag_definitions.AddErrorClass",
    "bdash.form.tags.tag_definitions.SortableHeader",
]
