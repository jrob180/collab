from .models import Token
def refresh_access_token():

    token = Token.objects.get(id = 1)
    refresh_token = token.refresh_token
    client_id = 'zJib8nQsTG0QA_JgEqj5Q'
    client_secret = 'V7GDiRa1c1d9gMRfW4GzZMvp3MJY7vkE'

    message = client_id + ':' + client_secret
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    auth = 'Basic ' + base64_bytes.decode('ascii')

    endpoint = 'https://zoom.us/oauth/token?grant_type=refresh_token&refresh_token=' + refresh_token
    headers = {'Authorization': auth, 'host': 'zoom.us'}
    x = requests.post(endpoint, headers = headers)
    j = json.loads(x.text)
    token.refresh_token= j['refresh_token']
    token.access_token = j['access_token']
    token.save()
    #print('\n')
    #print('TOKEN HAS BEEN REFRESHED' + str(time.time()))
    #print('\n')
    return