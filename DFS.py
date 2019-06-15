# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 21:20:43 2019

@author: jkunka
"""
import numpy as np;

def dfs(binary_image, visited, i, j):
    visited[i][j] = 1;
    neighbors = adjacent(i, j, len(binary_image[0]), len(binary_image),  visited, binary_image);
    for point in neighbors:
        dfs(binary_image, visited, point['x'], point['y']);
    return;
    
# children for DFS
def adjacent(i, j, width, height, visited, binary_image):
    indices = [];
    for x in range(3):
        for y in range(3):
            # valid adjacent and not visited and value should be 1
            if(i - 1 + x >= 0 and i - 1 + x < width and j - 1 + y >=0 and j - 1 + y < height and visited[i - 1 + x][j - 1 + y] == 0 and binary_image[i - 1 + x][j - 1 + y] == 1):
                indices.append( {"x": (i - 1 + x), "y": (j - 1 + y)} );
    
    return indices;

def calculate_num_characters(binary_image):
    num_chars = 0;
    visited = np.zeros((len(binary_image), len(binary_image[0])));
    for i in range(len(binary_image)):
        for j in range(len(binary_image[i])):
            if(visited[i][j] == 0 and binary_image[i][j] == 1) :
                num_chars = num_chars + 1;
                dfs(binary_image, visited, i, j);
                # already visited ignore
            
    print(num_chars)
    return num_chars


sample = [[0,0,0,0,0,0,0,0],
          [0,1,0,0,0,1,0,0],
          [0,0,1,0,0,1,0,0],
          [0,0,1,0,0,1,0,0],
          [0,1,0,0,0,1,0,0],
          [0,1,1,1,1,1,0,0],
          [0,0,0,0,0,0,0,0]]

calculate_num_characters(sample)