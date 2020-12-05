# wk10ex3.py
#
# Naam: Sander Kroeze
#

import random
# functie #1
#
def create_dictionary (fileName) :
    d = {}
    f = open(fileName)
    text = f.read()
    f.close()
    
    LoW = text.split()
    isStart = True
    for i in range(len(LoW)) :
        
        if isStart :
            d.setdefault("$", []).append(LoW[i])
        else :
            d.setdefault(LoW[i - 1], []).append(LoW[i])
        last = LoW[i][-1]
        if last == '.' or last == '!' or last == '?' :
            isStart = True
        else :
            isStart = False
    return d 


# functie #2
#
def generate_text(d, n):
    res = ""
    curr = "$"
    for i in range(n) :
        curr = random.choice(d[curr])
        res += " " + curr
        last = curr[-1]
        if last == '.' or last == '!' or last == '?' :
            curr = "$"
    return res[1:]


#
# Je gegenereerde essay van ongeveer 500 woorden (plak in de onderstaande triple-quoted strings):
#
"""
This image that these Lucasfilm faithful relentlessly call the New promise but everyone else calls Star Wars fell out in 1977. It and its sequels (and television films and sketches and toys and bedsheets) burrowed deeply into common culture. And if those people in the Walt Disney corporation, which purchased Lucasfilm for $ 4 billion at 2012, have thing to tell about it, this last four decades of Star Wars were merely prologue. They represent getting more. A deal more. The company intends to lay out The new Star Wars film each year for as long as people can get tickets. Make me guess it another choice: If everything turns out for Disney, and if you exist (like me) older enough to get been aware for those early character Wars film, you will probably not live to see the last one. It’s that forever business.

If it sounds like I'm bagging on Jon Ossoff's candidacy, I'm not. Ossoff's a young, ambitious guy who's got a long political future ahead of him, and I'd rather have him in the House than another Republican. Plus, he's a huge Star Wars fan , which is a plus in my book. But if the Democratic establishment is trying to prove a point that their "trade a blue-collar vote for a moderate Republican" by backing his candidacy and ignoring the progressive, Sanders-inspired campaigns of James Thompson and Rob Quist, let me say that all three deserve attention from Democratic leadership if they plan on retaking the government sooner or later.

Character Wars period, May 4, celebrates George Lucas' character Wars. It is respected by fans of this media business. Observance of this commemorative time moved rapidly through media and grassroots celebrations.  (painter , Alicia grey, May 4, 2009)   (my fur Chattanooga. May 4, 2010.) 

While the hovercars and speeders found in Star Wars might not be seen anytime soon, we do have some exciting new possibilities on the horizon. Take, for example, the self-driving cars made by Singapore-based company  Nutonomy . Their vehicles whiz around the streets using complex software programs to detect if there are people, animals, or other cars in their way, and so far, have been seeing great success.

Find a few movies that match the genre you want to write, but not movies you're familiar with. Instead of Star Trek or Star Wars, think Lord of the Rings or Mass Effect. About that last one — computer game soundtracks are excellent instrumental background music, especially if you're writing action scenes. If you're not a hard core gamer, you're less likely to be distracted by the familiar.

Bond told her ARL's event included activities that involved Star Wars storm troopers, robots and virtual reality exhibits. And despite the hundreds of similar events that she helps coordinate each year, it was her conversation with Bond that promoted her to ask for a special invitation to attend the event in Adelphi.

When the world's social media giants meet to discuss the most interesting jobs available online, creating fake accounts is not on the list. Fake social media profiles are the cannon-fodder of the propaganda wars. Automated and regimented, fake profiles can be deployed in tens of thousands within minutes and taken down almost as quickly.

Source: EssayBot.com


"""
#
#