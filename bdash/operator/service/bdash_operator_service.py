from pf_flask_auth.common.pffa_auth_config import PFFAuthConfig
from pf_flask_auth.model.pffa_default_model import DefaultModel
from pf_flask_auth.service.operator_service import OperatorService
from pf_flask_rest.form.common.pffr_field_data import FieldData
from pf_flask_rest.helper.pf_flask_form_crud_helper import FormCRUDHelper


class BDashOperatorService:
    operator_service = OperatorService()

    def get_crud_helper(self):
        return FormCRUDHelper(DefaultModel.OperatorModel)

    def list(self):
        search = ["firstName", "lastName", "email", "username"]
        return self.get_crud_helper().form_paginated_list(search_fields=search)

    def delete(self, model_id):
        return self.get_crud_helper().form_delete(model_id)

    def reset_password(self, form, model_id):
        operator = self.operator_service.get_operator_by_id(model_id)
        if not operator:
            form.definition.set_field_errors({"confirmPassword": "Invalid operator"})
            return False
        operator.password = form.confirmPassword
        operator.save()
        return True

    def create(self, form):
        identifier = PFFAuthConfig.loginIdentifier
        if identifier == "email":
            email_exist = self.operator_service.get_operator_by_email(form.email)
            if email_exist:
                form.definition.set_field_errors({"identifier": "Email already exist."})
                return False

        model = form.get_model()
        model.save()
        return True

    def get_details(self, model_id):
        return self.get_crud_helper().form_details(model_id)

    def update(self, form, model_id):
        identifier = PFFAuthConfig.loginIdentifier
        if identifier == "email":
            email_exist = self.operator_service.get_operator_by_email(form.email)
            if email_exist and model_id != email_exist.id:
                form.definition.set_field_errors({"identifier": "Email already exist."})
                return False

        existing_model = self.operator_service.get_operator_by_id(model_id)
        model = form.get_model(existing_model)
        model.save()
        return True

    def create_update_fields(self, form, is_create=True, klass="col-6"):
        identifier = PFFAuthConfig.loginIdentifier
        fields = [{"name": "firstName", "class": klass}, {"name": "lastName", "class": klass}]
        if identifier == "email":
            fields.append({"name": "email", "class": klass})
        else:
            fields.append({"name": "username", "class": klass})

        if is_create:
            fields.append({"name": "password", "class": klass})
        if PFFAuthConfig.operatorAdditionalFields:
            for additional_field in PFFAuthConfig.operatorAdditionalFields:
                fields.append({"name": additional_field["name"], "class": klass})
        return self.get_form_fields(form, fields)

    def get_form_fields(self, form, fields: list):
        for field in fields:
            if hasattr(form.definition, field["name"]):
                field["field"] = getattr(form.definition, field["name"])
        return fields
