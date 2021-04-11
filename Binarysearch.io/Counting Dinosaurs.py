'''
Counting Dinosaurs

You are given a string animals 
and another string dinosaurs. 
Every letter in animals represents 
a different type of animal and 
every unique character in dinosaurs 
represents a different dinosaur.

Return the total number of dinosaurs in animals.
'''


class Solution:
    def solve(self, animals, dinosaurs):
        a = [i for i in animals]
        d = set([j for j in dinosaurs])

        dino_count = 0

        for i in a:
            if i in d:
                dino_count += 1

        return dino_count
