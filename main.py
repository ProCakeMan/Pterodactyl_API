from http import client
import requests

class PyCli(object):
    """SIMPLE API FOR PTERODACTYL DEVELOPED BY RASMUS LØVLI NETLAND"""

    def __init__(self, url=None, clientAPI=None, applicationAPI=None):
        if not url:
            pass
        if not clientAPI:
            pass
        if not applicationAPI:
            pass

        self.url = url
        self.clientAPI = clientAPI
        self.applicationAPI = applicationAPI
        
        if clientAPI:
            self.headersClient = {
                "Authorization": "Bearer " + self.clientAPI,
                "Accept": "application/json"
            }
        if applicationAPI:
            self.headersApplication = {
                "Authorization": "Bearer " + self.applicationAPI,
                "Accept": "application/json"
            }


    def app_list_users(self, as_ID = False, as_username = False):
        try:
            url = self.url + "/api/application/users"
            response = requests.request('GET', url, headers=self.headersApplication)
            data = response.json()
            if as_ID and as_username:
                data = data['data']
                users = []
                for user in data:
                    users.append({user['attributes']['id']: user['attributes']['username']})
                data = users
            else:
                if as_ID:
                    data = data['data']
                    users = []
                    for user in data:
                        users.append(user['attributes']['id'])
                    data = users
                if as_username:
                    data = data['data']
                    users = []
                    for user in data:
                        users.append(user['attributes']['username'])
                    data = users
        except:
            return "Something is configured wrongly, check url and API keys."
        return data

    def app_list_servers(self):
        try:
            url = self.url + "/api/application/servers"
            response = requests.request('GET', url, headers=self.headersApplication)
            data = response.json()
        except:
            return "Something is configured wrongly, check url and API keys."
        return data

    def get_servers_by_user(self, userID):
        try:
            servers = self.app_list_servers()
            servers = servers['data']
            owned_servers = []
            for server in servers:
                if server['attributes']['user'] == userID:
                    owned_servers.append(server['attributes']['name'])
                else:
                    pass
            if not owned_servers:
                owned_servers.append("No servers registered")
            return owned_servers
        except:
            return "Something is configured wrongly, check url and API keys."




def match_server_with_userID(self, userID):
    try:
        url = self.url + "/api/application/users"
        response = requests.request('GET', url, headers=self.headersApplication)
        serverList = response.json()
        serverList = serverList['data']
        servers = []
        for server in serverList:
            if server['attributes']['user'] == userID:
                #print("Match: " + str(userID) + " " + str(server['attributes']['user']))
                servers.append({server['attributes']['name']: server['attributes']['id']})
            else:
                pass
        return servers
    except:
        return "Something is configured wrongly, check url and API keys."