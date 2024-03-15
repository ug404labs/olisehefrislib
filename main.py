from modules.globaldata import GlobalData
from modules.data import Data
from modules.returnstateinfo import ReturnStateInfo
import requests


class Client:
    _extend_field_info = {}

    def __init__(self, url):
        self.url = url
        self.Global_Data = GlobalData(self)
        self.Data = Data(self)
        self.ReturnStateInfo = ReturnStateInfo(self)

    def set_global_key(self, key, value):
        try:
            global_keys = {
                "appid": "appId",
                "version": "version",
                "dataexchangeid": "dataExchangeId",
                "interfacecode": "interfaceCode",
                "requestcode": "requestCode",
                "requesttime": "requestTime",
                "responsecode": "responseCode",
                "username": "userName",
                "devicemac": "deviceMAC",
                "deviceno": "deviceNo",
                "tin": "tin",
                "brn": "brn",
                "taxpayerid": "taxpayerID",
                "longitude": "longitude",
                "latitude": "latitude"
            }

            if key.lower() in global_keys:
                real_key = global_keys[key.lower()]
                self.global_info[real_key] = value
        except Exception as e:
            print(f"Error setting {key}: {e}")

    def set_extend_reference(self, reference):
        self.Global_Data.set_extend_reference(reference)

    def set_extend_date_format(self, date_format):
        self.Global_Data.set_extend_date_format(date_format)

    def set_extend_time_format(self, time_format):
        self.Global_Data.set_extend_time_format(time_format)

    def send_request(self):
        initial_json = {
            "data": self.Data.get_data(),
            "globalInfo": self.Global.get_global_info(),
            "returnStateInfo": self.ReturnStateInfo.get_return_state_info()
        }

        try:
            response = requests.post(self.url, json=initial_json)
            # Check response status code
            if response.status_code == 200:
                print("Request sent successfully!")
                print("Response:", response.json())  # If you want to print the response
            else:
                print("Failed to send request. Status code:", response.status_code)
        except Exception as e:
            print("Error sending request:", e)
