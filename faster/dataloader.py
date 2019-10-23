import pandas as pd
import io
import requests

class datatloader:
    def __init__(self):
        self.baseUrl = "https://www.football-data.co.uk/mmz4281/"
    
    def loadSeason(self, season, competition):
        dataurl = self.baseUrl + season + "/" + competition + ".csv"
        content=requests.get(dataurl).content
        return pd.read_csv(io.StringIO(content.decode('utf-8')))