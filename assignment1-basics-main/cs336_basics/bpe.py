# #  Problem(train_bpe):BPETokenizerTraining

# def train_bpe(input_path:str, vocab_size:int,special_tokens:list[str]):
#     # vocab must be dict int and type {id ,token}
#     # merge must be merges done 
#     # split sentment into character
#     # for i in range of vocab_size-1
#     # merge first two character the take the most one occur 
#     #add merge.append(most occur one)
#     # add the id"Number" of the vocab 
#     with open(input_path, "r", encoding="utf-8") as f:
#         content = f.read()  # reads the entire file as a string
#         # Split each character into a list
#         char_list = list(content)
#         character_merge=[char_list[i],char_list[i+1] for i in range (len(vocab_size)-1)]
        
    

#     return vocab,merges


from collections import Counter

# Split each character into a list
vocab_size=3
content="hello word hel"
char_list = list(content)
character_merge=[char_list[i]+char_list[i+1] for i in range (len(char_list)-1)]
print(character_merge)
count_occurance=Counter(character_merge)
print ("**********************************************************************************************")
print(count_occurance.most_common(1)[0])
