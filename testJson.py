import json


def writerex(f1,str1):
    with open(f1,'w',encoding='utf-8') as f:
        f.write(str1)

def readrex(f1):
    with open(f1,'r',encoding='utf-8') as f:
        rex =json.loads(f.read())
    return rex
def main():
    # str1 = json.dumps([(r'\d+\.\d+(e(\+|\-)\d+)?', r'x'),
    #                           (r'([A-Fa-f0-9]{2}\:){3}[A-Fa-f0-9]\:([A-Fa-f0-9]{2}\:)([A-Fa-f0-9]{2})',
    #                            r'[MAC_XX]'), (r'\]\d+', r']x'), (r'\:\d+', r':x'), (r'\s\d+', r' x'),
    #                           (r'PA\d+\-\d', r'PAxxxx'), (r'\d+', r'[n]')])
    # print(type(str1))
    # writerex(r'data_test',str1)
    ls = readrex(r'data_test2')
    print(type(ls))
    print(ls)
    # for ele in ls:
    #     print(ele)
main()
