How to run

Step 1: Make sure python > 3.8 is installed and added to PATH

Step 2: Open CMD, type: python manage.py runserver

Step 3: Install the missing/required python packages

-Type the below commands in CMD to bypass proxy and download the required python packages

set http_proxy=http://proxy01.intra.hkma.gov.hk:8080
set https_proxy=http://proxy01.intra.hkma.gov.hk:8080
pip --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org install django

Step 4: Follow step 2 run again

Step 5: Go to http://127.0.0.1:8000/ to view the application
