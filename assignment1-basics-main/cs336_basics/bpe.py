# #  Problem(train_bpe):BPETokenizerTraining
from collections import Counter 
# def train_bpe(input_path:str, vocab_size:int,special_tokens:list[str]):
    # vocab must be dict int and type {id ,token}
    # merge must be merges done 
    # split sentment into character
    # for i in range of vocab_size-1
    # merge first two character the take the most one occur 
    #add merge.append(most occur one)
    # add the id"Number" of the vocab 
with open("test.txt", "rb") as f:
    file_bytes  = f.read()  # reads the entire file as a string
# print("list file bytes",list(file_bytes))
    # Split each character into a list
special_tokens = ["<pad>", "<eos>"]
# char_list = list(content)
# character_merge=[char_list[i],char_list[i+1] for i in range (len(vocab_size)-1)]

#add 256 character as  as a token 
vocab = {i: bytes([i]) for i in range(256)}
# print("first_vocab",vocab)


#special token stay as str not converted into a bytes
#add special token into the 256 character 
for token in special_tokens:
    vocab[len(vocab)]=token
# print("after add special token_vocab",vocab)
# print ("*******************************************************")
# print(len(vocab))
# print("**********************************************************************")

#convert the text from byes to byte list     
file_bytes_list=list(file_bytes)
# print("convert file into a list of characters",file_bytes_list)
merges=[]
vocab_size=2
while len(vocab) <vocab_size :
    pairs=[(file_bytes_list[i],file_bytes_list[i+1]) for i in range (len(file_bytes_list)-1)]
    pairs_freqs=Counter(pairs)
    most_freq_pair=pairs_freqs.most_common(1)[0][0]
    # print("most_freq_pair",most_freq_pair)
    #add new token 
    new_token=bytes(most_freq_pair)
    new_token_id=len(vocab)
    vocab[new_token_id]=new_token
    merges.append(most_freq_pair)

    #replace all the occurance of the new token with its id 
    i=0
    new_file_bytes_list=[]
    while i <len(file_bytes_list):
        if i< len(file_bytes_list)-1 and ((file_bytes_list[i],file_bytes_list[i+1]))==most_freq_pair:
              new_file_bytes_list.apend(new_token_id)  
              i+=2
        else:
            file_bytes_list.append(file_bytes_list[i])
            i+=1 
    file_bytes_list=new_file_bytes_list
    
  
print(merges)
print("**************************************")
print(vocab)






        
    

    # return vocab,merges


# from collections import Counter

# # Split each character into a list
# vocab_size=3
# content="hello word hel"
# char_list = list(content)
# character_merge=[char_list[i]+char_list[i+1] for i in range (len(char_list)-1)]
# print(character_merge)
# count_occurance=Counter(character_merge)
# print ("**********************************************************************************************")
# print(count_occurance.most_common(1)[0])
