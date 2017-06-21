import json

option = {
            'tooltip': {
                'show': True
            },
            'legend': {
                'data':['销量']
            },
            'xAxis' : [
                {
                    'type' : 'time',
                    'data' : ["2015","2016","2017","2018","2019","2020"]
                }
            ],
            'yAxis' : [
                {
                    'type' : 'value'
                }
            ],
            'series' : [
                {
                    "name":"销量",
                    "type":"line",
                    "data":[5, 20, 40, 10, 10, 20]
                }
            ]
        }
if __name__=='__main__':
	print(option)
	s=json.dumps(option)
	print(s)