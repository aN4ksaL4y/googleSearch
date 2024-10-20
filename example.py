from ini_google_search import search


# this is an example of search with 30 results
r = search('does sob rock better than continuum?', num_results=30, advanced=True)

print ( [v.title for v in r] )

"""
# output
['Sob Rock is my favorite John Mayer album. I like it more ...', 'Ranking Every John Mayer Album - Nitin Bharadwaj - Medium', 'John Mayer Sob Rock', 'John Mayer - Sob Rock', 'Review of Continuum by bunger', 'Amazon.sg:Customer reviews: Heavier Things', 'John Mayer Sob Rock | Page 22', 'Heavier Things', 'John Mayer - Continuum (album review 2)', 'John Mayer', 'Review: John Mayer, Continuum', 'Continuum - Album by John Mayer', 'John Mayer - Beard Blog', "John Mayer Gear | The legendary 'Continuum' album ...", 'John Mayer – Continuum +1 - (Vinyl Record)', 'John Mayer', 'John Mayer - Sob Rock. July 16.', "Album Review: John Mayer – 'Sob Rock'", 'John Mayer - Continuum - Music & Performance - Vinyl', 'John Mayer - Continuum', 'Continuum: Amazon.com.be: CDs & Vinyl', 'John Mayer Brings SOB Rock To Tampa', "John Mayer's Continuum Vocal Chain", 'John Mayer Album', 'Continuum - John Mayer (Vinyl) – Swee Lee Singapore', 'John Mayer - Sob Rock. July 16.', "John Mayer SIGNED 'Sob Rock' Vinyl Album Autograph ...", 'John Mayer: Sob Rock and a Pink Silver Sky - Page 3', 'John Mayer – Sob Rock - (Vinyl Record)', 'Continuum - Album by John Mayer']
"""