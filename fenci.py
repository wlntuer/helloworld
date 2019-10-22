import jieba
sent='中原银行是河南省区域内第一家成立的省级法人银行，当前正在进行敏捷转型，从年初到年尾都风风火火的，明年还会继续转型。'
seg_list =jieba.cut(sent,cut_all=False)
print('/'.join(seg_list))