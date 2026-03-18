import re

# Dictionary of name to image file
images = {
    "Angel's Blush (Энжел Блаш)": "Angel's Blush (Энжел Блаш).jpg",
    "Baby Lace (Бейби Лейс)": "Baby Lace (Бейби Лейс).jpg",
    "Be Green (Би Грин)": "Be Green (Би Грин).webp",
    "Be Happy (Би Хеппи)": "Be Happy (Би Хеппи).jpg",
    "Be Sweet (Би Свит)": "Be Sweet (Би Свит).webp",
    "BJ (Би Джей)": "BJ (Би Джей).jpg",
    "Bloomulus Nimbus (Блумулус Нимбус)": "Bloomulus Nimbus (Блумулус Нимбус).jpg",
    "Bobo (Бобо)": "Bobo (Бобо).jpg",
    "Bonfire (Бонфаер)": "Bonfire (Бонфаер).jpg",
    "Colorful Cocktail (Колорфул Коктейль)": "Colorful Cocktail (Колорфул Коктейль).jpg",
    "Cotton Cream (Коттон Крим)": "Cotton Cream (Коттон Крим).jpg",
    "Diamant Rouge (Даймонд Руж)": "Diamant Rouge (Даймонд Руж).jpg",
    "Dolly (Долли)": "Dolly (Долли).png",
    "Firelight (Фаерлайт)": "Firelight (Фаерлайт).jpg",
    "Firelight Tiny Bitt (Фаерлайт Тини Бит)": "Firelight Tiny Bitt (Фаерлайт Тини Бит).jpg",
    "Fraise Melba (Фрайс Мельба)": "Fraise Melba (Фрайс Мельба).jpg",
    "Gardenlight Brightlight (Гарденлайт Брайтлайт)": "Gardenlight Brightlight (Гарденлайт Брайтлайт).jpg",
    "Gardenlight Greenlight (Гарденлайт Гринлайт)": "Gardenlight Greenlight (Гарденлайт Гринлайт).jpg",
    "Gardenlight Lemonlight (Гарденлайт Лемонлайт)": "Gardenlight Lemonlight (Гарденлайт Лемонлайт).jpg",
    "Gardenlight Pinklight (Гарденлайт Пинклайт)": "Gardenlight Pinklight (Гарденлайт Пинклайт).webp",
    "Gardenlight Redlight (Гарденлайт Редлайт)": "Gardenlight Redlight (Гарденлайт Редлайт).jpg",
    "Gardenlight Whitelight (Гарденлайт Вайтлайт)": "Gardenlight Whitelight (Гарденлайт Вайтлайт).jpg",
    "Gardenlight XS Light (Гарденлайт ХS-Лайт)": "Gardenlight XS Light (Гарденлайт ХS-Лайт).webp",
    "Graffiti (Граффити)": "Graffiti (Граффити).jpg",
    "Great Star (Грейт Стар)": "Great Star (Грейт Стар).jpg",
    "Hercules (Геркулес)": "Hercules (Геркулес).jpg",
    "Infinity (Инфинити)": "Infinity (Инфинити).webp",
    "Limelite (Лаймлайт)": "Limelite (Лаймлайт).webp",
    "Little Alf (Литл Альф)": "Little Alf (Литл Альф).webp",
    "Little Apple (Литл Эпл)": "Little Apple (Литл Эпл).jpg",
    "Little Blossom (Литл Блоссом)": "Little Blossom (Литл Блоссом).jpg",
    "Little Fresco (Литл Фреско)": "Little Fresco (Литл Фреско).jpg",
    "Little Hottie (Литл Хотти)": "Little Hottie (Литл Хотти).jpg",
    "Little Lime Punch (Литл Лайм Панч)": "Little Lime Punch (Литл Лайм Панч).jpg",
    "Little Passion (Литл Пэшн)": "Little Passion (Литл Пэшн).jpg",
    "Little Rosy (Литл Рози)": "Little Rosy (Литл Рози).jpg",
    "Little Spooky (Литл Спуки)": "Little Spooky (Литл Спуки).jpg",
    "Magical Andes (Мэджикал Андэс)": "Magical Andes (Мэджикал Андэс).jpg",
    "Magical Candle (Мэджикал Кэндл)": "Magical Candle (Мэджикал Кэндл).png",
    "Magical Fire (Мэджикал фаер)": "Magical Fire (Мэджикал фаер).jpg",
    "Magical Kilimanjaro (Мэджикал Килиманджаро)": "Magical Kilimanjaro (Мэджикал Килиманджаро).jpg",
    "Magical Mont Blanc (Мэджикал Монблан)": "Magical Mont Blanc (Мэджикал Монблан).jpg",
    "Magical Sweet Summer (Мэджикал Свит Саммэр)": "Magical Sweet Summer (Мэджикал Свит Саммэр).jpg",
    "Magical Vesuvio (Мэджикал Везувио)": "Magical Vesuvio (Мэджикал Везувио).jpg",
    "Mega Mindy (Мега Минди)": "Mega Mindy (Мега Минди).jpg",
    "Metallica (Металлика)": "Metallica (Металлика).jpg",
    "Milk and Honey (Милк энд Хани)": "Milk and Honey (Милк энд Хани).jpg",
    "Minty Spirit (Минти Спирит)": "Minty Spirit (Минти Спирит).jpg",
    "Mojito (Мохито)": "Mojito (Мохито).jpg",
    "Pastel green (Пастель грин)": "Pastel green (Пастель грин).jpg",
    "Petitе Cherry (Петит Черри)": "Petitе Cherry (Петит Черри).jpg",
    "Petitе Flori (Петит Флори)": "Petitе Flori (Петит Флори).webp",
    "Petitе Lantern (Петит Лантерн)": "Petitе Lantern (Петит Лантерн).webp",
    "Petitе Star (Петит Стар)": "Petitе Star (Петит Стар).png",
    "Phantom (Фантом)": "Phantom (Фантом).jpg",
    "Pink and Rose (Пинк энд Роуз)": "Pink and Rose (Пинк энд Роуз).jpg",
    "Pink Shade (Пинк Шейд)": "Pink Shade (Пинк Шейд).jpg",
    "Pinkachu (Пинкачу)": "Pinkachu (Пинкачу).webp",
    "Pinky Promise (Пинки Промис)": "Pinky Promise (Пинки Промис).png",
    "Pixio (Пиксио)": "Pixio (Пиксио).jpg",
    "Polestar (Полестар)": "Polestar (Полестар).webp",
    "Quick Fire Fаb (Квик Фаер Фаб)": "Quick Fire Fаb (Квик Фаер Фаб).jpg",
    "Red Velvet (Рэд Вельвет)": "Red Velvet (Рэд Вельвет).webp",
    "Royal Flower (Роял Флауэр)": "Royal Flower (Роял Флауэр).jpg",
    "Silver Dollar (Сильвер Доллар)": "Silver Dollar (Сильвер Доллар).jpg",
    "Skyfall (Скайфол)": "Skyfall (Скайфол).jpg",
    "Star Rose (Стар Роуз)": "Star Rose (Стар Роуз).jpg",
    "Strawberry Blossom (Стробери Блоссом)": "Strawberry Blossom (Стробери Блоссом).jpg",
    "Sugar Rush (Шугар Раш)": "Sugar Rush (Шугар Раш).jpg",
    "Summer Breeze (Саммер Бриз)": "Summer Breeze (Саммер Бриз).jpg",
    "Summer Love (Саммер Лав)": "Summer Love (Саммер Лав).jpg",
    "Summer Snow (Саммер Сноу)": "Summer Snow (Саммер Сноу).webp",
    "Sundae Fraise (Сандей Фрайс)": "Sundae Fraise (Сандей Фрайс).jpg",
    "Tardiva (Тардива)": "Tardiva (Тардива).jpg",
    "Tickled Pink (Тиклед Пинк)": "Tickled Pink (Тиклед Пинк).jpg",
    "Touch of Pink (Тач оф Пинк)": "Touch of Pink (Тач оф Пинк).jpg",
    "Unique (Юник)": "Unique (Юник).webp",
    "Vanilla Fraise (Ванилла Фрейз)": "Vanilla Fraise (Ванилла Фрейз).jpg",
    "Граундбрейкер (Groundbreaker)": "Граундбрейкер (Groundbreaker).jpg",
    "Жемчужина фестиваля (Pearl of Festivale)": "Жемчужина фестиваля (Pearl of Festivale).jpg",
    "Краса Лесково": "Краса Лесково.jpg",
    "Панателла (Panatella)": "Панателла (Panatella).jpg",
    "Пандалус (Pandalus)": "Пандалус (Pandalus).jpg",
    "Пандора (Pandora)": "Пандора (Pandora).jpg",
    "Пандрия (Pandria)": "Пандрия (Pandria).jpg",
    "Паненка (Panenka)": "Паненка (Panenka).jpg",
    "Панзола (Panzola)": "Панзола (Panzola).jpg",
    "Панорама (Panorama)": "Панорама (Panorama).jpg",
    "Пансана (Pansana)": "Пансана (Pansana).jpg",
    "Пантеон (Pantheon)": "Пантеон (Pantheon).jpg",
    "Пантера (Pantera)": "Пантера (Pantera).jpg",
    "Пантонелла (Pantonella)": "Пантонелла (Pantonella).jpg",
    "Пануччи (Panucci)": "Пануччи (Panucci).png",
    "Панчетта (Pancetta)": "Панчетта (Pancetta).jpg",
    "Полярный медведь (Polar Bear)": "Полярный медведь (Polar Bear).webp",
    "Самарская Лидия": "Самарская Лидия.jpg",
}

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to match the product objects
pattern = r'\{ "id": "(mac-\d+)", "name": "([^"]+)", "desc": "([^"]*)", "price": "(\d+)", "priceNum": (\d+), "badge": "([^"]*)", "badgeColor": "([^"]*)", "bg": "([^"]*)", "emoji": "([^"]*)" \}'

def replace_func(match):
    id_ = match.group(1)
    name = match.group(2)
    desc = match.group(3)
    price = match.group(4)
    priceNum = match.group(5)
    badge = match.group(6)
    badgeColor = match.group(7)
    bg = match.group(8)
    emoji = match.group(9)

    if emoji.startswith('<'):
        return match.group(0)

    if name in images:
        img = images[name]
        new_emoji = f'<img src="img/gor/{img}" alt="{name}" class="product-actual-img">'
        return f'{{ "id": "{id_}", "name": "{name}", "desc": "{desc}", "price": "{price}", "priceNum": {priceNum}, "badge": "{badge}", "badgeColor": "{badgeColor}", "bg": "{bg}", "emoji": "{new_emoji}" }}'
    else:
        return match.group(0)

content = re.sub(pattern, replace_func, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)