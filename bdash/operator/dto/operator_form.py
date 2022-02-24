from pf_flask_auth.common.pffa_auth_config import PFFAuthConfig


class OperatorForm(PFFAuthConfig.customOperatorDTO):

    class Meta:
        model = PFFAuthConfig.customOperatorModel
        load_instance = True
