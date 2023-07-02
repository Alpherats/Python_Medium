# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

import re
from collections import Counter

def count_words(text: str) -> list:

    text = re.sub(r'[^\w\s]', '', text.lower())
    words = text.split()
    word_counts = Counter(words)

    most_common_words = word_counts.most_common(10)

    return most_common_words

text = """
Barack Hussein Obama II ( English pronunciation:  [bəˈrɑːk huːˈseɪn oʊˈbɑːmə]  ( listen ) ), born August 4 , 1961 in Honolulu , Hawaii , is an American lawyer and Democratic politician who was the 44th President of the United States in the years 2009–2017. He took office on 20 January 2009 after winning the presidential election on 4 November 2008 . In the presidential electionon November 6, 2012, he was re-elected for another four years in office; he then came to serve two terms, which is the maximum for a president in the United States. He is the first African American to be elected president and also the first African American to be nominated for office by a major political party.

Obama is a trained lawyer and received his JD in 1991 from Harvard Law School . During his studies, he was also chairman of the Harvard Law Review . He also holds a bachelor's degree (BA) in political science from Columbia University in 1983. Before the presidency, he worked as a lecturer in government law at the University of Chicago Law School from 1992-2004. He also practiced as a civil rights attorney and served three terms in the Illinois State Senate from 1997-2004. In November 2004, he was elected to the United States Senateand was a federal senator for Illinois in 2005–2008. Based on how Obama has voted in the Senate, he is politically far to the left. [ 2 ]

During his time as President of the United States (2009–2017), his greatest achievements were the introduction of universal health insurance (Obamacare), the enforcement of a stimulus package for investment in education, infrastructure, health care and green energy, a reform of the regulatory framework for Wall Street , the signing of the 2015 Paris Agreement , the introduction of a new immigration law that granted work permits to some illegal immigrants , and the legalization of same-sex marriage . [ 3 ]

Obama was awarded the Nobel Peace Prize in October 2009 for his efforts to strengthen international diplomacy and cooperation. This after being president for just under nine months. [ 4 ] That Obama was awarded the prize has subsequently met with criticism. Geir Lundestad , director at the Norwegian Nobel Institute , has emphasized that the prize did not have the desired effect on Obama's foreign policy. [ 5 ] Obama's foreign policy has been criticized for having been weak and giving space to Russia , China and North Korea , among others, to expand their global power and increasing political instability inThe Middle East .
"""

result = count_words(text)

for word, count in result:
    print(word, count)
