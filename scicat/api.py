#!/usr/bin/env python3
"""fetch api """


class Api:
    """ fetch api"""

    api = ""
    base = ""

    def __init__(self):
        self.base = "https://scitest.esss.lu.se/"
        self.api = self.base + "api/v3/"

    def set_api(self, api):
        """set api"""
        self.api = api


def main():
    """main"""
    api = Api()
    print(api.api)


if __name__ == "__main__":
    main()
