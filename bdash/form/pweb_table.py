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

    def _page_number_calculate(self, current_page: int, total_page: int):
        delta = 2
        left = current_page - delta
        right = current_page + delta + 1
        range_list = []
        range_with_dots = []
        temp = 0

        for i in range(1, total_page + 1):
            if i == 1 or i == total_page or left <= i < right:
                range_list.append(i)

        for i in range_list:
            if temp:
                if (i - temp) == 2:
                    range_with_dots.append(temp + 1)
                elif (i - temp) != 1:
                    range_with_dots.append("...")
            range_with_dots.append(i)
            temp = i
        return range_with_dots

    def _prepare_pagination_link(self, current_page: int, total_page: int):
        pagination_item = self._page_number_calculate(current_page, total_page)
        pagination_details = []
        url_info = self.request_helper.get_url_info()
        for pagination in pagination_item:
            selected = False
            url = "#"
            if pagination == current_page:
                selected = True
            elif pagination != "...":
                url = pffr_url_processor.add_query_params(url_info.relativeURLWithParam, {PFFRConfig.get_page_param: pagination})
            pagination_details.append({
                "text": pagination,
                "url": url,
                "selected": selected,
            })
        return pagination_details

    def pagination(self, current_page: int, total_page: int, **kwargs):
        per_page = PFFRConfig.total_item_per_page
        if total_page < per_page:
            return ""
        template = self.pweb_form_common.get_template("pagination")
        data = {
            "prev": "",
            "pages": self._prepare_pagination_link(current_page, total_page),
            "next": "",
        }
        return render_template_string(template, conf=data)


pweb_table = PWebTable()
