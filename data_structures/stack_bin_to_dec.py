from stack_implementation import Stack

def dec_to_bin(dec_num):
    rs = Stack()
    while dec_num>0:
        r = dec_num%2
        rs.push(r)
        dec_num = dec_num//2
        
    return_str = ""
    while not rs.isEmpty():
        return_str = return_str + str(rs.pop())
        
    return return_str

def dec_to_other_base(dec_num, base):
    digits = "0123456789ABCDEF"
    rs = Stack()
    while dec_num>0:
        r = dec_num%base
        rs.push(r)
        dec_num = dec_num//base
        
    return_str = ""
    while not rs.isEmpty():
        return_str = return_str + digits[rs.pop()]
        
    return return_str



#print(dec_to_bin(233))

#print(dec_to_other_base(255,16))