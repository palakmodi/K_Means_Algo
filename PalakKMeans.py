# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 17:31:37 2016

@author: Palak
"""
import numpy as np
import random
import math
import sys
clustersize= 3
         
if __name__ == "__main__":
    #open the data file
    file_ptr = open('km-data.txt')
    
    #put the data points in a 2D list
    data = []
    for line in file_ptr.readlines():
        data.append([float(x) for x in line.strip().split(',')])
        
    #create a numPy 2D array from the list
    num_array = np.array(data)
    print "\n"
    print "------------------------\n"
    
    #assign the initial centroids by calling Random function
    initial_centroids= random.sample(num_array,clustersize);
    print "\n"
    print "------------------------\n"
    print "Initial Centroid Values\n"
    print "\n"
    print initial_centroids
    print "------------------------\n"
    
    #Ask for user choice, if he wants to calculate clusters based on Euclidean or Manhattan Distances?
    print "Do you want to calculate distances between data points and centroids with\n 1. Euclidean 'D1' (Press 1)\n 2. Manhattan 'D2' (Press 2)"
    print "\n"

    flag = sys.stdin.readline().strip()
    #Take a 0*150 list, to store values of assignment of clusters for 150 points
    clusters= [0]*150
    previous_centroid=[0]

    while(True):
        for i in range(len(num_array)):
            x = num_array[i];
            best= 100000000
            for j in range(len(initial_centroids)):
                y= initial_centroids[j]
                #Euclidean Distance
                if(flag== '1'):
                    current= math.sqrt(((x[0]-y[0])**2 + (x[1]-y[1])**2))
                #Manhattan Distance
                if(flag== '2'):
                    current= abs((x[0]-y[0]))+abs((x[1]-y[1]))
                if(current< best):
                    best = current
                #Assignment of points to Cluster
                    clusters[i] = j
        for i in range(len(initial_centroids)):
            cluster_list=[]
            for j in range(len(clusters)):
                if (clusters[j]== i):
                    cluster_list.append(num_array[j])
            #Recomputing the Centroid according to mean
            initial_centroids[i]= np.mean(cluster_list,axis=0)
            # Condition to stop computing Cluster Assignment
        if(previous_centroid== initial_centroids[0][0]):
            break;
        else:
            previous_centroid= initial_centroids[0][0] 
    print "\n"
    print "Final Centroid Values\n"
    print initial_centroids
    print "\n"
    print "Final Cluster assignment for all the data points\n"
    print clusters
    file_ptr.close()
    
