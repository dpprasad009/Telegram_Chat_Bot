import telebot
import datetime
import pytz
tz = pytz.timezone('Asia/Kolkata')

# Set the list of classes with their timings for each day
classes = {
    'Monday': [
        {'start_time': '09:00', 'end_time': '9:50', 'class_name': 'CD'},
        {'start_time': '09:50', 'end_time': '10:40', 'class_name': 'CNS'},
        {'start_time': '10:40', 'end_time': '10:50', 'class_name': 'BREAK TIME'},
        {'start_time': '10:50', 'end_time': '12:30', 'class_name': 'CRTP-APTITUDE'},
        {'start_time': '12:30', 'end_time': '13:20', 'class_name': 'LUNCH BREAK'},
        {'start_time': '13:20', 'end_time': '14:10', 'class_name': 'OOAD'},
        {'start_time': '14:10', 'end_time': '15:00', 'class_name': 'FUEE'},
        {'start_time': '15:00', 'end_time': '15:50', 'class_name': 'COUNSLING'},
        {'start_time': '15:50', 'end_time': '16:30', 'class_name': 'CULB'},
    ],
    'Tuesday': [
        {'start_time': '09:00', 'end_time': '9:50', 'class_name': 'OOAD'},
        {'start_time': '09:50', 'end_time': '12:30', 'class_name': 'ML/CD _LAB'},
        {'start_time': '10:40', 'end_time': '10:50', 'class_name': 'BREAK TIME'},
        {'start_time': '12:30', 'end_time': '13:20', 'class_name': 'LUNCH BREAK'},
        {'start_time': '13:20', 'end_time': '14:10', 'class_name': 'CNS'},
        {'start_time': '14:10', 'end_time': '15:00', 'class_name': 'CD'},
        {'start_time': '15:00', 'end_time': '15:50', 'class_name': 'ES-II'},
        {'start_time': '15:50', 'end_time': '16:30', 'class_name': 'CULB'},
    ],
    'Wednesday': [
        {'start_time': '09:00', 'end_time': '9:50', 'class_name': 'ML'},
        {'start_time': '09:50', 'end_time': '10:40', 'class_name': 'SOC'},
        {'start_time': '10:40', 'end_time': '10:50', 'class_name': 'BREAK TIME'},
        {'start_time': '10:50', 'end_time': '11:40', 'class_name': 'OOAD'},
        {'start_time': '11:40', 'end_time': '12:30', 'class_name': 'CD'},
        {'start_time': '12:30', 'end_time': '13:20', 'class_name': 'LUNCH BREAK'},
        {'start_time': '13:20', 'end_time': '15:00', 'class_name': 'CRTP-ENGLISH'},
        {'start_time': '15:00', 'end_time': '15:50', 'class_name': 'ML'},
        {'start_time': '15:50', 'end_time': '16:30', 'class_name': 'CULB'},
    ],
    'Thursday': [
        {'start_time': '09:00', 'end_time': '9:50', 'class_name': 'FUEE'},
        {'start_time': '09:50', 'end_time': '10:40', 'class_name': 'CNS'},
        {'start_time': '10:40', 'end_time': '10:50', 'class_name': 'BREAK TIME'},
        {'start_time': '10:50', 'end_time': '11:40', 'class_name': 'CD'},
        {'start_time': '11:40', 'end_time': '12:30', 'class_name': 'ML'},
        {'start_time': '12:30', 'end_time': '13:20', 'class_name': 'LUNCH BREAK'},
        {'start_time': '13:20', 'end_time': '15:50', 'class_name': 'SOC_LAB'},
        {'start_time': '15:50', 'end_time': '16:30', 'class_name': 'CULB'},
    ],
    'Friday': [
        {'start_time': '09:00', 'end_time': '9:50', 'class_name': 'ES-II'},
        {'start_time': '09:50', 'end_time': '12:30', 'class_name': 'FUEE'},
        {'start_time': '10:40', 'end_time': '10:50', 'class_name': 'BREAK TIME'},
        {'start_time': '10:50', 'end_time': '12:40', 'class_name': 'CRTP-PROGRAMMING'},
        {'start_time': '12:30', 'end_time': '13:20', 'class_name': 'LUNCH BREAK'},
        {'start_time': '13:20', 'end_time': '15:50', 'class_name': 'CD/ML_LAB'},
        {'start_time': '15:50', 'end_time': '16:30', 'class_name': 'CULB'},
    ],
    'Saturday': [
        {'start_time': '09:00', 'end_time': '9:50', 'class_name': 'ML'},
        {'start_time': '09:50', 'end_time': '12:30', 'class_name': 'FUEE'},
        {'start_time': '10:40', 'end_time': '10:50', 'class_name': 'BREAK TIME'},
        {'start_time': '10:50', 'end_time': '11:40', 'class_name': 'OOAD'},
        {'start_time': '11:40', 'end_time': '12:30', 'class_name': 'CNS'},
        {'start_time': '12:30', 'end_time': '13:20', 'class_name': 'LUNCH BREAK'},
        {'start_time': '13:20', 'end_time': '15:50', 'class_name': 'CNS_LAB'},
        {'start_time': '15:50', 'end_time': '16:30', 'class_name': 'CULB'},
    ],
    'Sunday': [
        {'start_time': '09:00', 'end_time': '9:50', 'class_name': 'COLLEGE HOILDAY'},
    ],

}

# Create a new Telegram bot object
bot = telebot.TeleBot('6208709165:AAHV0CIHNBtA_B0MM4hSmyaxT8ess7SOO8I')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hi there, how can I assist you?")

@bot.message_handler(func=lambda message: True, content_types=['new_chat_members'])
def welcome_message(message):
    for member in message.new_chat_members:
        bot.send_message(message.chat.id, f"Welcome {member.first_name} to the group!")

# Define a message handler for text messages
@bot.message_handler(func=lambda message: True)
def reply_to_hi(message):
    # Check if the message is "Hi"
    if message.text.lower() == "hi" or message.text.lower() == "hello" or message.text.lower() == "hai" or message.text.lower() == "hey" :
        # Get the name of the group where the message was sent
        chat = message.chat
        if chat.type == 'group' or chat.type == 'supergroup':
            group_name = chat.title
        else:
            group_name = "a private chat"

        # Reply to the user with a message including the group name
        reply = f"Hi {message.from_user.first_name}!" +"😊" + f".\nWelcome to {group_name}."
        bot.reply_to(message, reply)
    elif message.text.lower() == "class" or message.text.lower() == "period" :
      day = datetime.datetime.now(tz).strftime("%A")
      time = datetime.datetime.now(tz).strftime("%H:%M")
      class_name = None
      for c in classes[day]:
        start_time = datetime.datetime.strptime(c['start_time'], '%H:%M')
        end_time = datetime.datetime.strptime(c['end_time'], '%H:%M')
        current_time = datetime.datetime.strptime(time, '%H:%M')
        if start_time <= current_time <= end_time:
            class_name = c['class_name']
            break
      if class_name:
        time_obj = datetime.datetime.strptime(time, '%H:%M')
        ntime = time_obj.strftime('%I:%M %p')
        bot.reply_to(message, f"Your class for {day} at {ntime} is {class_name}")
      else:
        bot.reply_to(message, f"No class found for {day} at {time}")
    elif message.text.lower() == "timetable" or message.text.lower() == "schedule" or message.text.lower() == "time table" :
        chat_id = message.chat.id
        bot.reply_to(message, f"Dear {message.from_user.first_name},\nYour TimeTable is........⏱️")
        # Replace /path/to/image.jpg with the actual path to your image file
        photo_path = 'timetable.jpg'
        # Open the image file
        with open(photo_path, 'rb') as f:
            photo = f.read()

        # Send the photo to the bot's chat
        bot.send_photo(chat_id, photo=photo)
    elif message.text.lower() == "syllabus" :
        chat_id = message.chat.id
        bot.reply_to(message, f"Dear {message.from_user.first_name},\nYour Syllabus is........📖")
        # Replace /path/to/image.jpg with the actual path to your image file
        file_path = 'syllbus.pdf'
        bot.send_document(chat_id=chat_id, document=open(file_path, 'rb'))

    elif message.text.lower() == "cns" or \
                                    message.text.lower() == "ml" or \
                                    message.text.lower() == "cd" or \
                                    message.text.lower() == "ooad" or \
                                    message.text.lower() == "fuee" or \
                                    message.text.lower() == "cns notes" or \
                                    message.text.lower() == "ml notes" or \
                                    message.text.lower() == "cd notes" or \
                                    message.text.lower() == "ooad notes" or \
                                    message.text.lower() == "fuee notes" or \
                                    message.text.lower() == "cns materials" or \
                                    message.text.lower() == "ml materials" or \
                                    message.text.lower() == "cd materials" or \
                                    message.text.lower() == "ooad materials" or \
                                    message.text.lower() == "fuee materials" or \
                                    message.text.lower() == "p&s materials" or \
                                    message.text.lower() == "p&s material" or \
                                    message.text.lower() == "material" or \
                                    message.text.lower() == "materials" or \
                                    message.text.lower() == "books" or \
                                    message.text.lower() == "book" or \
                                    message.text.lower() == "papers" or \
                                    message.text.lower() == "notes" :
        bot.reply_to(message, f"Dear {message.from_user.first_name},\nYour Notes/Materials is........📖 \n\n https://t.me/cse_sviet")
    else :

        fl = f"Sorry {message.from_user.first_name}!" + "😔" + "\nCould Not Understand You !!. Please try Agian.......!!"
        bot.reply_to(message, fl)

    print(message.text)


# Disable the webhook before starting the long polling method
bot.delete_webhook()

# Start the bot
bot.polling()
