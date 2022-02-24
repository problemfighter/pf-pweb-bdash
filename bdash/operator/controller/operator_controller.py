from flask import Blueprint, render_template

from bdash.form.pweb_form import pweb_form

url_prefix = "/operator"
operator_controller = Blueprint(
    "bdash_operator", __name__, url_prefix=url_prefix,
    template_folder="../../bdash-html",
    static_url_path="bdash",
    static_folder="../../bdash-static",
)


@operator_controller.route("/")
@operator_controller.route("/list")
def list():
    data_list = []
    return render_template("bdash/operator/list.html", data_list=data_list)


@operator_controller.route("/create", methods=['POST', 'GET'])
def create():
    data_list = []
    return render_template("bdash/operator/create.html", data_list=data_list)
