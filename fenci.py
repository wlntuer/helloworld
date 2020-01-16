import jieba
sent = '这里可以写一句汉语，就会分词。'
seg_list = jieba.cut(sent, cut_all=False)
print('/'.join(seg_list))
