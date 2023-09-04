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

        # print("Settings updated           ", end = '\r')




if __name__ == '__main__':
    set = Setting()
    # set.data['pasword'] = '0000'
    # set.update()

    # set.data['forced_chanels'] = {}https://t.me/sexiiwbeyw
    # set.data['forced_chanels']['@kino_bot_discuss'] = 'https://t.me/Kino_bot_news'
    # set.data['forced_chanels']['@sexiiwbeyw'] = 'https://t.me/sexiiwbeyw'
    # set.data['bot_url'] = '@kino_qidiruvchi_robot'
    # set.data['user_manual'] = 'Blah blah'
    set.data['vide_manual'] = 333
    print(set.data)

    set.update()