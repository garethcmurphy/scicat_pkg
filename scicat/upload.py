#!/usr/bin/env python3
"""upload to scicat"""

def upload(name):
    """upload to scicat"""
    print("uploading to scicat")
    dataset = {
     "datasetName":name   
    }
    print(dataset)

def main():
    """main"""
    name = "nexus"
    upload(name)

if __name__ == "__main__":
    main()