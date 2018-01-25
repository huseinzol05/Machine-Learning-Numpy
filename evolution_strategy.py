import numpy as np
import time

class Deep_Evolution_Strategy:
    
    def __init__(self, weights, inputs, solutions, reward_function, population_size, sigma, learning_rate):
        self.weights = weights.copy()
        self.inputs = inputs
        self.solutions = solutions
        self.reward_function = reward_function
        self.population_size = population_size
        self.sigma = sigma
        self.learning_rate = learning_rate
        
    def _get_weight_from_population(self, population):
        weights_population = []
        for index, i in enumerate(population):
            jittered = self.sigma * i
            weights_population.append(self.weights[index] + jittered)
        return weights_population
    
    def get_weight(self):
        return self.weights
    
    def predict(self, weights, inputs, activation_function = None):
        if activation_function[0]:
            w = activation_function[0](inputs * weights[0])
        else:
            w = inputs * weights[0]
        for n in range(1, len(weights)):
            if activation_function[n]:
                w = activation_function[n](np.dot(w, weights[n]))
            else:
                w = np.dot(w, weights[n])
        return w
    
    def train(self, epoch = 100, print_every = 5, activation_function = None):
        lasttime = time.time()
        for i in range(epoch):
            population = []
            rewards = np.zeros(self.population_size)
            for k in range(self.population_size):
                x = []
                for w in self.weights:
                    x.append(np.random.randn(*w.shape))
                population.append(x)
            for k in range(self.population_size):
                weights_population = self._get_weight_from_population(population[k])
                w = self.predict(weights_population, self.inputs, activation_function = activation_function)
                rewards[k] = self.reward_function(self.solutions, w)
            rewards = (rewards - np.mean(rewards)) / np.std(rewards)
            for index, w in enumerate(self.weights):
                A = np.array([p[index] for p in population])
                self.weights[index] = w + self.learning_rate/(self.population_size * self.sigma) * np.dot(A.T, rewards).T
            if (i+1) % print_every == 0:
                w = self.predict(self.weights, self.inputs, activation_function = activation_function)
                print('iter %d. reward: %f' %  (i+1, self.reward_function(self.solutions, w)))
        print('time taken to train:', time.time()-lasttime, 'seconds')   