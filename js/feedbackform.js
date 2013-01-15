dojo.require("dojo.data.ItemFileReadStore");
dojo.require("dojox.data.KeyValueStore");
dojo.require("dojox.grid.DataGrid");

//-- Initial startup
dojo.ready(function() {
    initEmployeeSelector();
});

//-- Handle events

//-- Update the table with live information from the database
function initEmployeeSelector() {

    // Fetch the update from the database
    var resp = ajax('./cgi/jsIface.py?op=getEmployeeNames');
    if (resp != '/n') {

        // Create the new datastore
        var tokens = resp.split("\n");
        var i = 0;
        var data_list = new Array();
        while (i<tokens.length) {
            data_list.push({'name':tokens[i]});
            i++;
        }
        var datastore = new dojox.data.KeyValueStore({data: data_list});

        // Push the content to the grid
        //var grid = dijit.byId("grid_macFilter");
        //grid.setStore(datastore);
    }
}

