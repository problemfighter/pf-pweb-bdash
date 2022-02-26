from marshmallow import fields
from pf_flask_auth.common.pffa_auth_config import PFFAuthConfig


class OperatorForm(PFFAuthConfig.customOperatorDTO):
    identifier = fields.String(required=True, error_messages={"required": "Please enter identifier."})
    password = fields.String(required=True, error_messages={"required": "Please enter password."}, type="password")


class OperatorUpdateForm(PFFAuthConfig.customOperatorDTO):
    identifier = fields.String(required=True, error_messages={"required": "Please enter identifier."})

    def init_identifier(self, model):
        identifier = PFFAuthConfig.loginIdentifier
        if identifier == "email":
            self.definition.identifier.value = model.email
        else:
            self.definition.identifier.value = model.username
