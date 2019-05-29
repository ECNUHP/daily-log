


from rouge import Rouge
rouge = Rouge()
result=['我 是 谁 ， 这是 在 哪里 呢 ？','希望 你是 一个 好 孩子 。']
gold=['我 喜欢 你 ， 在 哪里 ？','明天 会 更好 的 ，小 孩子 。']
rouge_score = rouge.get_scores(result, gold)
print(rouge_score[0]["rouge-1"])
print(rouge_score[0]["rouge-2"])
print(rouge_score[0]["rouge-l"])
#result
# {'f': 0.6249999950781252, 'p': 0.5555555555555556, 'r': 0.7142857142857143}
# {'f': 0.14285713795918387, 'p': 0.125, 'r': 0.16666666666666666}
# {'f': 0.6063432835814155, 'p': 0.5555555555555556, 'r': 0.7142857142857143}