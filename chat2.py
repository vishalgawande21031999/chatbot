from nltk.chat.util import Chat, reflections
a=input("enter your name:")
b=input("enter your bot name:")
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
[
        r"who created you ?",
        ["I was created by ishal",]
    ],


     [
        r"what is your name ?",
        ["My name is "+b+" and I'm a chatbot ?",]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about You ?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","Alright :)",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program dude\nSeriously you are asking me this?",]
        
    ],


    [
        r"(.*) fuck (.*)",
        ["mind your tongue please",]
        
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
        
    ],
    [
        r"(.*) created ?",
        ["Nagesh created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Chennai, Tamil Nadu',]
    ],
    [
        r"how is weather in (.*)?",
        ["https://www.google.com/search?q=weather+in+aurangabad&oq=weather+in+aurangabad&aqs=chrome..69i57j0l7.6018j1j4&sourceid=chrome&ie=UTF-8"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.",]
    ],
[
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2","Damn its raining too much here in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Football",]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Messy","Ronaldo","Roony"]
],

    [
        r"quit",
        ["BBye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
],
]
def chatty():
	print("Hi,"+ a +" I'm "+b+ " at your service ")
	chat = Chat(pairs, reflections)
	chat.converse()
if __name__ == "__main__":
	chatty()