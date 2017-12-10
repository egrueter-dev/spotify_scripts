'''
The first example from http://spotipy.readthedocs.io/en/latest/
Added authentication for this application

---------------------------------------

Expected output:
Beautiful Lies
Fire Within
Live In London
Birdy
Birdy
Birdy (Deluxe Version)

{'tracks': {'href': 'https://api.spotif.......

---------------------------------------

When run, depending on the value of the variable "scope", this code may ask for spotify authentication in web browser,
then may ask in command line of what url gets returned, it should be something of the form
https://example.com/callback/?code=[SOME ALPHANUMERIC CODE HERE]

It's pretty annoying to have to copy paste every time you run, there is probably a way to 
automate this using the caching option or setting up an HTTP server on localhost.

My quick fix:
Changed my line 80 of util.py in spotipy library to hardcode in the url 
returned during authentication because of limitations of Sublime Text (raw input doesen't work??)
Was:
response = raw_input("Enter the URL you were redirected to: ")
Now:
response = '<the url that gets returned in callback>'

----------------------------------------
'''

import spotipy
import spotipy.util as util

#------------------Authentication-----------------------
username='W'
scope=''
SPOTIPY_CLIENT_ID = 'afec6b91ff52456495b1ad91b2247de4'
SPOTIPY_CLIENT_SECRET = '80de1fb094814b7086bb9022defd640e'
SPOTIPY_REDIRECT_URI = 'https://example.com/callback/'

token = util.prompt_for_user_token(username, scope=scope, client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri = 'https://example.com/callback/')

spotify = spotipy.Spotify(auth=token)

#------------------1st example-----------------------
birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
results = spotify.artist_albums(birdy_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])

#------------------2nd example-----------------------
'''
print('---------------------------------------')
lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'
results = spotify.artist_top_tracks(lz_uri)

for track in results['tracks'][:10]:
    print ('track    : ' + track['name'])
    print ('audio    : ' + track['preview_url'])
    print ('cover art: ' + track['album']['images'][0]['url'])
    print
'''

print('---------------------------------------')
print(spotify.search('On a boat', limit=10, offset=0, type='track'))