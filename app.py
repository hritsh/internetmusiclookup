import mechanicalsoup

class review:
    def __init__(self, source, score, url, artist, album):
        self.source = source
        self.score = score
        self.url = url
        self.artist = artist
        self.album = album
    
    def __str__(self):
        return self.source + ": " + self.score + "/10" + " - " + self.url

def getPitchfork(artist, album):
    pitchfork = review('Pitchfork', 0, '', artist, album)
    browser.open("https://www.pitchfork.com/search/?query=" + artist + " " + album)

    for link in browser.get_current_page().find_all('a'):
        if link.has_attr('class') and 'review__link' in link.attrs['class']:
            pitchfork.url = browser.absolute_url(link.attrs['href'])
            browser.open(pitchfork.url)
            # Rating is in a p with class Rating-iATjmx
            score = browser.get_current_page().find_all('p')
            for p in score:
                if p.has_attr('class') and 'Rating-iATjmx' in p.attrs['class']:
                    pitchfork.score = p.text
                    break
            break
    return pitchfork

browser = mechanicalsoup.StatefulBrowser()

artist = 'kanye west'
album = 'yeezus'

pitchfork = getPitchfork(artist, album)
print(pitchfork)





    