# GeneticAlgorithmPython
**GeneticAlgorithmPython** is an open source Python project for implementing the genetic algorithm based on NumPy. Based on this project, a Python library named [`PyGAD`](https://pypi.org/project/pygad) is available at PyPI: https://pypi.org/project/pygad. To install PyGAD using pip, just issue this command:

```python
pip install pygad
```

The project has a single module named `pygad.py` which contains a class named `GA`. There is a script named `example.py` in which an example is given for using the `pygad.py` module. 

Simply, to run the genetic algorithm all you need to do is to create an instance of the `GA` class and pass the appropriate parameters to its constructor. The `GA` class has all the required parameters and methods for implementing the genetic algorithm. 

The documentation starts by discussing the available parameters in addition to the steps of using the library. Note that the [PyGAD library](https://pypi.org/project/pygad) is a reflection to the **GeneticAlgorithmPython** GitHub project. As a result, the documentation can either use **project** or **library** interchangeably.

## Supported Parameters

The single module available in the `PyGAD` library is named `pygad.py` and contains a class named `GA`. For creating an instance of this class, there are a number of parameters that allows the user to customize the genetic algorithm. Before running the GA, the parameters must be prepared. The list of all supported parameters is as follows:

- `num_generations` : Number of generations.
- `num_parents_mating ` : Number of solutions to be selected as parents.
- `fitness_func` : Accepts a function that must accept 2 parameters (a single solution and its index in the population) and return the fitness value of the solution. Available starting from [PyGAD](https://pypi.org/project/pygad) 1.0.17 until 1.0.20 with a single parameter representing the solution. Changed in [PyGAD](https://pypi.org/project/pygad) 2.0.0 and higher to include the second parameter representing the solution index.
- `initial_population`: A user-defined initial population. It is useful when the user wants to start the generations with a custom initial population. It defaults to `None` which means no initial population is specified by the user. In this case, [**PyGAD**](https://pypi.org/project/pygad) creates an initial population using the `sol_per_pop` and `num_genes` parameters. An exception is raised if the `initial_population` is `None` while any of the 2 parameters (`sol_per_pop` or `num_genes`) is also `None`. Introduced in PyGAD 2.0.0 and higher.
- `sol_per_pop` : Number of solutions (i.e. chromosomes) within the population.
- `num_genes`: Number of genes in the solution/chromosome.
- `init_range_low=-4`: The lower value of the random range from which the gene values in the initial population are selected. `init_range_low` defaults to `-4`. Available in [PyGAD](https://pypi.org/project/pygad) 1.0.20 and higher.
- `init_range_high=4`: The upper value of the random range from which the gene values in the initial population are selected. `init_range_high` defaults to `+4`. Available in [PyGAD](https://pypi.org/project/pygad) 1.0.20 and higher.
- `parent_selection_type="sss"` : The parent selection type. Supported types are `sss` (for steady state selection), `rws` (for roulette wheel selection), `sus` (for stochastic universal selection), `rank` (for rank selection), `random` (for random selection), and `tournament` (for tournament selection).
- `keep_parents=-1` : Number of parents to keep in the current population. `-1` (default) means keep all parents in the next population. `0` means keep no parents in the next population. A value `greater than 0` means keep the specified number of parents in the next population. Note that the value assigned to `keep_parents` cannot be `< - 1` or greater than the number of solutions within the population `sol_per_pop`.
- `K_tournament=3` : In case that the parent selection type is `tournament`, the `K_tournament` specifies the number of parents participating in the tournament selection. It defaults to `3`.
- `crossover_type="single_point"` : Type of the crossover operation. Supported types are `single_point` (for single point crossover), `two_points` (for two points crossover), and `uniform` (for uniform crossover). It defaults to `single_point`.
- `mutation_type="random"` : Type of the mutation operation. Supported types are `random` (for random mutation), `swap` (for swap mutation), `inversion` (for inversion mutation), and `scramble` (for scramble mutation). It defaults to `random`.
- `mutation_percent_genes=10` : Percentage of genes to mutate which defaults to `10`. Out of this percentage, the number of genes to mutate is deduced. This parameter has no action if the parameter `mutation_num_genes` exists. 
- `mutation_num_genes=None` : Number of genes to mutate which defaults to `None` meaning that no number is specified. If the parameter `mutation_num_genes` exists, then no need for the parameter `mutation_percent_genes`.
- `random_mutation_min_val=-1.0` : For `random` mutation, the `random_mutation_min_val` parameter specifies the start value of the range from which a random value is selected to be added to the gene. It defaults to `-1`.
- `random_mutation_max_val=1.0` : For `random` mutation, the `random_mutation_max_val` parameter specifies the end value of the range from which a random value is selected to be added to the gene. It defaults to `+1`.
- `callback_generation`: If not `None`, then it accepts a function to be called after each generation. This function must accept a **single parameter** representing the instance of the genetic algorithm.

The user doesn't have to specify all of such parameters while creating an instance of the GA class. A very important parameter you must care about is `fitness_func` which defines the fitness function.

It is OK to set the value of any of the 2 parameters `init_range_low` and `init_range_high` to be equal, higher or lower than the other parameter (i.e. `init_range_low` is not needed to be lower than `init_range_high`).

## Instance Attributes

All the parameters and functions passed to the GA class constructor are used as attributes and methods in the instances of the GA class. In addition to such attributes, there are other attributes and methods added to the instances of the GA class which are:

- `generations_completed`:  Holds the number of the last completed generation.
- `population`: A NumPy array holding the initial population.
- `valid_parameters`: Set to `True` when all the parameters passed in the `GA` class constructor are valid.
- `run_completed`: Set to `True` only after the `run()` method completes gracefully.
- `pop_size`: The population size.
- `crossover`: Refers to the method that applies the crossover operator based on the selected type of crossover in the `crossover_type` property.
- `mutation`: Refers to the method that applies the mutation operator based on the selected type of mutation in the `mutation_type` property.
- `select_parents`: Refers to a method that selects the parents based on the parent selection type specified in the `parent_selection_type` attribute.
- `best_solution_fitness`: A list holding the fitness value of the best solution for each generation.
- `cal_pop_fitness`: A method that calculates the fitness values for all solutions within the population by calling the function passed to the `fitness_func` parameter for each solution.

Next, the steps of using the PyGAD library are discussed.

## How to Use the PyGAD?

To use PyGAD, here is a summary of the required steps: 

1. Preparing the `fitness_func` parameter.
2. Preparing other parameters.
3. Example of preparing the parameters.
4. Import the `pygad.py` module.
5. Create an instance of the `GA` class.
6. Run the genetic algorithm.
7. Plotting Results.
8. Saving & Loading the Results.

Let's discuss how to do each of these steps.

### Preparing the `fitness_func` Parameter

Even there are a number of steps in the genetic algorithm pipeline that can work the same regardless of the problem being solved, one critical step is the calculation of the fitness value. There is no unique way of calculating the fitness value and it changes from one problem to another. 

On **`15 April 2020`**, a new argument named `fitness_func` is added to PyGAD 1.0.17 that allows the user to specify a custom function to be used as a fitness function. This function must be a **maximization function** so that a solution with a high fitness value returned is selected compared to a solution with a low value. Doing that allows the user to freely use the library to solve any problem by passing the appropriate fitness function. 

Let's discuss an example:

> Given the following function:
>     y = f(w1:w6) = w1x1 + w2x2 + w3x3 + w4x4 + w5x5 + 6wx6
>     where (x1,x2,x3,x4,x5,x6)=(4,-2,3.5,5,-11,-4.7) and y=44
> What are the best values for the 6 weights (w1 to w6)? We are going to use the genetic algorithm to optimize this function.

So, the task is about using the genetic algorithm to find the best values for the 6 weight `W1` to `W6`. Thinking of the problem, it is clear that the best solution is that returning an output that is close to the desired output `y=44`. So, the fitness function should return a value that gets higher when the solution's output is closer to `y=44`. Here is a function that does that:

```python
function_inputs = [4,-2,3.5,5,-11,-4.7] # Function inputs.
desired_output = 44 # Function output.

def fitness_func(solution, solution_idx):
    output = numpy.sum(solution*function_inputs)
    fitness = 1.0 / numpy.abs(output - desired_output)
    return fitness
```

The function must accept 2 parameters:

1. 1D vector representing a single solution. Introduced in PyGAD 1.0.17 and higher.
2. Solution index within the population. Introduced in PyGAD 2.0.0 and higher.

By creating this function, you are ready to use the library. 

### Example of Preparing the Parameters

Here is an example for preparing the parameters:

```python
num_generations = 50
num_parents_mating = 4

fitness_function = fitness_func

sol_per_pop = 8
num_genes = len(function_inputs)

init_range_low = -2
init_range_high = 5

parent_selection_type = "sss"
keep_parents = 1

crossover_type = "single_point"

mutation_type = "random"
mutation_percent_genes = 10
```

#### Optional `callback_generation` Parameter

In PyGAD 2.0.0 and higher, an optional parameter named `callback_generation` is supported which allow the user to call a function (with a single parameter) after each generation. Here is a simple function that just prints the current generation number and the fitness value of the best solution in the current generation. The `generations_completed` attribute of the GA class returns the number of the last completed generation.

```python
def callback_gen(ga_instance):
    print("Generation : ", ga_instance.generations_completed)
    print("Fitness of the best solution :", ga_instance.best_solution()[1])
```

After being defined, the function is assigned to the `callback_generation` parameter of the GA class constructor. By doing that, the `callback_gen()` function will be called after each generation.

```python
ga_instance = pygad.GA(..., 
                       callback_generation=callback_gen,
                       ...)
```

After the parameters are prepared, we can import the `pygad` module and build an instance of the GA class.

### Import the `pygad.py` Module

The next step is to import the `pygad` module as follows:

```python
import pygad
```

This module has a class named `GA` which holds the implementation of all methods for running the genetic algorithm.

### Create an Instance of the `GA` Class.

The `GA` class is instantiated where the previously prepared parameters are fed to its constructor. The constructor is responsible for creating the initial population.

```python
ga_instance = pygad.GA(num_generations=num_generations,
                       num_parents_mating=num_parents_mating, 
                       fitness_func=fitness_function,
                       sol_per_pop=sol_per_pop, 
                       num_genes=num_genes,
                       init_range_low=init_range_low,
                       init_range_high=init_range_high,
                       parent_selection_type=parent_selection_type,
                       keep_parents=keep_parents,
                       crossover_type=crossover_type,
                       mutation_type=mutation_type,
                       mutation_percent_genes=mutation_percent_genes)
```

### Run the Genetic Algorithm

After an instance of the `GA` class is created, the next step is to call the `run()` method as follows:

```python
ga_instance.run()
```

Inside this method, the genetic algorithm evolves over a number of generations by doing the following tasks:

1. Calculating the fitness values of the solutions within the current population.
2. Select the best solutions as parents in the mating pool.
3. Apply the crossover & mutation operation
4. Repeat the process for the specified number of generations. 

### Plotting Results

There is a method named `plot_result()` which creates a figure summarizing how the fitness values of the solutions change with the generations .

```python
ga_instance.plot_result()
```

![Fig02](https://user-images.githubusercontent.com/16560492/78830005-93111d00-79e7-11ea-9d8e-a8d8325a6101.png)

### Saving & Loading the Results

After the `run()` method completes, it is possible to save the current instance of the genetic algorithm to avoid losing the progress made. The `save()` method is available for that purpose. According to the next code, a file named `genetic.pkl` will be created and saved in the current directory.

```python
# Saving the GA instance.
filename = 'genetic' # The filename to which the instance is saved. The name is without extension.
ga_instance.save(filename=filename)
```

You can also load the saved model using the `load()` function and continue using it. For example, you might run the genetic algorithm for a number of generations, save its current state using the `save()` method, load the model using the `load()` function, and then call the `run()` method again.

```python
# Loading the saved GA instance.
loaded_ga_instance = pygad.load(filename=filename)
```

After the instance is loaded, you can use it to run any method or access any property.

```python
print(loaded_ga_instance.best_solution())
```

## Crossover, Mutation, and Parent Selection

The library supports different types for selecting the parents and applying the crossover & mutation operators. More features will be added in the future. To ask for a feature, please open an issue in the [GitHub project](https://github.com/ahmedfgad/GeneticAlgorithmPython): https://github.com/ahmedfgad/GeneticAlgorithmPython/issues/new

The supported crossover operations at this time are:

- Single point: Implemented using the `single_point_crossover()` method.
- Two points: Implemented using the `two_points_crossover()` method.
- Uniform: Implemented using the `uniform_crossover()` method.

The supported mutation operations at this time are:

- Random: Implemented using the `random_mutation()` method.
- Swap: Implemented using the `swap_mutation()` method.
- Inversion: Implemented using the `inversion_mutation()` method.
- Scramble: Implemented using the `scramble_mutation()` method.

The supported parent selection techniques at this time are:

- Steady state: Implemented using the `steady_state_selection()` method.
- Roulette wheel: Implemented using the `roulette_wheel_selection()` method.
- Stochastic universal: Implemented using the `stochastic_universal_selection()` method.
- Rank: Implemented using the `rank_selection()` method.
- Random: Implemented using the `random_selection()` method.
- Tournament: Implemented using the `tournament_selection()` method.

More types will be added in the future. You can also ask for supporting more types by opening an issue in the [GitHub project](https://github.com/ahmedfgad/GeneticAlgorithmPython) associated with the library: https://github.com/ahmedfgad/GeneticAlgorithmPython

## Release History

PyGAD 1.0.17 (15 April 2020):

1. The `GA` class accepts a new argument named `fitness_func` which accepts a function to be used for calculating the fitness values for the solutions. This allows the project to be customized to any problem by building the right fitness function.

PyGAD 1.0.20 (4 May 2020):

1. The attributes are moved from the class scope to the instance scope.
2. Raising a `ValueError` exception on passing incorrect values to the parameters.
3. Two new parameters are added (`init_range_low` and `init_range_high`) allowing the user to customize the range from which the genes values in the initial population are selected. 
4. The code object `__code__` of the passed fitness function is checked to ensure it has the right number of parameters.

PyGAD 2.0.0 (13 May 2020)

1. The fitness function accepts a new argument named `sol_idx` representing the index of the solution within the population.
2. A new parameter to the GA constructor named `initial_population` is supported to allow the user to use a custom initial population to be used by the genetic algorithm. If not None, then the passed population will be used. If `None`, then the genetic algorithm will create the initial population using the `sol_per_pop` and `num_genes` parameters. 
3. The parameters `sol_per_pop` and `num_genes` are optional and set to `None` by default.
4. A new parameter named `callback_generation` is introduced in the GA class constructor. It accepts a function with a single parameter representing the GA instance. This function called after each generation. This helps the user to do post-processing or debugging operations after each generation.

## For More Information

To start with coding the genetic algorithm, you can check the tutorial titled [**Genetic Algorithm Implementation in Python**](https://www.linkedin.com/pulse/genetic-algorithm-implementation-python-ahmed-gad) available at these links:

- https://www.linkedin.com/pulse/genetic-algorithm-implementation-python-ahmed-gad

- https://towardsdatascience.com/genetic-algorithm-implementation-in-python-5ab67bb124a6

[This tutorial](https://www.linkedin.com/pulse/genetic-algorithm-implementation-python-ahmed-gad) is prepared based on a previous version of the project but it still a good resource to start with coding the genetic algorithm.

![Fig03](https://user-images.githubusercontent.com/16560492/78830052-a3c19300-79e7-11ea-8b9b-4b343ea4049c.png)

You can also check my book cited as [**Ahmed Fawzy Gad 'Practical Computer Vision Applications Using Deep Learning with CNNs'. Dec. 2018, Apress, 978-1-4842-4167-7**](https://www.amazon.com/Practical-Computer-Vision-Applications-Learning/dp/1484241665).

![Fig04](https://user-images.githubusercontent.com/16560492/78830077-ae7c2800-79e7-11ea-980b-53b6bd879eeb.jpg)

---

**Important Note**

The library just supports the decimal representation for the chromosome and there is no current support for binary representations. The library is updated and soon support for the binary version will be available.

## Get in Touch

* E-mail: ahmed.f.gad@gmail.com
* [LinkedIn](https://www.linkedin.com/in/ahmedfgad)
* [Amazon Author Page](https://amazon.com/author/ahmedgad)
* [Heartbeat](https://heartbeat.fritz.ai/@ahmedfgad)
* [Paperspace](https://blog.paperspace.com/author/ahmed)
* [KDnuggets](https://kdnuggets.com/author/ahmed-gad)
* [TowardsDataScience](https://towardsdatascience.com/@ahmedfgad)
* [GitHub](https://github.com/ahmedfgad)
