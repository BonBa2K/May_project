from datetime import date
d = date.today() # 730920th day after 1. 1. 0001
print("d == ")
print(d)

# Methods related to formatting string output
print("d.isoformat()")
print(d.isoformat())
print("d.strftime(\"%d/%m/%y\")")
print(d.strftime("%d/%m/%y"))
print("d.strftime(\"%A %d. %B %Y\")")
print(d.strftime("%A %d. %B %Y"))
print("d.ctime()")
print(d.ctime())

# Methods for to extracting 'components' under different calendars
t = d.timetuple()
for i in t:     
    print("i == ")
    print(i)

ic = d.isocalendar()
for i in ic:    
    print("i == ")
    print(i)
d.replace(year=2005)
print("d == ")
print(d)
