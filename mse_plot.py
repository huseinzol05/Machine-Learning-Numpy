import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
sns.set()

def subplot_evolution_strategies(step, learning_rate, sigma, population_size,
                                 x_boundary = 1, y_boundary = 2, 
                                 step_x = 20, step_y = 50, midpoint = 0, ax=None):
    if ax is None:
        ax = plt.gca()
    x = np.linspace(-x_boundary,x_boundary,step_x)
    y = midpoint * x
    
    def mean_square_error(theta):
        theta = np.atleast_2d(np.asarray(theta))
        return np.mean((y-hypothesis(x, theta))**2, axis=1)

    def hypothesis(x, theta):
        return theta * x
    
    theta_grid = np.linspace(-y_boundary,y_boundary,step_y)
    J_grid = mean_square_error(theta_grid[:,np.newaxis])

    ax.plot(theta_grid, J_grid)
    theta = [-y_boundary]
    J = [mean_square_error(theta[0])[0]]
    strings = 'X-axis steps:\n\n'
    for j in range(step-1):
        last_theta = theta[-1]
        random_weight = np.random.randn(population_size, step_x)
        population = np.zeros(population_size)
        for l in range(population_size):
            w_try = last_theta + sigma * random_weight[l]
            population[l] = -mean_square_error(w_try)
        A = (population - np.mean(population)) / np.std(population)
        current_theta = last_theta + learning_rate * np.mean((population_size * sigma) * np.dot(random_weight.T, A))
        strings += str(current_theta) + '\n'
        theta.append(current_theta)
        J.append(mean_square_error(current_theta)[0])
    colors = sns.color_palette("husl", step)
    for j in range(1,step):
        ax.annotate('', xy=(theta[j], J[j]), xytext=(theta[j-1], J[j-1]), arrowprops={'arrowstyle': '->', 'color': 'r', 'lw': 1},va='center', ha='center')
    ax.scatter(theta, J, c=colors, s=40, lw=0)
    ax.set_xlabel(r'$\theta_1$')
    ax.set_ylabel(r'$J(\theta_1)$')
    ax.set_title('MSE function on Evolution Strategies')
    return ax

def subplot_gradient_descent(step, learning_rate, technique, 
                             x_boundary = 1, y_boundary = 2,
                             momentum = 0.9, rho = 0.9, epsilon = 1e-8, 
                             b1 = 0.9, b2 = 0.999,
                             step_x = 20, step_y = 50, midpoint = 0, ax=None):
    if ax is None:
        ax = plt.gca()
    x = np.linspace(-x_boundary,x_boundary,step_x)
    y = midpoint * x
    
    def mean_square_error(theta):
        theta = np.atleast_2d(np.asarray(theta))
        return np.mean((y-hypothesis(x, theta))**2, axis=1)

    def hypothesis(x, theta):
        return theta * x
    
    theta_grid = np.linspace(-y_boundary,y_boundary,step_y)
    J_grid = mean_square_error(theta_grid[:,np.newaxis])

    ax.plot(theta_grid, J_grid)
    theta = [-y_boundary]
    J = [mean_square_error(theta[0])[0]]
    strings = 'X-axis steps:\n\n'
    velocity = np.zeros((1))
    second_velocity = np.zeros((1))

    for j in range(step-1):
        last_theta = theta[-1]
        if technique == 'gradient descent':
            gradient = np.sum((hypothesis(x, last_theta) - y) * x)
            current_theta = last_theta - learning_rate * gradient
        elif technique == 'momentum':
            gradient = np.sum((hypothesis(x, last_theta) - y) * x)
            velocity = velocity * momentum + learning_rate * gradient
            current_theta = last_theta - velocity
        elif technique == 'nesterov':
            gradient = np.sum((hypothesis(x, last_theta - momentum * velocity) - y) * x)
            velocity = velocity * momentum + learning_rate * gradient
            current_theta = last_theta - velocity
        elif technique == 'adagrad':
            gradient = np.sum((hypothesis(x, last_theta) - y) * x)
            velocity += np.square(gradient)
            current_theta = last_theta - learning_rate * gradient / np.sqrt(velocity + epsilon)
        elif technique == 'rmsprop':
            gradient = np.sum((hypothesis(x, last_theta) - y) * x)
            velocity += rho * velocity + (1 - rho) * np.square(gradient)
            current_theta = last_theta - learning_rate * gradient / np.sqrt(velocity + epsilon)
        elif technique == 'adam':
            gradient = np.sum((hypothesis(x, last_theta) - y) * x)
            velocity += b1 * velocity + (1-b1) * gradient
            second_velocity += b2 * second_velocity + (1-b2) * np.square(gradient)
            velocity_hat = velocity / (1-b1)
            second_velocity_hat = second_velocity / (1-b2)
            current_theta = learning_rate * velocity_hat / np.sqrt(second_velocity_hat + epsilon)
        else:
            raise Exception('Invalid optimizer')
        strings += str(current_theta) + '\n'
        theta.append(current_theta)
        J.append(mean_square_error(current_theta)[0])
    colors = sns.color_palette("husl", step)
    for j in range(1,step):
        ax.annotate('', xy=(theta[j], J[j]), xytext=(theta[j-1], J[j-1]), arrowprops={'arrowstyle': '->', 'color': 'r', 'lw': 1},va='center', ha='center')
    ax.scatter(theta, J, c=colors, s=40, lw=0)
    ax.set_xlabel(r'$\theta_1$')
    ax.set_ylabel(r'$J(\theta_1)$')
    ax.set_title('MSE function on %s Optimizer'%(technique))
    return ax