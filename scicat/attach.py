#!/usr/bin/env python3
"""attach a file"""
from login import Login


class Attach:
    """attach a file"""

    def __init__(self):
        self.file = ""
        self.pid = ""
        self.token = ""
        self.attachment = {}

    def get_token(self):
        """get scicat token"""
        self.token = "uhY29G8F1YecRNzSoKeVqxRL5SfYciPxTO0u7ZB6lzyB3Urfv8GZSiSodvORNTkc"
        print(self.token)

    def create_json(self):
        """create dict for attachment in scicat format"""
        file_string = self.file
        attachment = {
            "thumbnail": file_string,
            "caption": self.file,
            "pid": self.pid
        }
        return attachment

    def attach(self, file, pid):
        """attach a file"""
        self.file = file
        self.pid = pid
        self.attachment = self.create_json()
        print(self.attachment)
        print(self.token)


def attach(file, pid):
    """attach a file"""
    attachment = Attach()
    attachment.attach(file, pid)
    # r=requests.post(dataset_url, json)


def main():
    """main"""
    file = "im.jpg"
    pid = "10.18390/fhuieraehiru"
    attach(file, pid)


if __name__ == "__main__":
    main()
