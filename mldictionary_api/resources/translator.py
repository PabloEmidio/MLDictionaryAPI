from mldictionary import Dictionary


class Translator(Dictionary):
    url = 'https://www.linguee.com/english-portuguese/search?source=auto&query={}'
    language = 'Translator(en-pt)'
    target_tag = 'a'
    target_attr = {'class': 'featured'}

