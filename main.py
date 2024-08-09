import requests
from enum import Enum

class BaseURL(Enum):
    GITHUB_BASE_URL='https://api.github.com'


class Repository:
    def __init__(self, org_name, repo_url, personal_access_token=None):
        self.org_name = org_name
        self.repo_url = repo_url
        self.personal_access_token = personal_access_token

    def print_args(self):
        print(self.org_name, self.repo_url, self.personal_access_token)

    def _get_request(self):
        return requests.get(self.repo_url)

    def verify_request(self):
        return self._get_request().status_code==200
        
    def return_repository_list(self):
        if self.verify_request():
            return self._get_request().json()
        else:
            return {}
        

def return_last_updated(repo_list):
    return_list = []
    for repo in repo_list:
        return_list.append((repo['name'], repo['updated_at']))
    return return_list


if __name__=='__main__':    
    org_name = 'Netflix' 
    org_url = f"{BaseURL.GITHUB_BASE_URL.value}/orgs/{org_name}/repos"
    repository = Repository(org_name, org_url)
    repository.print_args()
    repo_list = repository.return_repository_list()    
    repo_last_updated = return_last_updated(repo_list)
    print(repo_last_updated[:5])


