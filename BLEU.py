
# Copyright 2017 Google Inc. All Rights Reserved.

#

# Licensed under the Apache License, Version 2.0 (the "License");

# you may not use this file except in compliance with the License.

# You may obtain a copy of the License at

#

#     http://www.apache.org/licenses/LICENSE-2.0

#

# Unless required by applicable law or agreed to in writing, software

# distributed under the License is distributed on an "AS IS" BASIS,

# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

# See the License for the specific language governing permissions and

# limitations under the License.

# ==============================================================================



"""Python implementation of BLEU and smooth-BLEU.



This module provides a Python implementation of BLEU and smooth-BLEU.

Smooth BLEU is computed following the method outlined in the paper:

Chin-Yew Lin, Franz Josef Och. ORANGE: a method for evaluating automatic

evaluation metrics for machine translation. COLING 2004.

"""



import collections

import math

def _get_ngrams(segment, max_order):

  """Extracts all n-grams upto a given maximum order from an input segment.



  Args:

    segment: text segment from which n-grams will be extracted.

    max_order: maximum length in tokens of the n-grams returned by this

        methods.
  Returns:
    The Counter containing all n-grams upto max_order in segment
    with a count of how many times each n-gram occurred.

  """

  ngram_counts = collections.Counter()

  for order in range(1, max_order + 1):

    for i in range(0, len(segment) - order + 1):

      ngram = tuple(segment[i:i+order])

      ngram_counts[ngram] += 1

  return ngram_counts





def compute_bleu(reference_corpus, translation_corpus, max_order=4,

                 smooth=False):

  """Computes BLEU score of translated segments against one or more references.
  Args:

    reference_corpus: list of lists of references for each translation. Each

        reference should be tokenized into a list of tokens.

    translation_corpus: list of translations to score. Each translation

        should be tokenized into a list of tokens.

    max_order: Maximum n-gram order to use when computing BLEU score.

    smooth: Whether or not to apply Lin et al. 2004 smoothing.

  Returns:

    3-Tuple with the BLEU score, n-gram precisions, geometric mean of n-gram

    precisions and brevity penalty.

  """

  matches_by_order = [0] * max_order
  possible_matches_by_order = [0] * max_order
  reference_length = 0
  translation_length = 0

  for (references, translation) in zip(reference_corpus,

                                       translation_corpus):

    reference_length += min(len(r) for r in references)
    translation_length += len(translation)
    merged_ref_ngram_counts = collections.Counter()
    for reference in references:

      merged_ref_ngram_counts |= _get_ngrams(reference, max_order)


    translation_ngram_counts = _get_ngrams(translation, max_order)

    overlap = translation_ngram_counts & merged_ref_ngram_counts

    for ngram in overlap:

      matches_by_order[len(ngram)-1] += overlap[ngram]

    for order in range(1, max_order+1):

      possible_matches = len(translation) - order + 1

      if possible_matches > 0:

        possible_matches_by_order[order-1] += possible_matches



  precisions = [0] * max_order

  for i in range(0, max_order):

    if smooth:

      precisions[i] = ((matches_by_order[i] + 1.) /

                       (possible_matches_by_order[i] + 1.))

    else:

      if possible_matches_by_order[i] > 0:

        precisions[i] = (float(matches_by_order[i]) /

                         possible_matches_by_order[i])

      else:

        precisions[i] = 0.0



  if min(precisions) > 0:

    p_log_sum = sum((1. / max_order) * math.log(p) for p in precisions)

    geo_mean = math.exp(p_log_sum)

  else:

    geo_mean = 0
  ratio = float(translation_length) / reference_length
  if ratio > 1.0:

    bp = 1.

  else:

    bp = math.exp(1 - 1. / ratio)
  bleu = geo_mean * bp
  return (bleu, precisions, bp, ratio, translation_length, reference_length)


import jieba

def get_candidate_reference(path):

  reference = []
  null = []
  like = []
  disgust = []
  sad = []
  happy = []
  angry = []
  with open(path, 'r', encoding='utf-8')as infile:
    lines = infile.readlines()
    newlines = []
    for line in lines:
      line = line.strip()
      if line:
        newlines.append(line)
    for index, line in enumerate(newlines):
      if index % 7 == 0:
        line = line.split('\t')[3]
        #line = ' '.join(jieba.cut(line))
        line=[word for word in jieba.cut(line)]
        reference.append(line)
      elif index % 7 == 1:
        line = line.split('\t')[1]
        #line = ' '.join(jieba.cut(line))
        line = [word for word in jieba.cut(line)]
        null.append(line)
      elif index % 7 == 2:
        line = line.split('\t')[1]
        line = [word for word in jieba.cut(line)]
        like.append(line)
      elif index % 7 == 3:
        line = line.split('\t')[1]
        line = [word for word in jieba.cut(line)]
        sad.append(line)
      elif index % 7 == 4:
        line = line.split('\t')[1]
        line = [word for word in jieba.cut(line)]
        disgust.append(line)
      elif index % 7 == 5:
        line = line.split('\t')[1]
        line = [word for word in jieba.cut(line)]
        angry.append(line)
      elif index % 7 == 6:
        line = line.split('\t')[1]
        line = [word for word in jieba.cut(line)]
        happy.append(line)

  return reference, null, like, angry, happy, disgust, sad




if __name__ == "__main__":
  path = r'C:\Users\hp\Desktop\ECM_test_result.txt'
  reference, null, like, angry, happy, disgust, sad = get_candidate_reference(path)
  references=[]
  for r in reference:
    temp=[]
    temp.append(r)
    references.append(temp)

  sum_bleu=0
  bleu, precisions, bp, ratio, translation_length, reference_length=compute_bleu(references, null, max_order=3,smooth=True)
  sum_bleu+=bleu
  print('null:{}'.format(round(bleu,5)))
  bleu, precisions, bp, ratio, translation_length, reference_length=compute_bleu(references, like, max_order=3,smooth=True)
  sum_bleu += bleu
  print('like:{}'.format(round(bleu,5)))
  bleu, precisions, bp, ratio, translation_length, reference_length=compute_bleu(references, angry, max_order=3,smooth=True)
  sum_bleu += bleu
  print('angry:{}'.format(round(bleu,5)))
  bleu, precisions, bp, ratio, translation_length, reference_length=compute_bleu(references, happy, max_order=3,smooth=True)
  sum_bleu += bleu
  print('happy:{}'.format(round(bleu,5)))
  bleu, precisions, bp, ratio, translation_length, reference_length=compute_bleu(references, disgust, max_order=3,smooth=True)
  sum_bleu += bleu
  print('disgust:{}'.format(round(bleu,5)))
  bleu, precisions, bp, ratio, translation_length, reference_length=compute_bleu(references, sad, max_order=3,smooth=True)
  sum_bleu += bleu
  print('sad:{}'.format(round(bleu,5)))

  print('average:{}'.format(round(sum_bleu/6,5)))

  # null=[['你', '说', '的', '是', '，', '是不是'], ['你', '是', '小朋友', '，', '你', '是', '小孩子']]
  #
  # reference=[[['我', '不', '这样', '认为', '。']],[['真相', '往往', '是', '出乎意料', '的', '。']]]
  #
  # bleu, precisions, bp, ratio, translation_length, reference_length = compute_bleu(reference, null, max_order=4,
  #                                                                                  smooth=True)
  #
  #
  # null=[['你', '说', '的', '是', '，', '是不是'], ['你', '是', '小朋友', '，', '你', '是', '小孩子']]
  #
  # reference=[['我', '不', '这样', '认为', '。'],['真相', '往往', '是', '出乎意料', '的', '。']]
  #
  # bleu, precisions, bp, ratio, translation_length, reference_length = compute_bleu(reference, null, max_order=4,
  #                                                                                  smooth=True)
