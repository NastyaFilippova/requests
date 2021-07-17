import requests

TOKEN = ""

class YaUploader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def get_headers(self):
        return {"Accept": "application/json", "Authorization": TOKEN}

    def _get_upload_link(self, filename):
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": f"netology/{filename}", "overwrite": True}
        res = requests.get(url=url, params=params, headers=headers)
        return res.json()

    def upload(self, filename):
        href = self._get_upload_link(filename=filename).get("href", "")
        upload = requests.put(url=href, data=open(self.file_path, 'rb'))
        if upload.status_code == 201:
            print("Успешно")


if __name__ == '__main__':
    uploader = YaUploader('C:/Users/aphilippova/PycharmProjects/test.txt')
    uploader.upload('test.txt')
