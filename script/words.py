"""
    Parse words.txt
"""
import re


def pre_process():
    f = open("../static/words.txt", "r")
    new_lines = []
    keyword = ""
    for line in f:
        if len(line) >= 2:
            line = line.strip()
            parsed = line.split(".")
            if len(parsed) <= 1:
                keyword = line
            else:
                word = parsed[1]
                word = re.sub(r"\[[^\w]*\]", '', word)
                new_lines.append("{}, {}\n".format(word, keyword))
    f.close()
    f = open("../static/words_pro.txt", "w")
    f.writelines(new_lines)
    f.close()


def process():
    f = open("../static/words_pro.txt", "r")
    new_line = []
    english = re.compile("^[#*,a-z\-\s]+")
    for line in f:
        word = re.sub(r"\s+", " ", line.strip(), re.L | re.U)
        word = re.sub(r"\s*,\s*", ",", word, re.L | re.U)
        eng = english.findall(word)
        assert len(eng) == 1
        chn = word[len(eng[0]):].strip()
        chn_list = chn.split(',')
        chn = '@'.join([','.join(chn_list[:-1]), chn_list[-1]])
        new_line.append("{}@{}\n".format(eng[0].strip(), chn))
    f.close()
    f = open("../static/words_final.txt", "w")
    f.writelines(new_line)
    f.close()


process()
