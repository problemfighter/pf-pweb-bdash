from flask import Blueprint

url_prefix = "/"
bdash_controller = Blueprint(
    "bdash_controller", __name__, url_prefix=url_prefix,
    template_folder="../bdash-html"
)


@bdash_controller.route("/dashboard")
def dashboard():
    return "Dashboard"
