Birds_year0 = 100 
Birth_rate = 0.5
Death_rate = 0.2
# We repeat the "for" loop with an additional step: every 3 years, a harsh winter pushes half of the bird population to migrate to another forest
Time=[0]
Birds=[100]
timesincelastmigration = 0;
for year in range (1,51) :
    Birds = Birds + [Birds[-1] + Birds[-1] * Birth_rate - Birds[-1] * Death_rate ]
    Time = Time + [year]
    timesincelastmigration = timesincelastmigration + 1
    if timesincelastmigration == 3: 
        timesincelastmigration = 0
        Birds[-1]=Birds[-1]/2
    print(Birds[-1])
    
import matplotlib.pyplot as plt
plt.plot(Time,Birds)
plt.xlabel("Time (years)")
plt.ylabel("# of birds")
plt.title('Birds population growth')
plt.show()

