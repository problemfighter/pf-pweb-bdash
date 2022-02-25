from flask import Blueprint, render_template
from marshmallow import fields
from pf_flask_rest.form.pf_app_form_def import FormAppDef
from pf_flask_rest_com.common.pffrc_enum_helper import BaseEnum, EnumField

url_prefix = "/bdash-example"
bdash_example_blueprint = Blueprint(
    "bdash_exp", __name__, url_prefix=url_prefix,
    template_folder="bdash-example-html",
    static_url_path="bdash-example",
    static_folder="bdash-example-static",
)


class GenderEnum(BaseEnum):
    Brother = "B"
    Sister = "S"


class PersonForm(FormAppDef):
    firstName = fields.String(
        required=True,
        error_messages={"required": "Please enter first name"},
        label="First Name",
        topAttr={"id": "a b c", "class": "asd"},
    )
    lastName = fields.String(allow_none=True, default="NA", helpText="Optional Data")
    email = fields.Email(required=True, error_messages={"required": "Please enter email"})
    age = fields.Integer(required=True, error_messages={"required": "Please enter age"})
    income = fields.Float(allow_none=True)

    password = fields.String(required=True, error_messages={"required": "Please enter password"}, type="password")
    description = fields.String(required=True, error_messages={"required": "Please enter description"}, type="textarea")
    gender = EnumField(GenderEnum, required=True, error_messages={"required": "Please enter gender"})


@bdash_example_blueprint.route("/")
@bdash_example_blueprint.route("/form-example", methods=['POST', 'GET'])
def form_example():
    form = PersonForm()
    if form.is_post_request() and form.is_valid_data():
        return "Data is valid"
    return render_template("form.html", form=form.definition)


@bdash_example_blueprint.route("/table")
def table():
    return render_template("table.html")
