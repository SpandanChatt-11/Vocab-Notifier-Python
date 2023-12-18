from plyer import notification
import time
import json
import requests
import win32com.client as wincl
from random_word import RandomWords

while True:
    random_words = RandomWords()
    word=random_words.get_random_word()
    spk = wincl.Dispatch("SAPI.SpVoice")
    rest=1800

    while True:
        url=f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        res=requests.get(url)
        dict=json.loads(res.text)

        try:
            for i in dict[0]['meanings']:
                for j in i['definitions']:
                    try:
                        notification.notify(title = word.upper(),
                           message = f"MEANING : {j['definition']}\nEXAMPLE : {j['example']}",
                           app_icon = None,
                           timeout = 30,
                            )
                        spk.speak(word)
                        spk.speak(f"MEANING : {j['definition']}  EXAMPLE : {j['example']}")
                        time.sleep(rest)
                        break
                    except:
                        notification.notify(title = word.upper(),
                           message = f"MEANING : {j['definition']}",
                           app_icon = None,
                           timeout = 30,
                            )
                        spk.speak(word)
                        spk.speak(f"MEANING : {j['definition']}")
                        time.sleep(rest)
                        break
                break
            break
        except:
            break