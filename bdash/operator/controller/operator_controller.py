from flask import Blueprint, render_template, redirect, url_for
from bdash.operator.dto.operator_form import OperatorForm, OperatorUpdateForm
from bdash.operator.service.bdash_operator_service import BDashOperatorService
from pf_flask_auth.common.pffa_auth_config import PFFAuthConfig

url_prefix = "/operator"
operator_controller = Blueprint(
    "bdash_operator", __name__, url_prefix=url_prefix,
    template_folder="../../bdash-html",
    static_url_path="bdash",
    static_folder="../../bdash-static",
)

bdash_operator_service = BDashOperatorService()

@operator_controller.route("/")
@operator_controller.route("/list")
def list():
    return render_template("bdash/operator/list.html", data=bdash_operator_service.list(), identifier=PFFAuthConfig.loginIdentifier)


@operator_controller.route("/create", methods=['POST', 'GET'])
def create():
    form = OperatorForm()
    if form.is_post_request() and form.is_valid_data():
        response = bdash_operator_service.create(form)
        if response:
            return redirect(url_for("bdash_operator.list"))
    data = {
        "identifier": PFFAuthConfig.loginIdentifier,
    }
    return render_template("bdash/operator/create.html", form=form.definition, data=data)


@operator_controller.route("/delete/<int:id>", methods=['GET'])
def delete(id: int):
    response = bdash_operator_service.delete(id)
    return redirect(url_for("bdash_operator.list"))


@operator_controller.route("/update/<int:id>", methods=['POST', 'GET'])
def update(id: int):
    form = OperatorUpdateForm()
    if form.is_post_request() and form.is_valid_data():
        response = bdash_operator_service.update(form, id)
        if response:
            return redirect(url_for("bdash_operator.list"))
    elif form.is_get_request():
        model = bdash_operator_service.get_details(id)
        if not model:
            return redirect(url_for("bdash_operator.list"))
        form.set_model_data(model)
        form.init_identifier(model)
    data = {
        "identifier": PFFAuthConfig.loginIdentifier,
    }
    return render_template("bdash/operator/update.html", form=form.definition, data=data, id=id)
