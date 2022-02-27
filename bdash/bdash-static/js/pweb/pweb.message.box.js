PF.messageBox = (function () {
    let messageHtml = '<div style="min-height:50px; min-width: 300px; max-width: 600px; position: fixed; top: 0; left: 0; right: 0; margin: 0 auto; text-align: center; z-index: 2000;" class="alert">';
    messageHtml += '<span class="message" style="font-weight: bold;"></span></div>';
    let timeOut = null;

    function hideMessage() {
        jQuery(".alert").hide();
        timeOut = null;
    }


    function checkTimeOut() {
        if (timeOut !== null) {
            clearTimeout(timeOut);
        }
    }

    return {

        showMessage: function (success, message) {
            if (!jQuery(".alert").length) {
                jQuery(document.body).append(messageHtml);
            }
            let messageType = "alert-success";
            if (success !== true) {
                messageType = "alert-danger";
            }

            checkTimeOut();
            let messageElement = jQuery(document.body).find(".alert");
            messageElement.find(".message").text(message);
            messageElement.removeClass("alert-success").removeClass("alert-danger").addClass(messageType);
            messageElement.show();
            timeOut = setTimeout(function () {
                hideMessage();
            }, 5000);
        }
    }
}());
