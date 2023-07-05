from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Song,Playlist,Artist,UserProfile,Comment
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404,HttpResponseRedirect
from django. contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from.forms import CommentForm
from django.contrib.auth import get_user_model

# Create your views here.

def playallsongs(request):
    playallsongs=Song.objects.all()
    context={
        'playallsongs':playallsongs
    }
    return render(request,'index.html',context)

@login_required(login_url='signin')
def favourite_list(request):
    user = request.user
    music_list=list(Song.objects.all().values())
    new=Song.objects.filter(favourites=request.user)
    # listed=CreatePlaylist.objects.all()
    # if request.method == 'POST':
    #     name = request.POST.get('name')
    #     # Create a new BlogPost object and save it to the database
    #     blog_post = CreatePlaylist(name=name,user = request.user)
    #     blog_post.save()
    context={
        'new':new,
        'music_list':music_list,
        'profile':profile,
        # 'listed':listed,
        'username': user.username,
        'first_name': user.first_name,
    }
    return render(request,'favourites.html',context)


@login_required(login_url='signin')
def favourite_add(request, id):
    post = get_object_or_404(Song, id=id)
    if post.favourites.filter(id=request.user.id).exists():
        post.favourites.remove(request.user)
    else:
        post.favourites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def searchresult(request):
    # q=request.GET.get('q')
    if 'q' in request.GET:
        q=request.GET['q']
        data=Song.objects.filter(song_name__icontains=q)
    else:    
        data=Song.objects.all()
    context={
        'data':data
    }
    return render(request,'searchresult.html',context)

def index(request):
    playallsongs=Song.objects.all()
    artist=Artist.objects.all()
    item=Song.objects.all()
    playlist=Playlist.objects.all()
    data=Song.objects.all()
    context={
        'playlist':playlist,
        'item':item,
        'data':data,
        'artist':artist,
        'playallsongs':playallsongs
    }
    return render(request,'index.html',context)

def playlist_image(request,):
    play_img=Playlist.objects.all()
    return render(request,'release.html',{'play_img' : play_img})

def about(request):
    return render(request,'about.html')

def profile(request):
    return render(request,'profile.html')

def contacts(request):
    return render(request,'contacts.html')

def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('index')
    
    return render(request,'signin.html')



def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['fname']

        User = get_user_model()
        myuser = User.objects.create_user(username=username, email=email, password=password, first_name=first_name)
        return redirect('signin')

    return render(request, 'signup.html')

def releases(request):
    playlist=Playlist.objects.all()
    context={
        'playlist':playlist
    }
    return render(request,'releases.html',context)

def release(request,id):
    clksong=Song.objects.filter(album_id=id)
    item=Song.objects.filter(album_id=id)
    music_list=list(Song.objects.all().values())
    playlist=Playlist.objects.all()
    # createplaylist=CreatePlaylist.objects.all()
    comment=Comment.objects.filter(author_id=id)
    albname=Playlist.objects.filter(id=id)
    playlist = get_object_or_404(Playlist, id=id)
    if request.method == 'POST':
        # form = CommentForm(request.POST)
        # if form.is_valid():
        # comment = request.save(commit=False)
        content = request.POST.get('content')
        if content:
            comment = Comment(post=playlist, author=request.user, content=content)
            comment.save()

        return redirect('release', id=id)
    # else:
    #     form = CommentForm()
    context={
        'item':item,
        'music_list':music_list,
        'playlist':playlist,
        # 'playlists':playlists,
        'clksong':clksong,
        'albname':albname,
        # 'form':form,
        'comment':comment,
        # 'createplaylist':createplaylist,
        }
    return render(request,'release.html',context)



def artists(request):
    allartist=Artist.objects.all()
    context={
        'allartist':allartist
    }
    return render(request,'artists.html',context)

def artist(request,id,name):
    artistsong=Song.objects.filter(artist_name=name)
    artist=Artist.objects.filter(id=id)
    suggest=Playlist.objects.all()
    context={
        'suggest':suggest,
        'artist':artist,
        'artistsong':artistsong
    }
    return render(request,'artist.html',context)

    

def logout_view(request):
  logout(request)
  # Redirect to a success page.
  return redirect('index')

# @login_required(login_url='signin')
# def createplaylist(request):
#     user = request.user
#     music_list=list(Song.objects.all().values())
#     plays=Song.objects.filter(favourites=request.user)
#     context={
#         'plays':plays,
#         'music_list':music_list,
#     }
#     return render(request,'createplaylist.html',context)

# @login_required(login_url='signin')
# def playlist_add(request, song_id):
#     songg = get_object_or_404(Song, id=song_id)

#     playlist = CreatePlaylist.objects.get_or_create(user=request.user)

#     if song in playlist.song.all():
#         playlist.song.remove(songg)
#         message = 'Song removed from playlist.'
#     else:
#         playlist.song.add(songg)
#         message = 'Song added to playlist.'

#     context = {
#         'songg': songg,
#         'message': message,
#     }
#     return render(request,'createplaylist.html', context)