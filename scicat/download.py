#!/usr/bin/env python3
"""downloader"""
import sys
import os
import time
import datetime
import re
import zipfile
import io
from typing import Tuple

import requests
from scicat import api


class SciCat:
    """base class"""
    _scicat_file_server = "https://scicatfileserver.esss.dk/"

    def __init__(self, username: str = None, password: str = None, timeout: int = 0.25):
        """
        Create a SciCat instance and obtain a login token.

        :param username: SciCat username
        :param password: SciCat password
        :param timeout: Timeout when obtaining files.
        """
        self.username = username
        self.token = None
        self.timeout = timeout
        self.bigtimeout = datetime.timedelta(seconds=60)
        self.scicat = api.Api()
        self.token = self.get_token(password)

    def get_token(self, password: str) -> str:
        """
        Obtain a login token from Scicat from your stored username and password supplied

        :param password: Password to access SciCat
        :return: Token for login
        """
        response = requests.post(self.scicat.api + "Users/login",
                                 json=dict(username=self.username, password=password))
        result = response.json()
        if response.status_code != 200:
            print("Login failed: {}".format(response.status_code))
            raise ConnectionError
        token = result.get("id")
        return token

    def download(self, file_path: str, file_names: list, extract_location: str = None) -> Tuple[str, list]:
        """
        Download a file/s from SciCat.

        :param file_path: Where is the file on SciCat?
        :param file_names: Which files do you want to download?
        :param extract_location: Where do you want the files to be saved?
        :return: Downloaded file path and downloaded file names as tuple.
        """

        response = requests.post(
            url=self.scicat.api + 'Users/jwt?access_token={}'.format(self.token))
        json_response = response.json()
        jwt = json_response["jwt"]

        download_dict = {
            "jwt": jwt,
            "base": file_path,
            'files': file_names
        }
        response = requests.post(
            url=self._scicat_file_server + 'zip', json=download_dict)
        decoded = response.content.decode('utf-8')
        file_name = re.search(r'var file =(.*?).zip', decoded)
        result = file_name.group(1)
        trimmed = result[2:]
        download_url = self._scicat_file_server + \
            'download/{}.zip'.format(trimmed)
        polling_url = self._scicat_file_server + \
            'zip/polling/{}.zip'.format(trimmed)
        time.sleep(self.timeout)
        content = requests.get(url=polling_url).content
        start_time = datetime.datetime.now()
        print(polling_url)
        while not content.startswith(b'/down'):
            time.sleep(self.timeout)
            content = requests.get(url=polling_url).content
            print(content)
            if datetime.datetime.now() - start_time > self.bigtimeout:
                raise TimeoutError
        response = requests.get(url=download_url)
        try:
            with zipfile.ZipFile(io.BytesIO(response.content)) as zipped_files:
                zipped_files.extractall(path=extract_location)
        except zipfile.BadZipFile as error:
            print('The retrieved file from SciCat is malformed. Try aagin')
            raise error
        if extract_location is None:
            extract_location = os.getcwd()

        return extract_location, file_names


def download(base1, files1):
    """download"""
    # Login
    scicat_inst = SciCat(username='brightness', password=sys.argv[1])
    # Download files
    file_location_on_disk, file_names = scicat_inst.download(base1, files1)
    # Print their location
    print(file_location_on_disk, file_names)


if __name__ == "__main__":
    """
    Example on how to use SciCat. 
    Note that the user `brightness` has no password. This password should be given as a 
    parameter when running to file.

    Example::

        python3 test_scicat_download.py `password`    

    """

    base = "/nfs/groups/beamlines/v20/YC7SZ5"
    files = ["nicos_00002498.hdf"]

    if len(sys.argv) < 2:
        print('A password was not supplied as an argument :-(')
        raise AttributeError

    # Login
    scicat_instance = SciCat(username='brightness', password=sys.argv[1])
    # Download files
    file_location_on_disk, file_names = scicat_instance.download(base, files)
    # Print their location
    print(file_location_on_disk, file_names)
