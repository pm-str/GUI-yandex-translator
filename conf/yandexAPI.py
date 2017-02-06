# default language
lang_from = 'английский'
lang_two = 'русский'

langs = {
    'марийский': 'mhr', 'сербский': 'sr', 'финский': 'fi', 'македонский': 'mk', 'гаитянский': '(креольский)',
    'сингальский': 'si', 'маори': 'mi', 'казахский': 'kk', 'турецкий': 'tr', 'азербайджанский': 'az',
    'португальский': 'pt', 'галисийский': 'gl', 'немецкий': 'de', 'хорватский': 'hr', 'русский': 'ru',
    'шотландский': 'gd', 'гуджарати': 'gu', 'украинский': 'uk', 'идиш': 'yi', 'болгарский': 'bg',
    'папьяменто': 'pap', 'мальтийский': 'mt', 'малагасийский': 'mg', 'индонезийский': 'id', 'себуанский': 'ht',
    'тамильский': 'ta', 'польский': 'pl', 'грузинский': 'ka', 'удмуртский': 'udm', 'хинди': 'hi', 'японский': 'ja',
    'боснийский': 'bs', 'тайский': 'th', 'таджикский': 'tg', 'непальский': 'ne', 'каннада': 'kn',
    'малайский': 'ms', 'урду': 'ur', 'испанский': 'es', 'сунданский': 'su', 'греческий': 'el', 'панджаби': 'pa',
    'узбекский': 'uz', 'персидский': 'fa', 'английский': 'en', 'телугу': 'te', 'словенский': 'sl',
    'малаялам': 'ml', 'армянский': 'hy', 'башкирский': 'ba', 'ирландский': 'ga', 'румынский': 'ro',
    'исландский': 'is', 'французский': 'fr', 'латышский': 'lv', 'албанский': 'sq', 'норвежский': 'no',
    'арабский': 'ar', 'бенгальский': 'bn', 'словацкий': 'sk', 'эсперанто': 'eo', 'валлийский': 'cy',
    'венгерский': 'hu', 'чешский': 'cs', 'шведский': 'sv', 'горномарийский': 'mrj', 'итальянский': 'it',
    'вьетнамский': 'vi', 'коса': 'xh', 'баскский': 'eu', 'каталанский': 'ca', 'яванский': 'jv', 'африкаанс': 'af',
    'китайский': 'zh', 'тагальский': 'tl', 'литовский': 'lt', 'латынь': 'la', 'датский': 'da', 'белорусский': 'be',
    'татарский': 'tt', 'люксембургский': 'lb', 'суахили': 'sw', 'корейский': 'ko', 'эстонский': 'et',
    'монгольский': 'mn', 'маратхи': 'mr', 'иврит': 'he', 'амхарский': 'am', 'голландский': 'nl',
    'киргизский': 'ky'
}
DICT_KEY = ''
TR_KEY = ''

DictLookup = 'https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key={}&lang={lang}&text={text}' \
    .format(DICT_KEY, lang='{lang}', text='{text}')

DoTr = 'https://translate.yandex.net/api/v1.5/tr.json/translate?key={}&text={text}&lang={lang}&options=1' \
    .format(TR_KEY, lang='{lang}', text='{text}')

update_time = 0.5
