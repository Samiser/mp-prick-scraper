import requests
import os.path
import csv

class Mp:
    def __init__(self, name, party):
        self.name = name
        self.party = party
        self.prick = 'unknown'
        self.prick = self.determine_prick(name)

    def __repr__(self):
        return self.name

    def determine_prick(self, mp):
        if self.prick != 'unknown':
            return self.prick

        url = 'http://ismympaprick.co.uk/find'
        body = {'searchterm':mp}

        x = requests.post(url, data = body)

        if 'is not a prick' in x.text:
            print(f'{self.name}, {self.party} MP, is not a prick :)')
            self.prick = False
        else:
            print(f'{self.name}, {self.party} MP, is a prick :(')
            self.prick = True

        return self.prick

def parse(mps_file):
    mps = []
    reader = csv.reader(mps_file)
    next(reader)

    for mp in reader:
        mps.append(Mp(mp[1] + ' ' + mp[2], mp[3]))

    return mps

def write_csv(mps):
    with open('pricks.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Party", "Prick"])
        for mp in mps:
            writer.writerow([mp.name, mp.party, mp.prick])

def visualise(pricks_file):
    prick_count = {}
    reader = csv.reader(pricks_file)
    next(reader)

    for mp in reader:
        if mp[1] not in prick_count:
            prick_count[mp[1]] = {'pricks': 0, 'members': 0}

        prick_count[mp[1]]['members'] += 1

        if mp[2] == 'True':
            prick_count[mp[1]]['pricks'] += 1

    for party in prick_count:
        print(
            f"{party} has {prick_count[party]['pricks']}",
            f"pricks out of {prick_count[party]['members']}",
            "elected representatives")

if __name__ == '__main__':
    mps = []

    if os.path.isfile('pricks.csv'):
        with open('pricks.csv', 'r') as pricks_file:
            visualise(pricks_file)

    elif os.path.isfile('mps.csv'):
        with open('mps.csv', 'r') as mps_file:
            mps = parse(mps_file)
            write_csv(mps)
        with open('pricks.csv', 'r') as pricks_file:
            visualise(pricks_file)

    else:
        print('mps csv not found, get it at https://www.theyworkforyou.com/mps/?f=csv')

