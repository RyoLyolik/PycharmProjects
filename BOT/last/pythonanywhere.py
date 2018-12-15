import requests

my_domain = 'pythonanywhere.com/user/RyoLyo/files/home/RyoLyo'
username = 'RyoLyo'
token = '38a76e35c0705c8b2f0997113c8ac6c090c3aa01'

response = requests.post(
    'https://www.pythonanywhere.com/api/v0/user/{username}/webapps/{domain}/reload/'.format(
        username=username, domain=my_domain
    ),
    headers={'Authorization': 'Token {token}'.format(token=token)}
)
print(response)
if response.status_code == 200:
    print('All OK')
else:
    print('Got unexpected status code\n{}: {!r}'.format(response.status_code, response.content))