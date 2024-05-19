import requests

php_script_url = "http://localhost/attendance/saveattendance.php"

# Set any parameters you need to pass to the PHP script

def savestudent(name):
    params = {
        'name': name 
        
    }

    response = requests.post(php_script_url, data=params)

    # Check the response
    if response.status_code == 200:
        print("PHP script executed successfully")
        print("Response:", response.text)
    else:
        print("Error:", response.status_code, response.text)