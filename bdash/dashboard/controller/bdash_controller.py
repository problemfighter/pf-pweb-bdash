from flask import Blueprint, render_template

url_prefix = "/"
bdash_controller = Blueprint(
    "bdash", __name__, url_prefix=url_prefix,
    template_folder="../../bdash-html",
    static_url_path="bdash",
    static_folder="../../bdash-static",
)


@bdash_controller.route("/dashboard")
def dashboard():
    return render_template("bdash/dashboard/dashboard.html")
