import pytest

from main import top_10_most_common_words


TEXT_1 = """
Ты жива еще, моя старушка?
Жив и я. Привет тебе, привет!
Пусть струится над твоей избушкой
Тот вечерний несказанный свет.

Пишут мне, что ты, тая тревогу,
Загрустила шибко обо мне,
Что ты часто ходишь на дорогу
В старомодном ветхом шушуне.

И тебе в вечернем синем мраке
Часто видится одно и то ж:
Будто кто-то мне в кабацкой драке
Саданул под сердце финский нож.

Ничего, родная! Успокойся.
Это только тягостная бредь.
Не такой уж горький я пропойца,
Чтоб, тебя не видя, умереть.

Я по-прежнему такой же нежный
И мечтаю только лишь о том,
Чтоб скорее от тоски мятежной
Воротиться в низенький наш дом.

Я вернусь, когда раскинет ветви
По-весеннему наш белый сад.
Только ты меня уж на рассвете
Не буди, как восемь лет назад.

Не буди того, что отмечталось,
Не волнуй того, что не сбылось, —
Слишком раннюю утрату и усталость
Испытать мне в жизни привелось.

И молиться не учи меня. Не надо!
К старому возврата больше нет.
Ты одна мне помощь и отрада,
Ты одна мне несказанный свет.

Так забудь же про свою тревогу,
Не грусти так шибко обо мне.
Не ходи так часто на дорогу
В старомодном ветхом шушуне.
"""

MOST_COMMON_1 = {'мне': 7, 'что': 4, 'так': 3, 'только': 3, 'часто': 3, 'буди': 2, 'ветхом': 2, 'дорогу': 2, 'меня': 2, 'наш': 2}


TEXT_2 = """
Не жалею, не зову, не плачу,
Все пройдет, как с белых яблонь дым.
Увяданья золотом охваченный,
Я не буду больше молодым.

Ты теперь не так уж будешь биться,
Сердце, тронутое холодком,
И страна березового ситца
Не заманит шляться босиком.

Дух бродяжий! ты все реже, реже
Расшевеливаешь пламень уст
О моя утраченная свежесть,
Буйство глаз и половодье чувств.

Я теперь скупее стал в желаньях,
Жизнь моя? иль ты приснилась мне?
Словно я весенней гулкой ранью
Проскакал на розовом коне.

Все мы, все мы в этом мире тленны,
Тихо льется с кленов листьев медь…
Будь же ты вовек благословенно,
Что пришло процвесть и умереть.
"""

MOST_COMMON_2 = {'все': 4, 'моя': 2, 'реже': 2, 'теперь': 2, 'белых': 1, 'березового': 1, 'биться': 1, 'благословенно': 1, 'больше': 1, 'босиком': 1}


TEXT_3 = """
Три девицы под окном
Пряли поздно вечерком.
"Кабы я была царица, -
Говорит одна девица, -
То на весь крещёный мир
Приготовила б я пир".
"Кабы я была царица, -
Говорит ее сестрица, -
То на весь бы мир одна
Наткала я полотна".
"Кабы я была царица, -
Третья молвила сестрица, -
Я б для батюшки-царя
Родила богатыря".

Только вымолвить успела,
Дверь тихонько заскрыпела,
И в светлицу входит царь,
Стороны той государь.
Во всё время разговора
Он стоял позадь забора;
Речь последней по всему
Полюбилася ему.
"Здравствуй, красная девица, -
Говорит он, - будь царица
И роди богатыря
Мне к исходу сентября.
Вы ж, голубушки-сестрицы,
Выбирайтесь из светлицы,
Поезжайте вслед за мной,
Вслед за мной и за сестрой:
Будь одна из вас ткачиха,
А другая повариха".
"""


MOST_COMMON_3 = {'царица': 4, 'была': 3, 'говорит': 3, 'кабы': 3, 'одна': 3, 'богатыря': 2, 'будь': 2, 'весь': 2, 'вслед': 2, 'девица': 2}


@pytest.mark.parametrize(
    'text, result',
    [
        (TEXT_1, MOST_COMMON_1),
        (TEXT_2, MOST_COMMON_2),
        (TEXT_3, MOST_COMMON_3),
    ]
)
def test_most_common_words(text, result):
    assert top_10_most_common_words(text) == result
