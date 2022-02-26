from marshmallow import fields
from pf_flask_auth.common.pffa_auth_config import PFFAuthConfig


class OperatorForm(PFFAuthConfig.customOperatorDTO):
    identifier = fields.String(required=True, error_messages={"required": "Please enter identifier."})
    password = fields.String(required=True, error_messages={"required": "Please enter password."}, type="password")

