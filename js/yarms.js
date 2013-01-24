/******************************************************************************
 Utility Functions
******************************************************************************/

var g_DEBUG = 1
function debug(msg) {
    if(g_DEBUG) {
        console.log('[' + msg + ']');
    }
}

function ajax(url) {
    var xmlhttp = new XMLHttpRequest();
    debug("AJAX: " + url);
    xmlhttp.open("GET", url, false);
    xmlhttp.send();
    var resp = xmlhttp.responseText;
    debug("AJAX: " + resp);
    return resp;
}

/******************************************************************************
 Global Variables
******************************************************************************/
var DataStore_Employees;

require(["dojo/ready",
         "dojo/data/ItemFileReadStore",
         "dojox/data/KeyValueStore", 
         "dojox/grid/DataGrid", 
         "dijit/form/FilteringSelect"
], function (ready, Select) {

    //-- Initial startup
    ready(function() {
        BuildDataStores();
        InitEmployeeSelector();
    });
    
    //-- Build Data Stores
    function BuildDataStores() {
        var i, resp, tokens, data_list;
            
        // Create the employees datastore with all non-null names returned
        resp = ajax('./cgi/jsIface.py?op=getEmployeeNames');
        if (resp != '/n') {
            i = 0;
            tokens = resp.split("\n");
            data_list = new Array();
            while (i<tokens.length) {
                if (tokens[i].length > 0)
                    data_list.push({'name':tokens[i]});
                i++;
            }
            DataStore_Employees = new dojox.data.KeyValueStore({data: data_list});
        }
    }

    //-- Update the table with live information from the database
    function InitEmployeeSelector() {            
        var s = new dijit.form.FilteringSelect({
            store: DataStore_Employees
        }, "target_select");
        s.startup();
    };
    
});

