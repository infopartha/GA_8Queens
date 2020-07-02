# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 22:46:40 2020

@author: 257095
"""
import os
from random import sample
from datetime import datetime as dt
from colorama import Fore, Back, Style

class NQueens_GA:
    """
    Solving n-Queens problem using Genetic Algorithm
    """
    
    def __init__(self, num_of_queens = 8, visualize = False):
        """
        Initialize n-Queens problem solver

        Parameters
        ----------
        num_of_queens : TYPE, optional
            Number of Queens to be placed or Size of the nXn Chess board. 
            The default is 8.

        """
        self.num_of_queens = num_of_queens
        self.population = list()
        self.visualize = visualize
        self.generation = 0
        self.trials = 0
        
    def init_population(self, population_size = 100):
        self.population = list()
        for each in range(population_size):
            self.population.append(sample(range(self.num_of_queens), self.num_of_queens))
        
    def fitness_score(self, chromosome):
        survival = list()
        for gene_i in range(self.num_of_queens):
            allele_i = chromosome[gene_i]
            survival_score = self.num_of_queens
            for gene_j in range(self.num_of_queens):
                if gene_i == gene_j:
                    continue
                allele_j = chromosome[gene_j]
                if allele_i == allele_j or ((gene_i - allele_i) == (gene_j - allele_j)) or ((gene_i + allele_i) == (gene_j + allele_j)):
                    survival_score -= 1
            survival.append(survival_score)
        
        fitness = (sum(survival)/(self.num_of_queens**2))
        return(fitness, survival)
    
    def select_parents(self):
        par1 = par2 = None
        par1_fit = par2_fit = 0
        #par1_surv = par2_surv = None
        
        for chromosome in self.population:
            fit, surv = self.fitness_score(chromosome)
            if fit > par1_fit:
                par2, par2_fit = par1, par1_fit
                par1, par1_fit = chromosome, fit
            elif fit > par2_fit:
                par2, par2_fit = chromosome, fit
        
        return(par1, par2)
    
    def display(self, chromosome):
        print('Generation: {}'.format(self.generation))
        for allele in range(self.num_of_queens):
            for gene in range(self.num_of_queens):
                bgcolor = Back.CYAN if (allele + gene) % 2 == 0 else Back.WHITE
                if allele == chromosome[gene]:
                    print(bgcolor + Fore.BLACK + ' Q ', end='')
                else:
                    print(bgcolor + Fore.BLACK + '   ', end='')
            print('')
        print(Style.RESET_ALL)
    
    def goal_check(self, chromosome):
        self.trials += 1
        fit, surv = self.fitness_score(chromosome)
        if fit == 1:
            print('==== Solution Found ====')
            self.display(chromosome)
            print('Solution  : {}'.format(chromosome))
            #print('Iterations: {}'.format(self.trials))
            return True
        if self.visualize:
            os.system('cls')
            self.display(chromosome)
        return False
    
    def crossover(self, par1, par2):
        fit1, surv1 = self.fitness_score(par1)
        fit2, surv2 = self.fitness_score(par2)
        offspring = list()
        for i in range(self.num_of_queens):
            if surv1[i] == surv2[i]:
                if par1[i] not in offspring:
                    offspring.append(par1[i])
                else:
                    offspring.append(par2[i])
            elif surv1[i] > surv2[i]:
                offspring.append(par1[i])
            else:
                offspring.append(par2[i])
        return offspring
    
    def mutate(self, chromosome):
        miss = list()
        dupl = list()
        for gene in range(self.num_of_queens):
            cnt = chromosome.count(gene)
            if cnt == 0:
                miss.append(gene)
            elif cnt > 1:
                dupl.append(gene)
        for i in range(len(miss)):
            chromosome[chromosome.index(dupl[i])] = miss[i]
        
        return chromosome
    
    def addChromosome(self, chromosome):
        if chromosome not in self.population:
            self.population.append(chromosome)
    
    def removeChromosome(self, chromosome):
        if chromosome in self.population:
            self.population.remove(chromosome)




st = dt.now()
if __name__ == '__main__':
    
    num_of_queens = 8
    population_size = 200
    
    nQns = NQueens_GA(num_of_queens, False)
    nQns.init_population(population_size)
    
    while True:    #nQns.generation < 200:
        nQns.generation += 1
        
        if len(nQns.population) < 2:
            nQns.init_population(population_size)
        
        par1, par2 = nQns.select_parents()
        
        if nQns.goal_check(par1):
            break
        
        offspring = nQns.crossover(par1, par2)
        
        if nQns.goal_check(par1):
            break
        
        mutant = nQns.mutate(offspring)
        
        if nQns.goal_check(par1):
            break
        
        nQns.addChromosome(mutant)
        nQns.removeChromosome(par1)
        nQns.removeChromosome(par2)

et = dt.now()
print('Started at  : {}'.format(st))
print('Finished at : {}'.format(et))
print('Time taken  : {}'.format(et-st))
