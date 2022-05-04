# -*- coding: utf-8 -*-
"""
Created on Tue May  3 23:04:23 2022

@author: eprol
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 11:32:14 2022

@author: eprol
"""

import numpy as np
import math
import matplotlib.pyplot as plt
import random_walk_checkpoint

class flock():
    def __init__(self,N,limit,L,P,V,delta,c1,c2,c3,c4,vlimit,p,v):
        self.N = N #No. of Boids 403
        self.limit = limit #Axis Limits
        self.L = limit*2
        self.P = P #Spread of initial position (gaussian)
        self.V = V #Spread of initial velocity (gaussian)
        self.delta = delta #Time Step
        self.c1 = c1 #Attraction Scaling factor
        self.c2 = c2 #Repulsion scaling factor
        self.c3 = c3 #Heading scaling factor
        self.c4 = c4 #Randomness scaling factor
        self.vlimit = vlimit #Maximum velocity
        #Initialize
        self.p = p
        self.v = v
    def calc_frame(self):
        v1 = np.zeros((2,self.N))
        v2 = np.zeros((2,self.N))


        #YOUR CODE HERE
        #Calculate Average Velocity v3 
        v3 = np.array([sum(self.v[0 ,:])/self.N, sum(self.v[1 ,:])/self.N])*self.c3

        if (np.linalg.norm(v3) > self.vlimit): #limit maximum velocity
            v3 = v3*self.vlimit/np.linalg.norm(v3)
        for n in range(0, self.N):
            for m in range(0, self.N):
                if m!=n:
                    #YOUR CODE HERE
                    #Compute vector r from one agent to the next
                    r = self.p[:,m]-self.p[:,n]

                    if r[0] > self.L/2:
                        r[0] = r[0]-self.L
                    elif r[0] < -self.L/2:
                        r[0] = r[0]+self.L
                    if r[1] > self.L/2:
                        r[1] = r[1]-self.L
                    elif r[1] < -self.L/2:
                        r[1] = r[1]+self.L
                    #YOUR CODE HERE
                    #Compute distance between agents rmag
                    rmag = math.sqrt(r[0]**2+r[1]**2)

                    #Compute attraction v1
                    if(m == 100):
                         v1[:,n] = v1[:,n] + (0.00003*r)
                    if(m == 101):
                        v1[:,n] = v1[:,n] + (0.00003*r)
                    if(m == 102):
                        v1[:,n] = v1[:,n] + (self.c1*r)
                    if(m >= 51 and m < 100):
                        v1[:,n] = v1[:,n] + (0.0001*r)
                    if(m%10 == 0 and m < 51):
                        v1[:,n] = v1[:,n] + (0.001*r)
                    #else:
                    v1[:,n] = v1[:,n] + (self.c1*r)

                    #Compute Repulsion [non-linear scaling] v2
                    #need to make the agent only be impacted 1 at a time
                    #maybe just try it for m or just try the if statement for n
                    #if(m == 100):
                    #    v2[: ,n] = v2[: ,n]-((self.c2*r)/(rmag**2))
                    #elif(m == 101):
                    #    v2[: ,n] = v2[: ,n]-((self.c2*r)/(rmag**2))
                    if(m == 102):
                        v2[: ,n] = v2[: ,n]-((15*r)/(rmag**2))
                    #else:
                    v2[: ,n] = v2[: ,n]-((self.c2*r)/(rmag**2))

            #YOUR CODE HERE


            #Compute random velocity component v4
            v4 = np.zeros((2,self.N))
            v4[:,n] = self.c4*np.random.randn(2)
            #Update velocity
           #print("Update Velocity: ",str(v1[: ,n])," + ",str(v2[: ,n])," + ",str(v3), " = ",str(v1[: ,n]+v2[: ,n]+v3))
            self.v[: ,n] = v1[: ,n]+v2[: ,n]+v3+v4[:,n]
            #print("v: ",v)
        #YOUR CODE HERE
        #Update position
            if((n or m != 100) or (m or n != 101) or (m or n != 102)):
                self.p[: ,n] = (self.p[: ,n] + self.v[: ,n])*self.delta
        #Periodic boundary
        tmp_p = self.p
        tmp_p[0, self.p[0,:] > self.L] = tmp_p[0,self.p[0,:]> (self.L)] - self.L
        tmp_p[1, self.p[1,:] > self.L] = tmp_p[1, self.p[1,:] > (self.L)] - self.L
        tmp_p[0, self.p[0,:] < 0]  = tmp_p[0, self.p[0,:] < (0)] + self.L
        tmp_p[1, self.p[1,:] < 0]  = tmp_p[1, self.p[1,:] < (0)] + self.L
        self.p = tmp_p
        return self.p