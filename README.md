# SciCat Custom Search Python Tool 🐍🔍  

[![Coverage Status](https://coveralls.io/repos/github/garethcmurphy/scicat_pkg/badge.svg?branch=master)](https://coveralls.io/github/garethcmurphy/scicat_pkg?branch=master)



This repository contains a **Python package** for performing custom searches in the **SciCat** science data catalog. The package is available on **PyPI** for easy installation and integration into workflows.

---

## Features ✨  

- **Custom Search Functionality**: Perform advanced queries on the SciCat API.  
- **Easy Integration**: Simple and intuitive Python interface for SciCat searches.  
- **PyPI Distribution**: Installable via `pip` for seamless usage.  

---

## Prerequisites 🛠️  

- Python 3.8+  
- SciCat API access and credentials.  

---

## Installation  

1. Install the package from PyPI:  
   pip install scicat-search-tool  

2. Alternatively, install from source:  
   git clone https://github.com/your-username/scicat-search-tool.git  
   cd scicat-search-tool  
   pip install .  

---

## Usage 🔧  

1. Import the package in your Python script:  
   from scicat_search import SciCatSearch  

2. Initialize the search tool:  
   scicat = SciCatSearch(api_url="https://scicat.example.com", token="your-api-token")  

3. Perform a custom search:  
   results = scicat.search(query={"key": "value"})  
   print(results)  

---

## File Structure 📂  

- `scicat_search/`: Package source code.  
- `setup.py`: Package configuration for PyPI.  
- `README.md`: Documentation for the repository.  

---

## Example Commands  

- Install the package:  
  pip install scicat-search-tool  

- Run a script using the package:  
  python example_script.py  

---

## Contributing 🤝  

1. Fork the repository.  
2. Create a new branch:  
   git checkout -b feature/your-feature  

3. Commit your changes:  
   git commit -m "Add your feature"  

4. Push the branch:  
   git push origin feature/your-feature  

5. Open a pull request.  

---

## License 📝  

This project is licensed under the MIT License. See the LICENSE file for details.  

---

**Streamline your SciCat searches with this Python package!** 🐍🔍  
