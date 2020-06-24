#1. Pyperclip
import pyperclip
pyperclip.copy('Heyyy this is being copied to clipboard')
print(pyperclip.paste())

#2. Emoji
from emoji import emojize
print(emojize(':thumbs_up:'),emojize(':snake:'))

#3. Howdoi
from howdoi import howdoi
query = "open a file in python"
parser = howdoi.get_parser()
args = vars(parser.parse_args(query.split(' ')))
output = howdoi.howdoi(args)
print(output)

#4. Antigravity
import antigravity

#5. Wikipedia
import wikipedia
page = wikipedia.page("Python")
print(page.summary)

#6. Dissemble Python
import dis
def myfun(num):
    return('Number to string : ',str(num))

dis.dis(myfun)


