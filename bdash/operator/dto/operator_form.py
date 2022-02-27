from marshmallow import fields
from pf_flask_auth.common.pffa_auth_config import PFFAuthConfig
from pf_flask_auth.model.pffa_default_model import DefaultModel

def OperatorCommonForm(exclude_fields=[]):
    is_email_required = False
    is_username_required = False
    if PFFAuthConfig.loginIdentifier == "email":
        is_email_required = True
    else:
        is_username_required = True

    class OperatorFormInternal(PFFAuthConfig.customOperatorDTO):
        email = fields.Email(required=is_email_required, error_messages={"required": "Please enter email."})
        username = fields.String(required=is_username_required, error_messages={"required": "Please enter username."})
        password = fields.String(required=True, error_messages={"required": "Please enter password."}, type="password")

        class Meta:
            model = DefaultModel.OperatorModel
            load_instance = True
            exclude = exclude_fields

    return OperatorFormInternal()


def OperatorForm():
    return OperatorCommonForm()


def OperatorUpdateForm():
    return OperatorCommonForm(["password"])
