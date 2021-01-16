import os
import django
import sys
sys.path.append('..')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "alphabet.settings")
django.setup()


from reciting.models import Word, Dictionary

Dictionary.objects.create(name="系统解剖学词汇")
dic_obj = Dictionary.objects.get(name="系统解剖学词汇")

f = open("../static/words_final.txt", "r")
for line in f:
    attr = line.strip().split("@")
    if len(attr) != 3:
        continue
    Word.objects.create(text=attr[0], description=attr[1], category=attr[2], dic=dic_obj)

