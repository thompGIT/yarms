/*****************************************************************************
 debug
******************************************************************************/
var g_DEBUG = 1
function debug(msg) {
    if(g_DEBUG) {
        console.log('[' + msg + ']');
    }
}

/******************************************************************************
 Utility Functions
******************************************************************************/
function ajax(url) {
    var xmlhttp = new XMLHttpRequest();
    debug("AJAX: " + url);
    xmlhttp.open("GET", url, false);
    xmlhttp.send();
    var resp = xmlhttp.responseText;
    debug("AJAX: " + resp);
    return resp;
}

dojo.ready(function() {
    debug('Testing 1..2..3..');
});

