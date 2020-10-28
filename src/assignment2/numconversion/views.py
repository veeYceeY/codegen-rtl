from django.shortcuts import render

# Create your views here.

################################# SIMPLY DONE WITH LIBRARY #############################

# def home(request):
#     if request.method=='POST':
#         number=request.POST['input']
#         from num2words import num2words
#         output=num2words(number)
#         text="one thousand"
        
#         import gtts
#         from playsound import playsound
#         tts = gtts.gTTS(output)
#         tts.save("number.mp3")

#         import os
#         file="number.mp3"
#         os.system("mpg123 " + file)
#         return render(request,'home.html',{'output':output,'input':number})
#     else:
#         return render(request,'home.html')


################################# MANUAL CODE #############################
import os

def home(request):
    if request.method=='POST':
        number=request.POST['number']
        #number to word coversion using manual function
        output=number2word(int(number)) 
        #text to speech conversion using gtts       
        import gtts
        # from playsound import playsound
        tts = gtts.gTTS(output)
        tts.save("number.wav")
        #playing number.mp3 using python backend
        os.system("mpg123 " + "number.wav")
        ########################################################################
        from django.conf import settings
        from .models import converted
        converted= converted.objects.get(id=1)
        initial_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"/"+"number.wav"
        # initial_path = "/home/veeyceey/Documents/workspace/sammu/assignment2/number.wav"
        print("===================================")
        converted.audio.name = "number.wav"

        new_path = settings.MEDIA_ROOT +"/" +converted.audio.name
        # Move the file on the filesystem
        os.rename(initial_path, new_path)
        
        # pathFile=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"/"+"number.wav"
        #rendering response
        return render(request,'home.html',{'output':output,'input':number,'audiofile':"number.wav"})
    else:
        return render(request,'home.html')

#function to convert number to word
def number2word(number):
    ones = ['zero', 'one', 'two', 'three', 'four','five', 'six', 'seven', 'eight', 'nine','ten', 'eleven', 'twelve', 'thirteen', 'fourteen','fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['zero', 'ten', 'twenty', 'thirty', 'forty','fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    for order, word in [(10**12, "trillion"), (10**9, "billion"),(10**5, "lack"), (10**3, "thousand")]:
        if number >= order:
            return "{0} {1}{2}".format(number2word(number // order), word," {0}".format(number2word(number % order))
            if number % order else "")
    if number >= 100:
        if number % 100:
            return "{0} hundred and {1}".format(number2word(number // 100), number2word(number % 100))
        else:
            return "{0} hundred".format(number2word(number // 100))
    if number < 20:
        return ones[number]
    else:
        return "{0}{1}".format(tens[number // 10]," {0}".format(number2word(number % 10)) 
        if number % 10 else "")  
