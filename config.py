from typing import Dict, Any
import json
import os

def load_settings():
    default_settings = {
        'ADMINS': [], # айди админа 
        'PASSCODE_MIN_PRICE': 1,
        'AUTO_DELIVERY': False
    }
    
    try:
        if os.path.exists('settings.json'):
            with open('settings.json', 'r') as f:
                return json.load(f)
    except Exception as e:
        print(f"Error loading settings: {e}")
    
    return default_settings

SETTINGS = load_settings()

ITEMS: Dict[str, Dict[str, Any]] = {
    'PASSCODE': {
        'name': 'ПАССКОД 🔑',
        'description': '*Просто описание*',
        'secret': 'PASSCODE',
        'min_price': SETTINGS['PASSCODE_MIN_PRICE']
    }
}

MESSAGES = {
    'welcome_photo_url': 'img/logo.png',
    'welcome': 'Добро пожаловать!\nВыбери товар для покупки благодаря Telegram Stars:',
    'help': (
        '*MKch Pay*\n\nКоманды:\n'
        '/start - Посмотреть товары\n'
        '/help - Справка\n\n'
        'Как использовать:\n'
        '1. /start - посмотреть товары\n'
        '2. Выбрать товар\n'
        '3. Оплатить звездами'
    ),
    'enter_amount': f"Введите сумму оплаты (не менее {SETTINGS['PASSCODE_MIN_PRICE']} ⭐ + можете добавить свое кол-во для поддержки):",
    'invalid_amount': f"❌ Неверная сумма! Минимум {SETTINGS['PASSCODE_MIN_PRICE']} ⭐.",
    'admin_help': (
        "⚙️ *Админ-панель*\n\n"
        "Доступные команды:\n"
        "/setprice [цена] - Изменить мин. цену PASSCODE (от 1 ⭐)\n"
        "/autodelivery [on|off] - Вкл/выкл автовыдачу\n"
        "/addadmin [id] - Добавить админа\n"
        "/removeadmin [id] - Удалить админа\n"
        "/listadmins - Список админов\n"
        "/stats - Статистика продаж"
    ),
    'admin_only': "❌ Только для администраторов",
    'price_updated': "✅ Минимальная цена PASSCODE обновлена: {} ⭐",
    'delivery_status': "✅ Автовыдача {}",
    'admin_added': "✅ Админ добавлен: {}",
    'admin_removed': "✅ Админ удален: {}",
    'admin_list': "👥 Администраторы:\n{}",
    'no_admins': "👥 Администраторов нет",
    'invalid_command': "❌ Неверная команда",
    'no_codes': "⚠️ Закончились коды! Обратитесь к администратору.",
    'stats': "📊 Статистика:\nВсего покупок: {}\nУникальных покупателей: {}",
    'min_price_error': "❌ Минимальная цена должна быть не менее 1 ⭐"
}