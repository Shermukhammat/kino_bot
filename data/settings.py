import json
class Setting:
    def __init__(self, file : str = 'data/settings.json'):
        self.file = file

        js = open(file, 'r')
        self.data = json.loads(js.read())
        js.close()

        # data = {'forced_chanels' : [], 'pasword' : '1234'}
        # js.write(json.dumps(data))

    def update(self):
        js = open(self.file, 'w')
        js.write(json.dumps(self.data))

        print("Settings updated           ", end = '\r')




if __name__ == '__main__':
    set = Setting()
    # set.data['pasword'] = '0000'
    # set.update()

    # set.data['forced_chanels'].append('@kino_bot_discuss')
    print(set.data)

    # set.update()