import requests


class GoogleRecaptcha:
    VERIFY_URL = "https://www.google.com/recaptcha/api/siteverify"

    def recaptcha(self, site_key, action, input_id=None):
        text_input = ""
        if not input_id:
            input_id = "g-recaptcha-token-input"
            text_input = f"""
                <input type="hidden" name="recaptchaToken" id="{input_id}">
            """

        return f"""
        {text_input}
        <script src="https://www.google.com/recaptcha/api.js?render={site_key}"></script>
        <script>
            grecaptcha.ready(function() {{
              grecaptcha.execute('{site_key}', {{action: '{action}'}}).then(function(token) {{
                  document.getElementById('{input_id}').value=token
              }});
            }});
        </script>
        """

    def verify(self, secret, token):
        json_data = {
            "secret": secret,
            "response": token,
        }
        api_response = requests.get(self.VERIFY_URL, params=json_data)
        if api_response.status_code == 200:
            response_json = api_response.json()
            if response_json and response_json["success"] and response_json["success"] > 0.0:
                return True
        return False
