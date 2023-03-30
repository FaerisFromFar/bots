import pymysql
from telebot import *

config = {
    'user': 'root',
    'password': '20050722',
    'host': 'localhost',
    'db': 'test123'
}

cnx = pymysql.connect(**config)
print('успех')

TOKEN = '6036460146:AAEW1u8G2lG2hLwJFJm3No0Bb6kUn51uba4'
bot = telebot.TeleBot(TOKEN)



keyboard = types.InlineKeyboardMarkup()
btn_ap11 = types.InlineKeyboardButton(text='АП-11', callback_data='get_all_students_ap11')
btn_tm11 = types.InlineKeyboardButton(text='ТМ-11', callback_data='get_all_students_tm11')
btn_ga11 = types.InlineKeyboardButton(text='ГА-11', callback_data='get_all_students_ga11')
btn_rt11 = types.InlineKeyboardButton(text='РТ-11', callback_data='get_all_students_rt11')
btn_nr11 = types.InlineKeyboardButton(text='НР-11', callback_data='get_all_students_nr11')
keyboard.row(btn_ap11, btn_tm11,btn_ga11,btn_rt11,btn_nr11 )


# обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton('/Cписок_Групп'))
    markup.add(types.KeyboardButton('/Изменить_Часы'))
    markup.add(types.KeyboardButton('/Пропуски'))
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Выберите действие:', reply_markup=markup)
    print('кто-то новый')


# обработчик команды /Cписок_Групп
@bot.message_handler(commands=['Cписок_Групп'])
def send_students_keyboard(message):
    bot.send_message(message.chat.id, 'Выберите группу:', reply_markup=keyboard)


############################################################################################
# обработчик команды Пропуски
@bot.message_handler(commands=['Пропуски'])
def update_hours(message):
    try:
        # создаем кнопки для выбора группы
        keyboard = types.InlineKeyboardMarkup()
        btn_ap11 = types.InlineKeyboardButton(text='АП-11', callback_data='leave_output_ap11')
        btn_tm11 = types.InlineKeyboardButton(text='ТМ-11', callback_data='leave_output_tm11')
        btn_ga11 = types.InlineKeyboardButton(text='ГА-11', callback_data='leave_output_ga11')
        btn_rt11 = types.InlineKeyboardButton(text='РТ-11', callback_data='leave_output_rt11')
        btn_nr11 = types.InlineKeyboardButton(text='НР-11', callback_data='leave_output_nr11')
        keyboard.row(btn_ap11, btn_tm11,btn_ga11,btn_rt11,btn_nr11)

        # отправляем сообщение с кнопками выбора группы
        bot.send_message(message.chat.id, 'Выберите группу, для которой нужно посчитать количество пропусков:',reply_markup=keyboard)
    except ValueError:
        bot.send_message(message.chat.id, 'Ошибка: неверное значение')


@bot.callback_query_handler(func=lambda call: call.data == 'leave_output_ap11')
def leave_output_ap11(call):
    # создание объекта курсора для выполнения запросов
    with cnx.cursor() as cursor:
        # выполнение запроса на выборку всех записей из таблицы students
        cursor.execute("SELECT name, hours FROM students WHERE hours > 0")
        # получение всех записей
        rows = cursor.fetchall()
        # формирование сообщения с результатом
        response = "Список пропусков у АП-11:\n\n"
        for row in rows:
            response += f"{row[0]}  |  часы: {row[1]} \n"
        # отправка сообщения в чат
        bot.send_message(call.message.chat.id, response)



@bot.callback_query_handler(func=lambda call: call.data == 'leave_output_ga11')
def leave_output_tm11(call):
    # создание объекта курсора для выполнения запросов
    with cnx.cursor() as cursor:
        # выполнение запроса на выборку всех записей из таблицы students
        cursor.execute("SELECT name, hours FROM ga11 WHERE hours > 0")
        # получение всех записей
        rows = cursor.fetchall()
        # формирование сообщения с результатом
        response = "Список пропусков у ГА-11:\n\n"
        for row in rows:
            response += f"{row[0]}  |  часы: {row[1]} \n"
        # отправка сообщения в чат
        bot.send_message(call.message.chat.id, response)


@bot.callback_query_handler(func=lambda call: call.data == 'leave_output_rt11')
def leave_output_tm11(call):
    # создание объекта курсора для выполнения запросов
    with cnx.cursor() as cursor:
        # выполнение запроса на выборку всех записей из таблицы students
        cursor.execute("SELECT name, hours FROM rt11 WHERE hours > 0")
        # получение всех записей
        rows = cursor.fetchall()
        # формирование сообщения с результатом
        response = "Список пропусков у РТ-11:\n\n"
        for row in rows:
            response += f"{row[0]}  |  часы: {row[1]} \n"
        # отправка сообщения в чат
        bot.send_message(call.message.chat.id, response)


@bot.callback_query_handler(func=lambda call: call.data == 'leave_output_nr11')
def leave_output_tm11(call):
    # создание объекта курсора для выполнения запросов
    with cnx.cursor() as cursor:
        # выполнение запроса на выборку всех записей из таблицы students
        cursor.execute("SELECT name, hours FROM nr11 WHERE hours > 0")
        # получение всех записей
        rows = cursor.fetchall()
        # формирование сообщения с результатом
        response = "Список пропусков у НР-11:\n\n"
        for row in rows:
            response += f"{row[0]}  |  часы: {row[1]} \n"
        # отправка сообщения в чат
        bot.send_message(call.message.chat.id, response)


@bot.callback_query_handler(func=lambda call: call.data == 'leave_output_tm11')
def leave_output_tm11(call):
    # создание объекта курсора для выполнения запросов
    with cnx.cursor() as cursor:
        # выполнение запроса на выборку всех записей из таблицы students
        cursor.execute("SELECT name, hours FROM tm11 WHERE hours > 0")
        # получение всех записей
        rows = cursor.fetchall()
        # формирование сообщения с результатом
        response = "Список пропусков у TM-11:\n\n"
        for row in rows:
            response += f"{row[0]}  |  часы: {row[1]} \n"
        # отправка сообщения в чат
        bot.send_message(call.message.chat.id, response)


############################################################################################

@bot.callback_query_handler(func=lambda call: call.data == 'get_all_students_ap11')
def get_all_students_callback(call):
    # создание объекта курсора для выполнения запросов
    with cnx.cursor() as cursor:
        # выполнение запроса на выборку всех записей из таблицы students
        cursor.execute("SELECT * FROM students")
        # получение всех записей
        rows = cursor.fetchall()
        # формирование сообщения с результатом
        response = "АП-11:\n\n"
        for row in rows:
            response += f"{row[0]}. {row[1]}   |   {row[3]}   |   часы {row[2]} \n"
        # отправка сообщения в чат
        bot.send_message(call.message.chat.id, response)

@bot.callback_query_handler(func=lambda call: call.data == 'get_all_students_tm11')
def get_all_students_callback(call):
    # создание объекта курсора для выполнения запросов
    with cnx.cursor() as cursor:
        # выполнение запроса на выборку всех записей из таблицы students
        cursor.execute("SELECT * FROM tm11")
        # получение всех записей
        rows = cursor.fetchall()
        # формирование сообщения с результатом
        response = "ТМ-11:\n\n"
        for row in rows:
            response += f"{row[0]}. {row[1]}   |   {row[3]}   |   часы {row[2]} \n"
        # отправка сообщения в чат
        bot.send_message(call.message.chat.id, response)

@bot.callback_query_handler(func=lambda call: call.data == 'get_all_students_ga11')
def get_all_students_callback(call):
    # создание объекта курсора для выполнения запросов
    with cnx.cursor() as cursor:
        # выполнение запроса на выборку всех записей из таблицы students
        cursor.execute("SELECT * FROM ga11")
        # получение всех записей
        rows = cursor.fetchall()
        # формирование сообщения с результатом
        response = "ГА-11:\n\n"
        for row in rows:
            response += f"{row[0]}. {row[1]}   |   {row[3]}   |   часы {row[2]} \n"
        # отправка сообщения в чат
        bot.send_message(call.message.chat.id, response)

@bot.callback_query_handler(func=lambda call: call.data == 'get_all_students_rt11')
def get_all_students_callback(call):
    # создание объекта курсора для выполнения запросов
    with cnx.cursor() as cursor:
        # выполнение запроса на выборку всех записей из таблицы students
        cursor.execute("SELECT * FROM rt11")
        # получение всех записей
        rows = cursor.fetchall()
        # формирование сообщения с результатом
        response = "РТ-11:\n\n"
        for row in rows:
            response += f"{row[0]}. {row[1]}   |   {row[3]}   |   часы {row[2]} \n"
        # отправка сообщения в чат
        bot.send_message(call.message.chat.id, response)

@bot.callback_query_handler(func=lambda call: call.data == 'get_all_students_nr11')
def get_all_students_callback(call):
    # создание объекта курсора для выполнения запросов
    with cnx.cursor() as cursor:
        # выполнение запроса на выборку всех записей из таблицы students
        cursor.execute("SELECT * FROM nr11")
        # получение всех записей
        rows = cursor.fetchall()
        # формирование сообщения с результатом
        response = "НР-11:\n\n"
        for row in rows:
            response += f"{row[0]}. {row[1]}   |   {row[3]}   |   часы {row[2]} \n"
        # отправка сообщения в чат
        bot.send_message(call.message.chat.id, response)
##########################################################################################

# обработчик команды /update_hours
@bot.message_handler(commands=['Изменить_Часы'])
def update_hours(message):
    try:
        # создаем кнопки для выбора группы
        keyboard = types.InlineKeyboardMarkup()
        btn_ap11 = types.InlineKeyboardButton(text='АП-11', callback_data='update_hours_ap11')
        btn_tm11 = types.InlineKeyboardButton(text='ТМ-11', callback_data='update_hours_tm11')
        btn_ga11 = types.InlineKeyboardButton(text='ГА-11', callback_data='update_hours_ga11')
        btn_rt11 = types.InlineKeyboardButton(text='РТ-11', callback_data='update_hours_rt11')
        btn_nr11 = types.InlineKeyboardButton(text='НР-11', callback_data='update_hours_nr11')
        keyboard.row(btn_ap11, btn_tm11,btn_ga11,btn_rt11,btn_nr11)

        # отправляем сообщение с кнопками выбора группы
        bot.send_message(message.chat.id, 'Выберите группу, для которой нужно изменить количество часов:',reply_markup=keyboard)
    except ValueError:
        bot.send_message(message.chat.id, 'Ошибка: неверное значение')



# update_hours_ap11
@bot.callback_query_handler(func=lambda call: call.data == 'update_hours_ap11')
def update_hours_ap11_callback(call):
    # запрашиваем у пользователя ID студента и количество часов
    bot.send_message(call.message.chat.id, "Введите ID студента АП и количество часов в формате 'ID часы':")

    # обработчик сообщений, в котором будет получено ID студента и количество часов
    @bot.message_handler(func=lambda m: True)
    def on_hours_received(message):
        try:
            # получение ID студента и количества часов из сообщения
            student_id, hours = message.text.split()
            # создание объекта курсора для выполнения запросов
            with cnx.cursor() as cursor:
                # выполнение запроса на обновление количества часов студента в таблице students
                cursor.execute("UPDATE students SET hours = %s WHERE id = %s", (hours, student_id))
                # сохранение изменений
                cnx.commit()
            # отправка сообщения в чат
            bot.send_message(message.chat.id, f"Количество часов для студента с ID {student_id} изменено на {hours}.")
        except ValueError:
            #отправка сообщения об ошибке пользователю
            bot.send_message(message.chat.id, "Неверный формат сообщения. Пожалуйста, введите ID студента и количество часов в формате 'ID часы'.")




# update_hours_tm11
@bot.callback_query_handler(func=lambda call: call.data == 'update_hours_tm11')
def update_hours_tm11_callback(call):
    # запрашиваем у пользователя ID студента и количество часов
    bot.send_message(call.message.chat.id, "Введите ID студента ТМ и количество часов в формате 'ID часы':")

    # обработчик сообщений, в котором будет получено ID студента и количество часов
    @bot.message_handler(func=lambda m: True)
    def on_hours_received(message):
        try:
            # получение ID студента и количества часов из сообщения
            student_id, hours = message.text.split()
            # создание объекта курсора для выполнения запросов
            with cnx.cursor() as cursor:
                # выполнение запроса на обновление количества часов студента в таблице tm11
                cursor.execute("UPDATE tm11 SET hours = %s WHERE id = %s", (hours, student_id))
                # сохранение изменений
                cnx.commit()
            # отправка сообщения в чат
            bot.send_message(message.chat.id, f"Количество часов для студента с ID {student_id} изменено на {hours}.")
        except ValueError:
            # отправка сообщения об ошибке пользователю
            bot.send_message(message.chat.id,
                             "Неверный формат сообщения. Пожалуйста, введите ID студента и количество часов в формате 'ID часы'.")





@bot.callback_query_handler(func=lambda call: call.data == 'update_hours_ga11')
def update_hours_ap11_callback(call):
    # запрашиваем у пользователя ID студента и количество часов
    bot.send_message(call.message.chat.id, "Введите ID студента ГА и количество часов в формате 'ID часы':")

    # обработчик сообщений, в котором будет получено ID студента и количество часов
    @bot.message_handler(func=lambda m: True)
    def on_hours_received(message):
        try:
            # получение ID студента и количества часов из сообщения
            student_id, hours = message.text.split()
            # создание объекта курсора для выполнения запросов
            with cnx.cursor() as cursor:
                # выполнение запроса на обновление количества часов студента в таблице students
                cursor.execute("UPDATE ga11 SET hours = %s WHERE id = %s", (hours, student_id))
                # сохранение изменений
                cnx.commit()
            # отправка сообщения в чат
            bot.send_message(message.chat.id, f"Количество часов для студента с ID {student_id} изменено на {hours}.")
        except ValueError:
            #отправка сообщения об ошибке пользователю
            bot.send_message(message.chat.id, "Неверный формат сообщения. Пожалуйста, введите ID студента и количество часов в формате 'ID часы'.")






@bot.callback_query_handler(func=lambda call: call.data == 'update_hours_rt11')
def update_hours_ap11_callback(call):
    # запрашиваем у пользователя ID студента и количество часов
    bot.send_message(call.message.chat.id, "Введите ID студента РТ и количество часов в формате 'ID часы':")

    # обработчик сообщений, в котором будет получено ID студента и количество часов
    @bot.message_handler(func=lambda m: True)
    def on_hours_received(message):
        try:
            # получение ID студента и количества часов из сообщения
            student_id, hours = message.text.split()
            # создание объекта курсора для выполнения запросов
            with cnx.cursor() as cursor:
                # выполнение запроса на обновление количества часов студента в таблице students
                cursor.execute("UPDATE rt11 SET hours = %s WHERE id = %s", (hours, student_id))
                # сохранение изменений
                cnx.commit()
            # отправка сообщения в чат
            bot.send_message(message.chat.id, f"Количество часов для студента с ID {student_id} изменено на {hours}.")
        except ValueError:
            #отправка сообщения об ошибке пользователю
            bot.send_message(message.chat.id, "Неверный формат сообщения. Пожалуйста, введите ID студента и количество часов в формате 'ID часы'.")






@bot.callback_query_handler(func=lambda call: call.data == 'update_hours_nr11')
def update_hours_ap11_callback(call):
    # запрашиваем у пользователя ID студента и количество часов
    bot.send_message(call.message.chat.id, "Введите ID студента НР и количество часов в формате 'ID часы':")

    # обработчик сообщений, в котором будет получено ID студента и количество часов
    @bot.message_handler(func=lambda m: True)
    def on_hours_received(message):
        try:
            # получение ID студента и количества часов из сообщения
            student_id, hours = message.text.split()
            # создание объекта курсора для выполнения запросов
            with cnx.cursor() as cursor:
                # выполнение запроса на обновление количества часов студента в таблице students
                cursor.execute("UPDATE nr11 SET hours = %s WHERE id = %s", (hours, student_id))
                # сохранение изменений
                cnx.commit()
            # отправка сообщения в чат
            bot.send_message(message.chat.id, f"Количество часов для студента с ID {student_id} изменено на {hours}.")
        except ValueError:
            #отправка сообщения об ошибке пользователю
            bot.send_message(message.chat.id, "Неверный формат сообщения. Пожалуйста, введите ID студента и количество часов в формате 'ID часы'.")



bot.polling()