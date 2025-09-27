"""
la suite de fibonacci
"""

def fibo_cached(n):
    """
    # une implémentation naïve et inefficace
    """
    dico={}
    if n in dico:
        return n
    if n <= 1:
            res=n
    else:
        res= fibo_cached(n-1) + fibo_cached(n-2)
    dico[n]=res
    return res    
