from bdash.dashboard.controller.bdash_controller import bdash_controller
from bdash.jinja.pweb_jinja_registry import registry
from bdash.operator.controller.operator_controller import operator_controller
from pf_flask_web.system12.pweb_interfaces import PWebAppRegistry


class BDashRegistry(PWebAppRegistry):

    def run_on_start(self, pweb_app):
        self._register_jinja_functions(pweb_app)

    def register_model(self, pweb_db):
        pass

    def register_controller(self, pweb_app):
        pweb_app.register_blueprint(bdash_controller)
        pweb_app.register_blueprint(operator_controller)

    def _register_jinja_functions(self, pweb_app):
        if pweb_app and pweb_app.jinja_env and pweb_app.jinja_env.globals:
            for method in registry:
                if method not in pweb_app.jinja_env.globals:
                    pweb_app.jinja_env.globals[method] = registry[method]
