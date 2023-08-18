import re
import emoji

def title_finder(movi_info : str):
    words = [info.lower() for info in movi_info.split(" ")]
    if re.search(r'[0-9]*.-*.qism|premyera', words[0]) == None:
        words = movi_info.split('\n')
        title = words[0]

        title = emoji.replace_emoji(title)
        return re.sub(r"kino*.nomi|nomi|:", "", title.lower()).strip().capitalize()
    for word in words[1:]:
        if len(word.replace(" ", '')) > 3:
            return word.strip().title()
    return False
        
  
def info_cleaner(info : str, bot : str = "@blah_bot"):
    return re.sub(r'.*\B@(?=\w{5,32}\b)[a-zA-Z0-9]+(?:_[a-zA-Z0-9]+)*.*', '', info).strip() + "\n\n" + bot
