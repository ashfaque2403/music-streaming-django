from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('playallsongs',views.playallsongs,name='playallsongs'),
    path('about/',views.about,name='about'),
    path('profile/',views.profile,name='profile'),
    path('contacts/',views.contacts,name='contacts'),
    path('signin/',views.signin,name='signin'),
    path('signup/',views.signup,name='signup'),
    path('releases/',views.releases,name='releases'),
    path('release/<int:id>',views.release,name='release'),
    path('artists/',views.artists,name='artists'),
    path('artist/<int:id><str:name>',views.artist,name='artist'),
    path('fav/<int:id>', views.favourite_add, name='favourite_add'),
    path('favourites/', views.favourite_list, name='favourites'),
    path('searchresult/', views.searchresult, name='searchresult'),
    path('logout/', views.logout_view, name='logout'),
    # path('createplaylist/', views.createplaylist, name='createplaylist'),
    # path('playlist_add/<int:song_id>', views.playlist_add, name='playlist_add'),
    # path('add-song/', views.add_song_view, name='add_song'),
    # path('artistsong/<int:name>', views.artistsong, name='artistsong'),

]
