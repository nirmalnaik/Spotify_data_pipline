#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install spotipy


# In[2]:


import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd


# In[3]:


client_credentials_manager = SpotifyClientCredentials(client_id="9dfb5d986fba4cf895aaca0487eb18ff", client_secret="d3eb5a9f2cc54e5298b60046f0528e4d")


# In[4]:


sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)


# In[5]:


playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbNG2KDcFcKOF?si=1333723a6eff4b7f"


# In[6]:


playlist_URI = playlist_link.split("/")[-1].split("?")[0]


# In[7]:


data = sp.playlist_tracks(playlist_URI)


# In[8]:


data['items'][0]['track']['album']['id']


# In[9]:


data['items'][0]['track']['album']['name']


# In[10]:


data['items'][0]['track']['album']['release_date']


# In[11]:


data['items'][0]['track']['album']['total_tracks']


# In[12]:


data['items'][0]['track']['album']['external_urls']['spotify']


# In[13]:


album_list = []
for row in data['items']:
    album_id = row['track']['album']['id']
    album_name = row['track']['album']['name']
    album_release_date = row['track']['album']['release_date']
    album_total_tracks = row['track']['album']['total_tracks']
    album_url = row['track']['album']['external_urls']['spotify']
    album_element = {'album_id':album_id,'name':album_name,'release_date':album_release_date,
                        'total_tracks':album_total_tracks,'url':album_url}
    album_list.append(album_element)


# In[14]:


album_list


# In[16]:


artist_list = []
for row in data['items']:
    for key, value in row.items():
        if key == "track":
            for artist in value['artists']:
                artist_dict = {'artist_id':artist['id'], 'artist_name':artist['name'], 'external_url': artist['href']}
                artist_list.append(artist_dict)


# In[17]:


artist_list


# In[18]:


song_list = []
for row in data['items']:
    song_id = row['track']['id']
    song_name = row['track']['name']
    song_duration = row['track']['duration_ms']
    song_url = row['track']['external_urls']['spotify']
    song_popularity = row['track']['popularity']
    song_added = row['added_at']
    album_id = row['track']['album']['id']
    artist_id = row['track']['album']['artists'][0]['id']
    song_element = {'song_id':song_id,'song_name':song_name,'duration_ms':song_duration,'url':song_url,
                    'popularity':song_popularity,'song_added':song_added,'album_id':album_id,
                    'artist_id':artist_id
                   }
    song_list.append(song_element)


# In[19]:


album_df= pd.DataFrame(album_list) 


# In[21]:


album_df.head()


# In[22]:


album_df = album_df.drop_duplicates(subset=['album_id'])


# In[23]:


artist_df = pd.DataFrame.from_dict(artist_list)


# In[24]:


artist_df = artist_df.drop_duplicates(subset=['artist_id'])


# In[25]:


song_df = pd.DataFrame.from_dict(song_list)


# In[26]:


song_df.head()


# In[27]:


artist_df.head()


# In[28]:


album_df.head()


# In[29]:


album_df['release_date'] = pd.to_datetime(album_df['release_date'])


# In[30]:


song_df['song_added'] =  pd.to_datetime(song_df['song_added'])


# In[31]:


song_df.info()


# In[ ]:




