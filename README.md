# &#127926; Scrape lyrics of any English song on google! &#127926;


<h3>Run: </h3>

```
git clone https://github.com/ayanatherate/lyricscraper.git
cd lyricscraper 
pip install -r requirements.txt
```

<br>
<h3>Open any Python IDE/Notebook: </h3>

```
from lyricscraper import get_lyrics 
lyrics=get_lyrics.ask_inp('metallica enter sandman') 
#please enter name of song along with artist name, space separated
```

<h3> Future Scopes</h3>
Future plans will oviously be to add multilingual song lyrics scraping ability.<br>
But in my research, it's difficult to establish a pattern (in the url search) <br>
that would be directed to the web driver. Lyrics of Bangla songs or even Hindi <br>
songs aren't as well documented as I had expected them to be and there is no such <br>
have-it-all resource on the internet where I can blisfully direct my driver to, to <br>
scrape any song possible. However,in my attempt to make this a full-proof project from <br>
my side, I'll try my best to make this library as generalized as possible.


