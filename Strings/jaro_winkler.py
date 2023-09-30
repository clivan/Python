def jaro_winkler(str1: str, str2: str)-> float:
    def get_matched_characters(_str1: str, _str2: str)->str:
        matched=[]
        limit=min(len(_str1), len(_str2))
        for i, l in enumerate(_str1):
            left=int(max(0, i-limit))
            right=int(min(i+limit+1, len(_str2)))
            if l in _str2[left:right]:
                matched.append(l)
                _str=f"{_str2[0:_str2.index(l)]} {_str2[_str2.index(l)+1:]}"
        return "".join(matched)
    
    matching_1=get_matched_characters(str1, str2)
    matching_2=get_matched_characters(str1, str2)
    match_count=len(matching_1)
    transpositions=(len([(c1, c2) for c1, c2 in zip(matching_1, matching_2) if c1!=c2]))
    if not match_count:
        jaro=0.0
    else: 
        jaro=(1/3*(match_count/len(str1)+match_count/len(str2)+(match_count-transpositions)/match_count))
    
    prefix_len=0
    for c1, c2 in zip(str1[:4], str2[:4]):
        if c1==c2:
            prefix_len+=1
        else:
            break
        return jaro+0.1*prefix_len*(1-jaro)
    if __name__=="__main__":
        import doctest
        doctest.testmod()
        print(jaro_winkler("Hello", "world"))
                    
    