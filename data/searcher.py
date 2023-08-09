from fuzzywuzzy import process, fuzz
from fuzzywuzzy.process import extractBests
# from base import Database
# from access import RAM
# import Levenshtein



class Google:
    def __init__(self, ram = None):
        self.ram = ram
        
        # s = ram.movies_title
        
        # matches = process.extract("sevadi", titles, limit = 1)
        
        
    def search_movies(self, match : str, limt : int = 10):
        scores, indexs = [], []
        for title in self.ram.movies_title:
            scores.append(fuzz.ratio(match, title))
        
        for n in range(limt):
            maxs = max(scores)
            indexs.append(scores.index(maxs))
            scores.remove(maxs)
        return indexs
        
        





















if __name__ == '__main__':
    db = Database("./data/database.db")
    ram = RAM(db)
    
    google = Google(ram = ram)
    indexs = google.search_movies(match = "sev", limt = 1)
    for index in indexs:
        print(ram.movies_title[index])
    
    
    
    
    
    # def search_movi(match : str, titles : str, limit : int = 10):
    #     matches = extractBests(match, titles, limit = limit)
    #     print(matches)
    #     return matches
    
    
    
    # titles = ['aple', 'banan', 'hello', 'this is bulshit', 'f* you', 'Google', 'face book', 'jon uik', 'google colab', 'yaxshi kino', 'yomon kino', 'kino topuvch bot', 'Forsaj 7', 'tor', 'qasoskorlar', 'qasoskorlar altron davri', 'manyakmisan ?', 'Jumong', 'Forsaj 7', 'Forsaj 8', 'Forsaj 9 : Xobs va shou', 'Forsaj 7', 'Forsaj 7']
    
    # matches = search_movi(match = 'forsaj', titles = titles, limit = 5)
    
    # while 'banan' in titles:
    #     index = titles.index('banan')
    #     titles.pop(index)
    