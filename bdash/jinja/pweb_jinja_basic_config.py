from pf_flask_web.system12.pweb_registry import PWebRegistry


class PwebJinjaBasicConfig:

    @staticmethod
    def get_app_name():
        if PWebRegistry.config.APP_NAME:
            return PWebRegistry.config.APP_NAME
        return "PWeb BDash App"
