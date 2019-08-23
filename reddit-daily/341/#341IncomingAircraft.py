#[2017-11-22] Challenge #341 [Intermediate] Listening for Incoming Aircraft
#needs to account for tangent at angle%90=0
import math



def incoming_aircraft():
    station_1 = [0,0,0]
    station_1[0] = float(input("Station 1 x: "))
    station_1[1] = float(input("Station 1 y: "))
    station_1[2] = float(input("Station 1 angle from x: "))

    station_2 = [0,0,0]
    station_2[0] = float(input("Station 2 x: "))
    station_2[1] = float(input("Station 2 y: "))
    station_2[2] = float(input("Station 2 angle from x: "))

    #aX+b=cX+d
    a = math.tan(math.radians(90 - station_1[2]))
    b = station_1[1] - a * station_1[0]
    c = math.tan(math.radians(90 - station_2[2]))
    d = station_2[1] - c * station_2[0]

    aircraft_x = round(-(b-d)/(a-c),2)
    aircraft_y = round(a * aircraft_x + b,2)
    return aircraft_x,aircraft_y


aircraft_coords = [0,0]
aircraft_coords = incoming_aircraft()
print("aircraft at coordinates: {},{}".format(aircraft_coords[0],aircraft_coords[1]))



