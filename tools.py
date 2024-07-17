from dotenv import load_dotenv
load_dotenv()
import os
import json
from langchain.tools import BaseTool
from langchain.utilities import GoogleSerperAPIWrapper

class InternetSearchTool(BaseTool):
    name = "Search the internet"
    description = "A tool that can be used to search the internet with a search_query."

    def _run(self, query: str, config=None):
        search = GoogleSerperAPIWrapper(serper_api_key=os.getenv('SERPER_API_KEY'))
        results = search.results(query)
        return json.dumps(results, ensure_ascii=False, indent=2)

    def _arun(self, query: str):
        raise NotImplementedError("This tool does not support async")

# Initialize the tool
tool = InternetSearchTool()