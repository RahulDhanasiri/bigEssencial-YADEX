import sys

current_key = None
word_total = 0
word_set   = set()

for line in sys.stdin:
    try:
        sorted_word, word, count = line.strip().split('\t', 2)
        count = int(count)
    
        if current_key != sorted_word:
            if current_key:
                print("{}\t{} {}\t{}".format(word_total, current_key, len(word_set), ",".join(sorted(word_set))))
                
            current_key = sorted_word
            word_set = set()
            word_total = 0
        
        word_total += count
        word_set.add(word)
        
    except ValueError as e:
        print(e)
        continue    

if current_key:
    print("{}\t{} {}\t{}".format(word_total, current_key, len(word_set), ",".join(sorted(word_set))))