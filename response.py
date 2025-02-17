# the response module

import random

yes_in_a_bunch_of_languages = [
    'yes', 'sí', 'oui', 'ja', 'sì',
    'sim', 'kyllä', 'já', 'ναι', 'да',
    '是', 'はい', '네', 'ndiyo', 'نعم',
    'כן', 'evet', 'igen', 'tak', 'ano',
    'áno', 'da', 'po', 'jah', 'jā',
    'taip', 'დიახ ', 'այո ', 'بله ', 'हाँ ',
    'হ্যাঁ ', 'ใช่ ', 'đúng', 'ya', 'iya',
    'nu', 'oo', 'nu', 'យល់ពូល', 'ແມ່ນ ',
    'ဟုတ်ကဲ့ ', 'አዎ ', 'eh', 'bẹẹ̀ni', 'ndiyo',
    'አዎን ', 'Այո ', 'კი ', 'Ия ', 'បាទ ',
    'ໂດຍ ', 'Тийм ', 'Hózhǫǫ́', 'हो ', 'ਹਾਂ ',
    '有 ', 'ใช่ ', 'ہاں '
]

line_count = len(yes_in_a_bunch_of_languages)

yes_index = random.randrange(0, line_count - 1)

print(yes_in_a_bunch_of_languages[yes_index])
