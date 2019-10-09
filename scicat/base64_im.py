#!/usr/bin/env python3
"""generate base64 image"""
import base64


class Base64Im:
    """generate base64 image"""
    filename = "raw_data_3D_detectors.png"
    image = ""
    header = "data:image/png;base64,"

    def set_filename(self, filename):
        """set filename"""
        self.filename = filename

    def convert(self, filename="raw_data_3D_detectors.png"):
        """convert image"""
        self.filename = filename
        with open(self.filename, "rb") as image_file:
            data = image_file.read()
            image_bytes = base64.b64encode(data)
            image_str = image_bytes.decode('UTF-8')
            self.image = self.header + image_str


def main():
    """main"""
    base = Base64Im()
    print(base.image[0:50])


if __name__ == '__main__':
    main()
