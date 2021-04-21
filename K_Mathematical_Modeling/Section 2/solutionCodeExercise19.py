from IPython.display import display, Latex, Math

print("We can get rid of all parameters by setting: ")
display(Latex('$U=C/C_{max}$'))
print("and")
display(Latex('$T=t*\lambda$'))
print("both of which are unit-less")
print("Then the ODE becomes:")
print("")
display(Latex('$dU/dT=-U*\ln U,$'))
print("")
print("As we can see, there is no parameter, so we can use a natural scale for the time step (i.e., neither delta t = 0.00000001 nor delta t  = 1000000)")
print("")
print("Sequence of instructions for the forward Euler method:")
print("- delta_t=0.001")
print("- tmax=10")
print("- N=10000")
print("- U=array_of_zeros(1 row, 10001 columns ")
print("- U(1)=U0, initial value of the renormalized variable U")
print("- T=array_of_zeros(1 row, 10001 columns ")
print("- FOR i=1 to N+1 do T(i)=(i-1)*delta_t  end FOR loop   : we define the time grid")
print("- for i=1 to N do:")
print("      U(i+1)=U(i)-delta_t*U(i)*ln(U(i))")
print("end FOR loop")
print("plot({T(i),U(i)}")

print("")
print("Sequence of instructions for the RK4 method:")
print("- delta_t=0.001")
print("- tmax=10")
print("- N=10000")
print("- U=array_of_zeros(1 row, 10001 columns ")
print("- U(1)=U0, initial value of the renormalized variable U")
print("- T=array_of_zeros(1 row, 10001 columns ")
print("- FOR i=1 to N+1 do T(i)=(i-1)*delta_t  end FOR loop   : we define the time grid")
print("- for i=1 to N do:")
print("      k1=-U(i)*ln(U(i)) ")
print("      k2=-[U(i)+k1*delta_t/2]*ln([U(i)+k1*delta_t/2]) ")
print("      k3=-[U(i)+k2*delta_t/2]*ln([U(i)+k2*delta_t/2]) ")
print("      k4=-[U(i)+k3*delta_t]*ln([U(i)+k3*delta_t]) ")
print("      U(i+1)=U(i)+delta_t*(k1+2*k2+2*k3+k4)/6")
print("end FOR loop")
print("plot({T(i),U(i)}")

print("")
print("We note that the Euler method is equivalent to a Runge Kutta 4 scheme with k1=k2=k3=k4")



print("")
print("Python code for the Runge Kutta method:")




import numpy as np
import matplotlib.pyplot as plt



delta_t=0.001
tmax=10
N=10000
U = np.zeros(N+1)
T = np.zeros(N+1)
U[0]=0.5
for i in range(0,N):  # Python starts indexing rows and columns at 0, not 1 as in the algorithm above
        T[i] = i*delta_t
for i in range(0,N):  
        k1=-U[i]*np.log(U[i])
        k2=-(U[i]+0.5*k1*delta_t)*np.log((U[i]+0.5*k1*delta_t))
        k3=-(U[i]+0.5*k2*delta_t)*np.log((U[i]+0.5*k2*delta_t))
        k4=-(U[i]+k3*delta_t)*np.log((U[i]+k3*delta_t))
        U[i+1]=U[i]+delta_t*(k1+2*k2+2*k3+k4)/6

# plot the time variations of all the node values
plt.figure()
plt.plot(U,'-')
plt.show()