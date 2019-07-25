import pandas as pd
import json, os

data = pd.read_csv("11w_mian.csv")


min_count = 32
maxlen = 4000
batch_size = 64
epochs = 100
char_size = 128
z_dim = 128
c = []

# for each in data['content_list']:
#     for a in str(each):
#         c.append(a)
#
# dic = {'key':c}
#
# kf = pd.DataFrame(dic)
#
# hh = kf.drop_duplicates()
#
# hh.reset_index()




chars = {}
for index,a in data.iterrows():
    for w in str(a['content_list']): # 纯文本，不用分词
        chars[w] = chars.get(w,0) + 1
    for w in str(a['tittle']): # 纯文本，不用分词
        chars[w] = chars.get(w,0) + 1
chars = {i:j for i,j in chars.items() if j >= min_count}
# 0: mask
# 1: unk
# 2: start
# 3: end
id2char = {i+4:j for i,j in enumerate(chars)}
char2id = {j:i for i,j in id2char.items()}
json.dump([chars,id2char,char2id], open('seq2seq_config.json', 'w'))


for index, a in data.iterrows():
    print(a)