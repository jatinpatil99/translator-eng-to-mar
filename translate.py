from textblob import TextBlob

def transinput(send):
    text=TextBlob(send)
    op=text.translate(from_lang='en', to='mr')
    return op