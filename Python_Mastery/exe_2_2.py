# Excercise 2.2
import readrides as rr_mod
import collections
import tracemalloc

tracemalloc.start()
file = "Python_Mastery/Data/ctabus.csv"
row_type = rr_mod.slot_row("", "", "", "")
rows = rr_mod.read_rides(file, row_type)
bus_route = set()
ppl_route22_20110202 = 0
bus_ride = collections.Counter()
ride_by_year = collections.defaultdict(collections.Counter)

for row in rows:
    bus_route.add(row.route)

    if row.route == '22' and row.date == "02/02/2011":
        ppl_route22_20110202 += row.rides
    
    bus_ride[row.route] += row.rides

    year = row.date.split("/")[2]
    ride_by_year[year][row.route] += row.rides 

diff_2011_2001 = ride_by_year["2011"] - ride_by_year["2001"]

print(f"Bus#: {len(bus_route)}")
print(f"""How many people rode the number 22 bus on February 2, 2011:
{ppl_route22_20110202}""")
print(f"What is the total number of rides taken on each bus route: {bus_ride}")
print(f"""What five bus routes had the greatest ten-year increase in ridership from 2001 to 2011: 
       {diff_2011_2001.most_common(5)}""")
