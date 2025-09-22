from asterisk.ami import AMIClient

client = AMIClient(address='localhost', port=5038)
client.login(username='astuserA', secret='astpassA')

response = client.send_action({'Action': 'Ping'})
print(response.response)

client.logoff()
