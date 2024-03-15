class ReturnStateInfo:
    def __init__(self, client_instance):
        self.client_instance = client_instance
        self.return_code = ""
        self.return_message = ""

    def set_return_code(self, return_code):
        self.return_code = return_code

    def set_return_message(self, return_message):
        self.return_message = return_message

    def get_return_state_info(self):
        return {
            "returnCode": self.return_code,
            "returnMessage": self.return_message
        }

    @staticmethod
    def set_return_state_info(return_code, return_message):
        return_state_info_instance = ReturnStateInfo(None)  # Creating an instance without client instance
        return_state_info_instance.set_return_code(return_code)
        return_state_info_instance.set_return_message(return_message)
        return return_state_info_instance.get_return_state_info()
