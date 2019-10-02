#!/usr/bin/env python3
"""attach a file"""


class Attach:
    """attach a file"""

    def attach(self, file, pid):
        """attach a file"""
        print(file)
        print(pid)


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
