from django.shortcuts import render,redirect
from pytube import YouTube
from django.contrib import messages
from .models import *
# Create your views here.
def Home(request):
    fr=0
    
          
    if request.method=='POST':
                yt=request.POST.get('ytv')
                yta=YouTube(yt)
                sq=yta.streams.all()
                video=list(enumerate(sq))
                vir=Video_link.objects.all()
                
                   

               
                vi=Video_link()
                vi.link=yt
                vi.save()
                for i in vir:
                   if i.link==yt:
                        fr=i.id
                   print(fr)
                data={'v':video,'vir':vir,'fr':fr}

                return render(request,'strm.html',data)
        
    return render(request,'home.html')


#  link=" https://youtu.be/LC0ty5-75h4?si=KnRz4vkxj2R4KvkO "

#     yt=YouTube(link)
#     sq=yt.streams.all()
#     video=list(enumerate(sq))
#     for vid in video:
#         print(vid)

#     strm=int(input('enter here : '))
#     sq[strm].download()
#     print('sucessfully download......')
# except Exception as e:
#     print('Somthing went wrong please try again')

def Dwn(request,id):
    yt=''
    vir=Video_link.objects.filter(id=id)
    for i in vir:
        yt=i.link
    print(yt)

    if request.method=='POST':
        strm=request.POST.get('stm')
        strm=int(strm)
        yta=YouTube(yt)
        sq=yta.streams.all()
        video=list(enumerate(sq))
        for vid in video:
            #  print(vid)
            pass
        sq[strm].download()
        messages.success(request,'Download Sucessfully')
        return redirect('/')


#     strm=int(input('enter here : '))
#     sq[strm].download()
        # strm=int(input('enter here : '))
        # sq[strm].download()
           
                
        