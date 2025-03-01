# the response module

import random

yes_in_a_bunch_of_languages = {
    'Afrikaans': 'Ja', 'Albanian': 'Po',
    'Amharic': 'አዎን (Awoon)', 'Arabic': '(Na\'am) نعم ',
    'Armenian': 'Այո (Ayo)', 'Aymara': 'Aru',
    'Azerbaijani': 'Bəli', 'Bengali': 'হ্যাঁ (Hyã)',
    'Basque': 'Bai', 'Belarusian': 'Так',
    'Bosnian': 'Da', 'Bulgarian': 'Да (Da)',
    'Cantonese': '係 (Hai)', 'French': 'Oui',
    'Catalan': 'Sí', 'Finnish': 'Kyllä',
    'Corsican': 'Sì', 'Czech': 'Ano',
    'Croatian': 'Da', 'Danish': 'Ja',
    'Dutch': 'Ja', 'English': 'Yes',
    'Estonian': 'Jah', 'Farsi (Persian)': 'بله (Bale)',
    'Ewe': 'Ɛ̃ (ee)', 'Fijian': 'Io',
    'Gaelic (Irish)': 'Tá', 'Georgian': 'კი (Ki)',
    'Galician': 'Sí', 'German': 'Ja',
    'Greek': 'Ναι (Ne)', 'Hebrew': 'כן (Ken)',
    'Guarani': 'Hẽ', 'Hindi': 'हाँ (Haan)',
    'Haitian Creole': 'Wi', 'Hmong': 'Yog',
    'Hungarian': 'Igen', 'Icelandic': 'Já',
    'Ilocano': 'Wen', 'Indonesian': 'Ya',
    'Italian': 'Ie', 'Japanese': 'はい (Hai)',
    'Kazakh': 'Ия (Iya)', 'Khmer': 'បាទ (Baht)',
    'Kinyarwanda': 'Yego', 'Korean': '네 (Ne)',
    'Kurdish': 'Bella', 'Lao': 'ໂດຍ (Doi)',
    'Latin': 'Ita', 'Latvian': 'Jā',
    'Lithuanian': 'Taip', 'Macedonian': 'Да (Da)',
    'Luxembourgish': 'Jo', 'Malagas': 'Eny',
    'Malay': 'Ya', 'Maltese': 'Iva',
    'Mandarin': '是 (Shì)', 'Maori': 'Āe',
    'Mongolian': 'Тийм (Tiim)', 'Myanmar (Burmese)': 'ဟုတ် (Hote)',
    'Nahuatl': 'Quin', 'Navajo': 'Hózhǫǫ́',
    'Nepali': 'Ja', 'Pashto': 'هو (Hu)',
    'Polish': 'Tak', 'Portuguese': 'Sim',
    'Punjabi': 'ਹਾਂ (Haan)', 'Romanian': 'Da',
    'Quechua': 'Arí', 'Russian': 'Да (Da)',
    'Samoan': 'Ioe', 'Serbian': 'Да (Da)',
    'Slovak': 'Áno', 'Somali': 'Haa',
    'Spanish': 'Sí', 'Swahili': 'Ndiyo',
    'Swedish': 'Ja	', 'Taiwanese': '有 (Ū)',
    'Tamil': 'ஆம் (Aam)', 'Thai': 'ใช่ (Chai)',
    'Tibetan': 'ཨོ (O)', 'Turkish': 'Evet',
    'Ukrainian': 'Так (Tak)	', 'Urdu': 'ہاں (Haan)	',
    'Uzbek': 'Ha', 'Vietnamese': 'Có',
    'Welsh': 'Ie', 'Xhosa': 'Ewe',
    'Esperanto': 'E'
}

language = random.choice(list(yes_in_a_bunch_of_languages))
print(f'{language}: {yes_in_a_bunch_of_languages[language]} ')
