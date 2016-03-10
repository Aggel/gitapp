from PIL import Image
import struct

print "Δώσε την διεύθυνση της εικόνας που θες"
image=raw_input()
import webbrowser
webbrowser.open(image)
picture=image.load()
print "Το μέγεθος της εικόνας είναι:"
print image.size
color1=image[10,100]
color2=image[50,200]
color3=image[200,50]
color4=image[150,150]
color5=image[100,10]

print " Τα χρώματα της εικόνας σε δεκαεξαδική μορφή είναι:"
def rgb2hex(color1):
    return struct.pack('BBB',*color1).encode('hex')

def rgb2hex(color2):
    return struct.pack('BBB',*color2).encode('hex')

def rgb2hex(color3):
    return struct.pack('BBB',*color3).encode('hex')

def rgb2hex(color4):
    return struct.pack('BBB',*color4).encode('hex')

def rgb2hex(color5):
    return struct.pack('BBB',*color5).encode('hex')
