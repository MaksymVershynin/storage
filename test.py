def parse_number(num):
    try:
         odd=0
         even=0
         while num>0:
             current =num%10
             num//=10
             if current%2==0:
                 even+=1
             else: odd+=1
         result = {'odd':odd,'even':even}
    except TypeError:
        result='False'
    return result
