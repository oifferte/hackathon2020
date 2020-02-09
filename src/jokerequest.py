import requests

class JokesAPI():

    def __init__(self):
        self.r = requests.get('https://geek-jokes.sameerkumar.website/api')
        self.jokes = self.r.json()
        #self.length = len(self.jokes['objects'])
        self.pun = ""
        self.list = []
        self.norris = 0


    def tellajoke(self):
        self.r = requests.get('https://geek-jokes.sameerkumar.website/api')
        while "Chuck Norris" in self.r.text or "quot" in self.r.text or "&" in self.r.text:
            self.r = requests.get('https://geek-jokes.sameerkumar.website/api')
            print("loading")
        return self.r.text
