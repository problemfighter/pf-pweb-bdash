from flask import request
from bdash.security.google_recaptcha import GoogleRecaptcha


class WebSecurity:

    @staticmethod
    def recaptcha(site_key, action="recaptcha"):
        google_recaptcha = GoogleRecaptcha()
        return google_recaptcha.recaptcha(site_key=site_key, action=action)

    @staticmethod
    def verify_recaptcha(secret, token=None):
        google_recaptcha = GoogleRecaptcha()
        if not token:
            token = request.form.get('recaptchaToken')
        return google_recaptcha.verify(secret=secret, token=token)
