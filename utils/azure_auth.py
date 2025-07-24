from azure.identity import DefaultAzureCredential
from msgraph.core import GraphClient

credential = DefaultAzureCredential()

def get_graph_client():
    return GraphClient(credential=credential)