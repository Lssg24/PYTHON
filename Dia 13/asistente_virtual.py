import datetime

import pyttsx3
import speech_recognition as sr


# escuchar nuestro microfono y devolver un string
def transformar_audio_en_texto():
    # almacenar recognizer en variable
    r = sr.Recognizer()

    with sr.Microphone() as origen:
        # tiempo de espera
        r.pause_threshold = 0.8

        # informar que comenzo la grabacion
        print('ya puedes hablar')
        # guardar lo que escuche como audio
        audio = r.listen(origen)
        try:
            # buscar en google lo que haya escuchado
            pedido = r.recognize_google(audio, language="es-cl")
            # preuba de audio
            print('Dijiste:' + pedido)
            # devolver a pedido
            return pedido
        # en caso que no comprenda el audio
        except sr.UnknownValueError:
            print('no entendi')
            return 'sigo esperando'
        except sr.RequestError:
            print('sigo esperando')
            return 'sigo esperando'
        except:
            print('algo ha salido mal')
            return 'sigo esperando'


# transformar_audio_en_texto()


def hablar(mensaje):
    # encender motor de pyttsx3
    engine = pyttsx3.init()
    # pued configurar la voz
    engine.setProperty('voice', id1)
    # pronunciasr mensaje
    engine.say(mensaje)
    engine.runAndWait()


'''engine = pyttsx3.init()
for voz in engine.getProperty('voices'):
    print(voz)
'''


def pedir_dia():
    dia = datetime.date.today()
    print(dia)

    dia_semana = dia.weekday()
    print(dia_semana)

    calendario = {0: 'Lunes', 1: 'Martes', 2: 'Miércoles', 3: 'Jueves', 4: 'Viernes', 5: 'Sábado', 6: 'Domingo'}

    # decir el dia de la semana
    hablar(f'Hoy es {calendario[dia_semana]}')


def pedir_hora():
    hora = datetime.datetime.now()
    hora = f'En este momento son las {hora.hour} horas con {hora.minute} minutos'
    print(hora)
    hablar(hora)


# opciones de voz
id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0'
id2 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'

pedir_hora()
