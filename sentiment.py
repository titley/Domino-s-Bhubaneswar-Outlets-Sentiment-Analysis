from textblob import TextBlob
text= "I’ve been using Mamaearth products consistently for over a year now, and I feel like I finally have enough experience to share a well-rounded review. First off, I love the brand’s commitment to being toxin-free and cruelty-free. The fact that their products are made with natural ingredients and are dermatologically tested really gives me peace of mind, especially since I have sensitive skin. One of the first products I tried was the Mamaearth Onion Hair Oil, and I was genuinely impressed. It helped reduce my hair fall over a period of 2–3 months and made my hair feel much smoother. I paired it with their Onion Shampoo and Conditioner, and I could see a noticeable improvement in my hair texture. However, I do feel the shampoo can be a bit drying for some hair types if not followed up with a proper conditioner."
Blobinput =TextBlob (text)
print (text)
print ("sentiment polarity", Blobinput.sentiment.polarity)
print ("\n sentiment subjectivity", Blobinput.sentiment.subjectivity)
if Blobinput.sentiment.polarity>0:
    print ("this is positive")
elif Blobinput.sentiment.polarity<0:
    print ("this is negative")
else:
    print ("this is neutral")