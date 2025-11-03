# Computer Sciences for Physics and Chemistry – Practical Works

This repository contains all practical works for the course **Computer Sciences for Physics and Chemistry** (Prof. Dr. Morgan Madec, morgan.madec@unistra.fr).
---

## 1. Calculation of Pi
**File:** `pi_evaluation.py`  
Implements two methods to estimate Pi:  
1. **Deterministic (Trapezoidal)** – divides a semicircle into N trapezoids and sums their areas to approximate Pi.  
2. **Stochastic (Monte Carlo)** – randomly throws N points into a square and counts how many fall inside the circle to estimate Pi = 4·(inside/total).  
Both methods ask the user for N, measure computation time using `datetime`, and print the resulting Pi value and timing.  
Uses `numpy`, `math`, and `datetime` modules.

---

## 2. Integration and Derivatives in Mechanics, Noise Analysis
**File:** `derivatives_and_integration.py`
Simulates motion along sinusoidal trajectories with added noise and explores the effect of numerical integration on noisy data.

1. Generates synthetic position data `x(t)` and `y(t)` as sine functions.  
2. Adds random noise to simulate measurement errors.  
3. Computes acceleration both analytically and from noisy data using `np.gradient`.  
4. Integrates acceleration twice with `scipy.integrate.cumulative_trapezoid` to reconstruct position.  
5. Plots and compares the reconstructed and original noisy trajectories to visualize noise effects.
Uses `numpy`, `matplotlib`, and `scipy`.


---

## 3. RC Circuit Simulation
**File:** `rc_bridge_voltage.py`  
Models and compares numerical and analytical solutions for the charging of a capacitor in an RC circuit.

1. Defines the differential equation for capacitor voltage:  
   $$\frac{dV_c}{dt} = \frac{1}{RC}(V_{in} - V_c)$$  
2. Solves it numerically with `scipy.integrate.solve_ivp`.  
3. Calculates the analytical solution:  
   $$V_c(t) = V_{in} \left(1 - e^{-\frac{t}{RC}}\right)$$  
4. Plots both results and their difference to assess numerical accuracy.

Uses `numpy`, `matplotlib`, and `scipy`.

---

## 4. Solving a Multi-Node Circuit

### File 1: `equation_solver_sympy.py`
Solves a four-node resistor network symbolically using Kirchhoff’s laws.

1. Defines voltage variables **VA**, **VB**, **VC**, **VD** and equations using `sympy.Eq`.  
2. Solves the system analytically with `sympy.solve`.  
3. Substitutes numerical resistor and voltage source values to get numerical results.  
Uses `sympy` for symbolic algebra.

### File 2: `equation_solver_linear_algebra.py`
Solves the same circuit numerically using linear algebra.

1. Builds the matrix form **$A \cdot V = B$** from Kirchhoff’s equations.  
2. Solves for node voltages **VA**, **VB**, **VC**, **VD** using `numpy.linalg.solve`.  
3. Compares numerical results with symbolic ones for verification.  
Uses `numpy` for matrix computation.

### File 3: `equation_solver_scipy.py`
Finds the circuit’s node voltages through error minimization.

1. Defines a cost function as the sum of squared residuals of Kirchhoff’s equations.  
2. Minimizes this cost using `scipy.optimize.minimize`.  
3. Prints the optimized voltages **VA**, **VB**, **VC**, **VD** and compares them to previous methods.  
Uses `numpy` and `scipy.optimize` for numerical optimization.

---

## 5. Chemical Kinetics, Stochastic Simulation

### File 1: `gillespie_simple_reaction.py`
Simulates a reversible chemical reaction **$A + B \rightleftharpoons AB$** using the **Gillespie stochastic algorithm**.

1. Initializes molecule counts and rate constants for forward and reverse reactions.  
2. Calculates reaction propensities (`rate_forward`, `rate_reverse`) at each step.  
3. Randomly selects the next reaction event and time increment using exponential and uniform distributions.  
4. Updates molecule counts and records their evolution over time.  
5. Plots concentration changes of **A**, **B**, and **AB** as functions of time.  
Uses `numpy` and `matplotlib`.

### File 2: `gillespie_enzymatic_reaction.py`
Compares stochastic and deterministic models of an **enzyme-catalyzed reaction**  
**$$E + S \rightleftharpoons ES \rightarrow E + P$$**

1. Implements the stochastic version using the **Gillespie algorithm** to simulate discrete reaction events.  
2. Defines the deterministic model with a system of ODEs solved by `scipy.integrate.odeint`.  
3. Tracks the evolution of enzyme (**E**), substrate (**S**), product (**P**), and complex (**ES**) over time.  
4. Plots and compares the stochastic (random) and deterministic (smooth) product formation curves.  
Uses `numpy`, `scipy`, and `matplotlib`.

---

## 6. Lifetime Fluorescence Spectroscopy, Curve Fitting

**File:** `curve_fitting.py`  
Analyzes fluorescence decay data from mixtures of polycyclic aromatic hydrocarbons (PAHs) and identifies molecular contributions using curve fitting.

1. Models the total fluorescence signal as a sum of six exponential decays, each corresponding to a PAH with a known lifetime (`TAUS`).  
2. Imports experimental data from 5 text (`.txt`) and 1 binary (`.dat`) files.  
   - Text files contain one data point per line with uniform time steps.  
   - Binary files store 16-bit unsigned integers representing fluorescence levels.  
3. Constructs a time axis and applies `scipy.optimize.curve_fit` to estimate the amplitude of each decay component, representing the concentration of each molecule.  
4. Displays fitted amplitudes alongside their corresponding lifetimes for mixture analysis.  
5. Plots measured signals with their fitted multi-exponential curves to assess fitting quality.  
Uses `numpy`, `matplotlib`, `scipy`, and `struct`.

## 7. Parsing and Checking Chemical Equations

**File:** `parsing_equation.py`  
Automates the analysis and validation of chemical formulas and reaction equations using CSV input data and regular expressions.

1. Reads lists of chemical formulas and reaction equations from CSV files.  
2. **Formula Parsing:** Extracts elements and their subscripts from each molecular formula (e.g., `C2H5OH` → `C:2, H:6, O:1`) and identifies molecules matching specific criteria, such as containing 2 carbon and 5 hydrogen atoms.  
3. **Equation Balancing Check:** Splits chemical equations into reactants and products, parses each side, counts atoms for all elements, and verifies whether the equation is balanced. Reports the number of balanced equations in each input file (`balanceequation1.csv`, `balanceequation2.csv`).  
4. Prints results of parsing and balance checking for easy verification.  
Uses `re` and `csv` modules.
