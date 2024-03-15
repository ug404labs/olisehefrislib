class GlobalData:
    def __init__(self, client_instance):
        self.client_instance = client_instance

    def set_global_key(self, key, value):
        self.client_instance.global_info[key] = value

    def set_global(self, data):
        try:
            global_keys = [
                "appId", "version", "dataExchangeId", "interfaceCode",
                "requestCode", "requestTime", "responseCode", "userName",
                "deviceMAC", "deviceNo", "tin", "brn", "taxpayerID",
                "longitude", "latitude"
            ]

            lowercase_keys = [key.lower() for key in global_keys]

            for key, value in data.items():
                if key.lower() in lowercase_keys:
                    real_key = global_keys[lowercase_keys.index(key.lower())]
                    self.client_instance.global_info[real_key] = value
                elif key.lower() == "extendfield":
                    # Handle extendField separately
                    self._set_extend_field(value)
        except Exception as e:
            print(f"Error setting global info: {e}")

    def set_extend_reference(self, reference):
        try:
            # Set the reference number under extendField
            self.client_instance._extend_field_info['referenceNo'] = reference
        except Exception as e:
            print(f"Error setting extend reference: {e}")

    def set_extend_date_format(self, date_format):
        try:
            # Set the date format under extendField
            self.client_instance._extend_field_info['responseDateFormat'] = date_format
        except Exception as e:
            print(f"Error setting extend date format: {e}")

    def set_extend_time_format(self, time_format):
        try:
            # Set the time format under extendField
            self.client_instance._extend_field_info['responseTimeFormat'] = time_format
        except Exception as e:
            print(f"Error setting extend time format: {e}")

    def _set_extend_field(self, extend_data):
        try:
            for key, value in extend_data.items():
                self.client_instance._extend_field_info[key] = value
        except Exception as e:
            print(f"Error setting extendField: {e}")
