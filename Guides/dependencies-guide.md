INSTALLING LISA DEPENDENCIES IN A VENV
In order to install dependencies in a virtual environment, you first need to install all
dependencies listed in the ‘requirements.txt’ file.
Once you’re in the virtual environment, you can do that with:
- pip3 install -r requirements.txt
Then you need to install the pycoral library, running the following commands:
- python3 -m pip install --extra-index-url
https://google-coral.github.io/py-repo/ pycoral~=2.0
- sudo apt-get install libopenblas-dev
