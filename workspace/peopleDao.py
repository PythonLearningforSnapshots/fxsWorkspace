'''

'''
import random


def simulator(persons = 100, loops = 100):
    p_list = [ 100 for i in range(persons) ]
    section = int(loops/10)+1
    for i in range(loops):
        if i > section:
            sort_ls(p_list)
            section += int(loops/10)+1
        for j in range(persons):
            r = random.randint(0,persons-1)
            if p_list[j] > 0:
                p_list[r]+=1
                p_list[j]-=1

    sort_ls(p_list)
    plot_game(p_list)
    return p_list


def sort_ls(ls):
    assert type(ls) is list
    for ele in ls:
        print('%-4d'%ele,end='| ')
    print('\n')
    return    

def plot_game(ls):
    assert type(ls) is list
    
    return


def main():
    persons = 100
    loops = 100
    while True:
        persons = int(input('How many people(>=2):'))
        loops = int(input('Run the game times(>0):'))
        if persons < 2:
            print('too less people')
            continue
        if loops < 1:
            break
        simulator(persons,loops)
        select = input('(c)Continue or (e)Exit:')
        if select is 'c':
            continue
        else:
            break
    return


main()
