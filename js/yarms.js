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
         "dijit/form/FilteringSelect",
         "dijit/form/ComboBox",
         "dojo/store/Memory"
], function (ready, Select, Memory) {

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
            DataStore_Employees = new dojo.store.Memory({});    
            while (i<tokens.length) {
                if (tokens[i].length > 0)
                    DataStore_Employees.put({name:tokens[i]});
                i++;
            }            
        }
    }

    //-- Initialize the target employee selector 
    function InitEmployeeSelector() {            
        var s = new dijit.form.ComboBox({
            id: "target_select",
            store: DataStore_Employees,
            onChange: function(target){
                var resp = ajax('./cgi/jsIface.py?op=getEmployeeInfoByName&name=' + target);
                if (resp != '\n') {   
                    var tokens = resp.split(",");
                    dojo.byId("target_title").innerHTML = tokens[2];
                    resp = ajax('./cgi/jsIface.py?op=getEmployeeInfoByKey&key=' + tokens[3]);
                    if (resp != '\n') {
                        var tokens = resp.split(",");
                        dojo.byId("target_super").innerHTML = tokens[0];
                    }
                }
            }
        }, "target_select");      
    }

});

