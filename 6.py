from pprint import pprint


def read_file():
    with open("6_input.txt") as f:
        times=f.readline().split()[1:]
        space_records=f.readline().split()[1:]

    races=[]
    for i in range(len(times)):
        races.append({
            'time':int(times[i]),
            'space_record':int(space_records[i])
        })
    pprint(races)
    return races

def part_one(races):
    res=1
    count_wins=0
    for race in races:
        print(race)
        for press_time in range(1, race['time']):
            final_space=(race['time']-press_time)*press_time
            # print("press_time:", press_time, "final_space", final_space)
            if final_space>race['space_record']:
                count_wins+=1
        if count_wins>0:
            res*=count_wins
            count_wins=0
    return res


def part_two(races):
    time=''
    space_record=''
    for race in races:
        time+=str(race['time'])
        space_record+=str(race['space_record'])

    races=[{
        'time':int(time),
        'space_record':int(space_record)
    }]
    return part_one(races)

if __name__ == "__main__":
    races=read_file()
    # res=part_one(races)
    res=part_two(races)
    print(res)