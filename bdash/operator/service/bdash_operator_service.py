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

    def create(self, form):
        identifier = PFFAuthConfig.loginIdentifier
        is_valid = True
        if identifier == "email":
            email_exist = self.operator_service.get_operator_by_email(form.identifier)
            form.definition.email.value = form.identifier
            form.definition.username.value = None
            if email_exist:
                is_valid = False
                form.definition.set_field_errors({"identifier": "Email already exist."})
        else:
            form.definition.username.value = form.identifier
            form.definition.email.value = None

        if is_valid:
            model = self.init_model_data(DefaultModel.OperatorModel(), form.definition)
            model.save()
            return True
        return False

    def get_details(self, model_id):
        return self.get_crud_helper().form_details(model_id)

    def update(self, form, model_id):
        identifier = PFFAuthConfig.loginIdentifier
        is_valid = True
        if identifier == "email":
            email_exist = self.operator_service.get_operator_by_email(form.identifier)
            form.definition.email.value = form.identifier
            if email_exist and model_id != email_exist.id:
                is_valid = False
                form.definition.set_field_errors({"identifier": "Email already exist."})
        else:
            form.definition.username.value = form.identifier

        if is_valid:
            existing_model = self.get_crud_helper().form_details(model_id)
            if not existing_model:
                return False
            model = self.init_model_data(existing_model, form.definition)
            model.save()
            return True
        return False

    def init_model_data(self, model, data):
        attrs = dir(data)
        for key in attrs:
            field = getattr(data, key)
            if not key.startswith("_") and hasattr(model, key) and isinstance(field, FieldData):
                setattr(model, key, field.value)
        return model
