function getCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for(var i=0;i < ca.length;i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1,c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
    }
    return null;
}

function requests(url, type, form, callback) {
    if (typeof form == 'string') {
        data = $(form).serialize();
    } else {
        data = form;
    }

    if (data != null) {
        data.csrfmiddlewaretoken = getCookie('csrftoken');
    }

    $.ajax({
        url: url,
        dataType: 'json',
        type: type,
        data: data,
        success: callback,
        header: {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }

    });
}