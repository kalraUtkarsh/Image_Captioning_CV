import pandas as pd

file = '/content/Flickr8k.token.txt'
f = open(file)

lines = f.readlines()
main_df = pd.DataFrame()

for line in lines:
    sent = "Startseq "
    word, sentence = line.split("\t")
    pic, index = word.split('#')
    clean_sentence = sentence.replace("[^a-zA-Z0-9]"," ")
    sent += clean_sentence[:-3]
    sent += " Endseq"
    df = pd.DataFrame([[pic,sent]], columns = ['image','description'])
    if main_df.empty:
        main_df = df
    else:
        main_df = pd.concat([main_df, df])

main_df.to_csv('sentences.csv',index=False)
