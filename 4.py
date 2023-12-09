from pprint import pprint


def read_file():
    cards={}
    with open("4_input.txt") as f:
        for line in f.readlines():
            colon_i=line.find(':')
            pipe_i=line.find('|')
            card_n=int(line[:colon_i].split()[-1])
            winning_numbers=line[colon_i+1:pipe_i].strip().split()
            my_numbers=line[pipe_i+1:].rstrip('\n').strip().split()
            # print(winning_numbers)
            # print(my_numbers)
            my_winners=[n for n in my_numbers if n in winning_numbers]
            # print(my_winners)
            cards[card_n]= {
                'winning_numbers': winning_numbers,
                'my_numbers': my_numbers,
                'my_winners': my_winners
            }
    return cards

def part_one(cards):
    sum=0
    for card_n, card_res in cards.items():
        # print(card_n, card_res)
        if len(card_res['my_winners']) >= 1:
                # print(len(card_res['my_winners']))
                sum+=2**(len(card_res['my_winners'])-1)

    return sum

def part_two(cards):
    sum=0
    for card_n in cards.keys():
        cards[card_n]["how_many"]=1;

    for card_n in cards.keys():
        for i in range(1, len(cards[card_n]['my_winners'])+1):
            if card_n+i<=len(cards.keys()):
                cards[card_n+i]["how_many"]+=1*cards[card_n]["how_many"]
                # print('('+str(len(cards[card_n]['my_winners']))+' winners)', "card_n+i->", card_n+i)
        # print("card_n->",card_n, "winners->",len(cards[card_n]['my_winners']), "how many->", cards[card_n]["how_many"])

    for card_n in cards.keys():
        sum+=cards[card_n]["how_many"]
    return sum

if __name__ == "__main__":
    cards=read_file()
    # pprint(cards)
    sum=part_one(cards)
    sum=part_two(cards)
    print(sum)