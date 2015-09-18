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

function sanitizeRequestData(data) {
    nData = [];
    if (data.pk != undefined) {
        nData['id']= data.pk;
    }
    if (data.fields != undefined && typeof data.fields) {
        for (key in data.fields) {
            nData[key] = data.fields[key]
        }
    }
    return nData;
}

function requests(http, url, type, form, callback) {
    if (typeof form == 'string') {
        data = $(form).serialize();
    } else {
        data = form;
    }

    if (data != null) {
        data = $.param(data);
    }

    if (type == 'post') {
        http.post(url, data).then(callback);
    } else if (type == 'get') {
        http.get(url).then(callback);
    }
}