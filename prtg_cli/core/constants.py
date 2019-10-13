PRTG_COUNT = 50000
PRTG_REQUEST_CONFIGS = {
    "status": {"route": "/api/getstatus.xml"},
    "passhash": {"route": "/api/getpasshash.htm"},
    "sensor_types": {"route": "/api/sensortypesinuse.json"},
    "probes": {
        "route": "/api/table.xml",
        "params": {
            "content": "probes",
            "columns": "objid,name",
            "filter_parentid": 0,
            "count": PRTG_COUNT,
        },
    },
    "groups": {
        "route": "/api/table.xml",
        "params": {
            "content": "groups",
            "columns": "objid,probe,group,type,name,parent",
            "count": PRTG_COUNT,
        },
    },
    "sensors": {
        "route": "/api/table.xml",
        "params": {
            "content": "sensors",
            "columns": "objid,probe,group,device,name,parent,sensor,status,lastvalue,priority,message",
            "count": PRTG_COUNT,
        },
    },
    "devices": {
        "route": "/api/table.xml",
        "params": {
            "content": "devices",
            "columns": "objid,probe,group,device,name,parent,sensor,status,lastvalue,priority",
            "count": PRTG_COUNT,
        },
    },
    "duplicate": {"route": "/api/duplicateobject.htm"},
    "pause": {"route": "/api/pause.htm", "params": {"action": 0}},
    "resume": {"route": "/api/pause.htm", "params": {"action": 1}},
    "delete": {"route": "/api/deleteobject.htm", "params": {"approve": 1}},
    "scan": {"route": "/api/scannow.htm", "params": {}},
}
