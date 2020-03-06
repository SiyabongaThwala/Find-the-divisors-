def people_in_the_bus(bus_stops):
    people_getting_in = 0
    people_getting_out = 0
    people_left = 0
    
    for item in bus_stops:
        people_getting_in += item[0]

    for item in bus_stops:
        people_getting_out += item[1]

    people_left = people_getting_in - people_getting_out
    print(people_left)

people_in_the_bus([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]])    


