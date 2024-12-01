from pprint import pprint


def read_file():
    almanac={}
    with open("5_input.txt") as f:
        while True:
            line=f.readline()
            if line == "":
                break
            if "seeds:" in line:
                almanac["seeds"]=[int(n) for n in line[line.find(':')+1:].strip().split()]
            elif "to" in line:
                source=line[:line.find('-')]
                dest=line[line.rfind('-')+1:-6]
                # print(source, dest)
                list_of_ranges=[]
                while True:
                    ranges=f.readline().strip('\n')
                    if ranges == "":
                        # print("ranges read done")
                        break
                    else:
                        # print(ranges)
                        ranges=ranges.split(' ')
                        list_of_ranges.append({
                            'dest_start': int(ranges[0]),
                            'source_start': int(ranges[1]),
                            'range_length': int(ranges[2])
                        })
                        almanac[source]={dest: list_of_ranges}


    # pprint(almanac)
    return almanac

def part_one(almanac):
    min_location=-1

    for seed in almanac["seeds"]:
        in_value=seed
        source="seed"

        while True:
            dest=list(almanac[source].keys())[0]
            # print(source, "\t", in_value, "->", end='')
            out_value=-1
            for this_range in almanac[source][dest]:
                if in_value >= this_range["source_start"] and in_value < this_range["source_start"]+this_range["range_length"]:
                    # print(this_range)
                    out_value=this_range["dest_start"]+(in_value-this_range["source_start"])
            if out_value == -1:
                out_value=in_value
            # print("\t", out_value, "\t", dest)

            in_value=out_value
            source=dest
            if dest=="location":
                # print("\t\t\t\tis location")
                if min_location==-1 or out_value<min_location:
                    min_location=out_value
                break

    return min_location

### use: ?
# from itertools import chain
# y_iter = chain(l1, l2)

def part_two(almanac):
    min_location=-1
    # print("original seeds len:", len(almanac["seeds"]))
    n=2
    couples=[almanac["seeds"][i * n:(i + 1) * n] for i in range((len(almanac["seeds"]) + n - 1) // n )]
    print(couples)
    # new_seeds=[]
    for couple in couples:
        print("this couple:", couple)
        seeds_to_add=list(range(couple[0], couple[0]+couple[1]))
        almanac["seeds"]=seeds_to_add
        new_min=part_one(almanac)
        print("new_min?", new_min)
        if min_location==-1 or new_min<min_location:
            min_location=new_min
        # new_seeds+=seeds_to_add
    # new_seeds=list(set(new_seeds))

    # print("final seeds len", len(new_seeds))
    # almanac["seeds"]=new_seeds

    return min_location

if __name__ == "__main__":
    almanac=read_file()
    # pprint(cards)
    res=part_one(almanac)
    res=part_two(almanac)
    print(res)