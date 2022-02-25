from urllib import parse
from urllib.parse import urlparse

from flask import render_template_string
from bdash.form.pweb_form_common import PWebFormCommon
from pf_flask_rest.common.pf_flask_rest_config import PFFRConfig
from pf_flask_rest_com.common.pffr_url_processor import pffr_url_processor
from pf_flask_rest_com.pf_flask_request_helper import RequestHelper
from pf_py_text.pfpt_string_util import PFPTStringUtil


class PWebTable:
    pweb_form_common = PWebFormCommon()
    request_helper = RequestHelper()

    def _get_header_display_name(self, name, **kwargs):
        display_name = kwargs.get("display_name")
        if not display_name:
            display_name = PFPTStringUtil.human_readable(name)
        return display_name

    def sortable_header(self, name, **kwargs):
        display_name = self._get_header_display_name(name, **kwargs)
        icon = "fa-sort"
        sort_field_key = PFFRConfig.sort_field_param
        sort_order_key = PFFRConfig.sort_order_param
        url_sort_field = self.request_helper.get_query_params_value(sort_field_key, None)
        url_sort_order = self.request_helper.get_query_params_value(sort_order_key, None)
        sort_fields = {sort_field_key: name, sort_order_key: "asc"}
        if url_sort_field and url_sort_field == name:
            icon = "fa-sort-down"
            order = "asc"
            if url_sort_order == "asc":
                icon = "fa-sort-up"
                order = "desc"
            sort_fields[sort_order_key] = order

        url_info = self.request_helper.get_url_info()
        url = pffr_url_processor.add_query_params(url_info.relativeURLWithParam, sort_fields)
        template = self.pweb_form_common.get_template("sortable-header")
        data = {
            "display_name": display_name,
            "icon": icon,
            "url": url
        }
        return render_template_string(template, conf=data)


pweb_table = PWebTable()
