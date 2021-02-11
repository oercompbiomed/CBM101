clear all
close all
clc
k1=3;k2=4;
k3=[0:0.01:20];
y1=1./(1+k1+k1.*k2+k1.*k2.*k3);
y2=k1./(1+k1+k1.*k2+k1.*k2.*k3);
y3=k1.*k2./(1+k1+k1.*k2+k1.*k2.*k3);
y4=k1.*k2.*k3./(1+k1+k1.*k2+k1.*k2.*k3);
figure
hold on
plot(k3,y1,'color','black')
plot(k3,y2,'color','red')
plot(k3,y3,'color','blue')
plot(k3,y4,'color','green');

clear all
k1=3;k3=4;
k2=[2:0.01:6];
y1=1./(1+k1+k1.*k2+k1.*k2.*k3);
y2=k1./(1+k1+k1.*k2+k1.*k2.*k3);
y3=k1.*k2./(1+k1+k1.*k2+k1.*k2.*k3);
y4=k1.*k2.*k3./(1+k1+k1.*k2+k1.*k2.*k3);
figure
hold on
plot(k2,y1,'color','black')
plot(k2,y2,'color','red')
plot(k2,y3,'color','blue')
plot(k2,y4,'color','green');

clear all
k3=4;k2=4;
k1=[0:0.01:5];
y1=1./(1+k1+k1.*k2+k1.*k2.*k3);
y2=k1./(1+k1+k1.*k2+k1.*k2.*k3);
y3=k1.*k2./(1+k1+k1.*k2+k1.*k2.*k3);
y4=k1.*k2.*k3./(1+k1+k1.*k2+k1.*k2.*k3);
figure
hold on
plot(k1,y1,'color','black')
plot(k1,y2,'color','red')
plot(k1,y3,'color','blue')
plot(k1,y4,'color','green');

