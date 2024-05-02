# This file will encoding the Video to base 64 and will attemp to decode it back to Video

def encodefile(filename):
    import base64 #import base64 module for encoding
    with open(filename, "rb") as videoFile: #Open the file and read byte from the file(First parameter)
        text = base64.b64encode(videoFile.read()) # read the file and encoded it into base64 digits
    return text #return text that stored bytes

def encodeDetails(string):
    import base64

    estring = base64.b64encode(string.encode()).decode()
    return estring

def decodeDetails(string):
    import base64

    dstring = base64.b64decode(string).decode()
    return dstring
