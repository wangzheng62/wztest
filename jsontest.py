import json

option = {
            tooltip: {
                show: true
            },
            legend: {
                data:['销量']
            },
            xAxis : [
                {
                    type : 'time',
                    data : ["2015","2016","2017","2018","2019","2020"]
                }
            ],
            yAxis : [
                {
                    type : 'value'
                }
            ],
            series : [
                {
                    "name":"销量",
                    "type":"line",
                    "data":[5, 20, 40, 10, 10, 20]
                }
            ]
        };