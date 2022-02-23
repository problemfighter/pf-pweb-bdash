from bdash.jinja.pweb_jinja_basic_config import PwebJinjaBasicConfig

registry = {
    "pweb_app_name": PwebJinjaBasicConfig.get_app_name(),
    "loggedin_operator_name": PwebJinjaBasicConfig.get_operator_name
}
