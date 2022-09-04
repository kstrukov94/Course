import requests

response = requests.get('https://api.github.com')
# print(response.status_code)
# print(response.content)
# print(response.text)
#
#
# from requests.exceptions import HTTPError
#
# for url in ['https://api.github.com', 'https://api.github.com/invalid']:
#     try:
#         response = requests.get(url)
#
#         # If the response was successful, no Exception will be raised
#         response.raise_for_status()
#     except HTTPError as http_err:
#         print(f'HTTP error occurred: {http_err}')  # Python 3.6
#     except Exception as err:
#         print(f'Other error occurred: {err}')  # Python 3.6
#     else:
#         print('Success!')

response_dict = response.json()
for key in response_dict:
    print(f"{key} : {response_dict[key]}")

response_headers_dict = response.headers
for key in response_headers_dict:
    print(f"{key} : {response_headers_dict[key]}")
