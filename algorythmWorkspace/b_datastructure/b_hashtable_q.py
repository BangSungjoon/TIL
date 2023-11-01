# 문자열에서 가장 많이 반복되는 문자 찾기
# 주어진 문자열에서 가장 많이 반복되는 문자를 찾아
# 배열에 담아 반환하는 함수를 작성하시오.

# hint : 반복하는 알파벳 
from b_hashtable import HashTable

def q1(text:str):
    hashtable = HashTable()
    
    for ch in text:
        if ch not in hashtable:
            hashtable.add(ch,1)
        else:
            hashtable.set(ch, hashtable.get(ch)+1)
    
    res = []
    max = 1
    
    for e in hashtable:
        if max < e.data : max = e.data
    
    for e in hashtable:
        if max == e.data : res.append(e.key)    
    
    return res