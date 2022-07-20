import urllib.request
import webbrowser
def openwindows():
    webbrowser.open(url='http://172.20.10.2/', new=0, autoraise=True)
    webbrowser.open(url='http://172.20.10.3/', new=0, autoraise=True)
    webbrowser.open(url='http://172.20.10.4/', new=0, autoraise=True)

def stoprecord():
    urllib.request.urlopen('http://172.20.10.2/stop')
    urllib.request.urlopen('http://172.20.10.3/stop')
    urllib.request.urlopen('http://172.20.10.4/stop')

def startrecord():
    urllib.request.urlopen('http://172.20.10.2/start?framesize=UVGA&length=3600&interval=500&quality=10&repeat=100&speed=30&gray=0')
    urllib.request.urlopen('http://172.20.10.3/start?framesize=UVGA&length=3600&interval=500&quality=10&repeat=100&speed=30&gray=0')
    urllib.request.urlopen('http://172.20.10.4/start?framesize=UVGA&length=3600&interval=500&quality=10&repeat=100&speed=30&gray=0')