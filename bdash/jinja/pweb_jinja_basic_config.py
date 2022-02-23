from pf_flask_auth.data.pffa_form_auth_data import FormAuthData
from pf_flask_web.system12.pweb_registry import PWebRegistry


class PwebJinjaBasicConfig:

    @staticmethod
    def get_app_name():
        if PWebRegistry.config.APP_NAME:
            return PWebRegistry.config.APP_NAME
        return "PWeb BDash App"

    @staticmethod
    def get_operator_name():
        name = "BDash Operator"
        try:
            form_auth_data: FormAuthData = FormAuthData.ins().get_logged_in_session()
            if form_auth_data.firstName:
                name = form_auth_data.firstName
            if form_auth_data.lastName:
                name = " " + form_auth_data.lastName
        except:
            pass
        return name
