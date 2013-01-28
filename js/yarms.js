/******************************************************************************
 Utility Functions
******************************************************************************/

var g_DEBUG = 0
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
var DataStore_FeedbackCategories;
var Target_key = -1;
var Provider_key = -1;

require(["dojo/ready",
         "dojo/data/ItemFileReadStore",
         "dojox/data/KeyValueStore", 
         "dojox/grid/DataGrid", 
         "dijit/form/FilteringSelect",
         "dijit/form/ComboBox",
         "dojo/store/Memory",
         "dijit/form/SimpleTextarea",
         "dojox/form/BusyButton"
], function (ready, Select, Memory, SimpleTextarea) {

    //-- Initial startup
    ready(function() {
        BuildDataStores();
        InitCategoryLabels();
        InitEmployeeSelector();
        InitFeebackAreas();
    });
           
    //-- Build Data Stores
    function BuildDataStores() {
        var i, resp, tokens, data_list;
            
        // Create the employees datastore
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
                   
        // Create the feedback categories datastore
        resp = ajax('./cgi/jsIface.py?op=getFeedbackQuestions');
        if (resp != '/n') {
            i = 0;
            var lines = resp.split("\n");
            DataStore_FeedbackCategories = new dojo.store.Memory({});    
            while (i<lines.length) {
                if (lines[i].length > 0)
                    var tokens = lines[i].split("`");                    
                    DataStore_FeedbackCategories.put({id:tokens[0],text:tokens[1]});
                i++;
            }            
        }        
    }

    //-- Initialize Category Labels
    function InitCategoryLabels() {
        dojo.byId("feedbackLabel_1").innerHTML = DataStore_FeedbackCategories.get(1).text;
        dojo.byId("feedbackLabel_2").innerHTML = DataStore_FeedbackCategories.get(2).text;
        dojo.byId("feedbackLabel_3").innerHTML = DataStore_FeedbackCategories.get(3).text;
        dojo.byId("feedbackLabel_4").innerHTML = DataStore_FeedbackCategories.get(4).text;
        dojo.byId("feedbackLabel_5").innerHTML = DataStore_FeedbackCategories.get(5).text;
        dojo.byId("feedbackLabel_6").innerHTML = DataStore_FeedbackCategories.get(6).text;
    }
    
    //-- Initialize all employee selection boxes
    function InitEmployeeSelector() {      
    
        //-- Initialize the target employee selector       
        var empSelect = new dijit.form.ComboBox({
            id: "target_select",
            store: DataStore_Employees,
            onChange: function(target){
                var resp = ajax('./cgi/jsIface.py?op=getEmployeeInfoByName&name=' + target);
                if (resp != '\n') {   
                    var tokens = resp.split(",");
                    Target_key = tokens[0];
                    dojo.byId("target_title").innerHTML = tokens[2];
                    resp = ajax('./cgi/jsIface.py?op=getEmployeeInfoByKey&key=' + tokens[3]);
                    if (resp != '\n') {
                        var tokens = resp.split(",");
                        dojo.byId("target_super").innerHTML = tokens[0];
                    }
                }
            }
        }, "target_select");      
        
        //-- Initialize the reviewing employee selector 
        var revSelect = new dijit.form.ComboBox({
            id: "reviewer_select",
            store: DataStore_Employees,
            onChange: function(target){
                var resp = ajax('./cgi/jsIface.py?op=getEmployeeInfoByName&name=' + target);
                if (resp != '\n') {   
                    var tokens = resp.split(",");
                    Provider_key = tokens[0];
                    dojo.byId("reviewer_title").innerHTML = tokens[2];
                    resp = ajax('./cgi/jsIface.py?op=getEmployeeInfoByKey&key=' + tokens[3]);
                    if (resp != '\n') {
                        var tokens = resp.split(",");
                        dojo.byId("reviewer_super").innerHTML = tokens[0];
                    }
                }
            }
        }, "reviewer_select");    
    }
    
    //-- Initialize Feeback Input Areas
    function InitFeebackAreas() {
    
        //-- Text input area
        for (var i=1; i<=6; i++) {
            var inputName = 'feedbackInput_' + i.toString();
            var textarea = new dijit.form.SimpleTextarea({
                name: inputName,
                style: 'width:100%; height:95%;'
            }, inputName);
        }
        
        //-- Submit button
        var button = new dojox.form.BusyButton({
            id: 'formSubmitButton',
            busyLabel: 'Submitting...',
            label: 'Submit Feedback',
            timeout: 2000,
            onClick: SubmitFeedback
        }, 'formSubmitButton');
    }
    
    //-- Submit feedback
    function SubmitFeedback() {        
        for (var i=1; i<=6; i++) {                                     
            var cmd = './cgi/jsIface.py?op=submitFeedback';
            cmd += '&target_key='   + Target_key;
            cmd += '&provider_key=' + Provider_key;
            cmd += '&category_key=' + i.toString();
            cmd += '&comment='      + dijit.byId('feedbackInput_' + i.toString()).get('value');
            ajax(cmd);
        }               
    }
});

