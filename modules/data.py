class Data:
    def __init__(self, client_instance):
        self.client_instance = client_instance
        self.content = None
        self.signature = None
        self.data_description = {
            "codeType": "0",
            "encryptCode": "1",
            "zipCode": "0"
        }

    def set_content(self, content):
        self.content = content

    def set_signature(self, signature):
        self.signature = signature

    def set_data_description(self, code_type, encrypt_code, zip_code):
        self.data_description = {
            "codeType": code_type,
            "encryptCode": encrypt_code,
            "zipCode": zip_code
        }

    def get_data(self):
        return {
            "content": self.content,
            "signature": self.signature,
            "dataDescription": self.data_description
        }

    @staticmethod
    def set_data_all(content, signature, code_type, encrypt_code, zip_code):
        data_instance = Data(None)  # Creating an instance without client instance
        data_instance.set_content(content)
        data_instance.set_signature(signature)
        data_instance.set_data_description(code_type, encrypt_code, zip_code)
        return data_instance.get_data()
