def score_letter(letter, position, true_word)
    #for example, score_letter('A', 1, 'ABBA') should be correct position
    if(true_word[position] == letter):
       return '*' # for correct position
    if(letter in ture_word):
       return 'o' # for correct letter, incorrect position
    else:
       return '-'
