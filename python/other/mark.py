import speech_recognition as sr
import pyttsx3

# Инициализация синтеза речи
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Настройка скорости речи

# Функция для синтеза речи
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Функция для распознавания речи
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Слушаю...")
        audio = recognizer.listen(source)
        try:
            print("Распознаю...")
            query = recognizer.recognize_google(audio, language="ru-RU")
            print(f"Вы сказали: {query}")
            return query.lower()
        except sr.UnknownValueError:
            speak("Извините, я не могу вас понять.")
            return None
        except sr.RequestError:
            speak("Ошибка соединения с сервером распознавания речи.")
            return None

# Основной цикл голосового помощника
def main():
    speak("Привет! КОД БАЙ ФЕДЯ")
    while True:
        query = listen()
        if query:
            if "привет" in query:
                speak("Привет, как я могу помочь?")
            elif "погода" in query:
                speak("Сожалею, я не могу предоставить информацию о погоде.")
            elif "пока" in query:
                speak("До свидания!")
                break
            else:
                speak("Извините, я не знаю, как ответить на этот запрос.")

if name == "main":
    main()