from bdash.controller.bdash_controller import bdash_controller
from pf_flask_web.system12.pweb_interfaces import PWebAppRegistry


class BDashRegistry(PWebAppRegistry):

    def run_on_start(self, pweb_app):
        pass

    def register_model(self, pweb_db):
        pass

    def register_controller(self, pweb_app):
        pweb_app.register_blueprint(bdash_controller)

