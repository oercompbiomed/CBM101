Birds_year0 = 100 
Birth_rate = 0.5
Death_rate = 0.2
# We repeat the "for" loop with an additional step: every time bird population reaches 1000, an epidemic kills half of them
Time=[0]
Birds=[100]
for year in range (1,51) :
    Birds = Birds + [Birds[-1] + Birds[-1] * Birth_rate - Birds[-1] * Death_rate ]
    Time = Time + [year]
    if Birds[-1]>1000: 
        Birds[-1]=Birds[-1]/2
    print(Birds[-1])
    
import matplotlib.pyplot as plt
plt.plot(Time,Birds)
plt.xlabel("Time (years)")
plt.ylabel("# of birds")
plt.title('Birds population growth')
plt.show()

