import requests
from configs.api_config import ApiConfig


class GraphQLRequests:
    @staticmethod
    def send_graphql_request(query, variables=None):
        url = ApiConfig.BASE_URL
        headers = {"Content-Type": "application/json"}
        data = {"query": query, "variables": variables}
        response = requests.post(url, headers=headers, json=data)
        return response
