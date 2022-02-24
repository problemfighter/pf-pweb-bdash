from flask import Blueprint, render_template
from marshmallow import fields
from pf_flask_rest.form.pf_app_form_def import FormAppDef

url_prefix = "/bdash-example"
bdash_example_blueprint = Blueprint(
    "bdash_exp", __name__, url_prefix=url_prefix,
    template_folder="bdash-example-html",
    static_url_path="bdash-example",
    static_folder="bdash-example-static",
)


class PersonForm(FormAppDef):
    first_name = fields.String(required=True, error_messages={"required": "Please enter first name"})
    last_name = fields.String(allow_none=True, default="NA")
    email = fields.Email(required=True, error_messages={"required": "Please enter email"})
    age = fields.Integer(required=True, error_messages={"required": "Please enter age"})
    income = fields.Float(allow_none=True)


@bdash_example_blueprint.route("/")
@bdash_example_blueprint.route("/form-example")
def form_example():
    form = PersonForm()
    return render_template("form.html", form=form.definition)
