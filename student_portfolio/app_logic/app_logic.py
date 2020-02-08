import json
import requests

def dummy_post_request():
    # Define API ENDPOINT
    API_ENDPOINT = "https://www.blackrock.com/tools/hackathon/portfolio-analysis"

    # data to be sent for request
    data = {
            "calculateExposures": "true",
            "calculatePerformance": "true",
            "positions": "OSMCX~17.49|HLIRX~14.77|LGIH~12.58|CWICX~1.93|IEI~17.71|RBESX~9.98|CGPFX~11.38|BCMCX~14.16|"
    }

    # sending post request and saving response as response object
    r = requests.post(url=API_ENDPOINT,data=data)
    return_data = r.text
    json_return = dict(json.loads(return_data)) # this returned json is converted to dict
    print(type(json_return))
