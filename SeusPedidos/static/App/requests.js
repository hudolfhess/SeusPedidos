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
    nData = {};
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

function showMessage(result) {
    if (result.data.success == 1){
        $('<div class="alert alert-dismissible alert-success"><button type="button" class="close" data-dismiss="alert">X</button>Dados salvos com sucesso!</div>').insertAfter('form').fadeOut(2000);
    } else {
        $('<div class="alert alert-dismissible alert-warning"><button type="button" class="close" data-dismiss="alert">X</button>Oops! Nao foi possivel salvar os dados.</div>').insertAfter('form').fadeOut(6000);
        if (typeof result.data.error != 'undefined') {
            for (key in result.data.error) {
                $('input[name=' + key + ']').parents('.form-group').addClass('has-error');
            }
        }
    }
}

function requests(http, url, type, form, callback) {
    if (typeof form == 'string') {
        data = $(form).serialize();
    } else {
        data = form;
    }
    if (data != null) {
        delete data['$$hashKey'];
        data = $.param(data);
    }

    if (type == 'post') {
        http.post(url, data).then(callback);
    } else if (type == 'put') {
        http.put(url, data).then(callback);
    } else if (type == 'get') {
        http.get(url + '?' + data).then(callback);
    } else if (type == 'delete') {
        http.delete(url + '?' + data).then(callback);
    }
}