# Awesome Linear Regression
![Awesome Linear Regression](https://github.com/somkietacode/Awesome_Linear_Regression/blob/main/image/alr.png?raw=true)
Linear regression attempts to model the relationship between variables by fitting a linear equation to observed data. 
This repository hosts the development of the Awesome Linear Regression library.

## About Awesome Linear Regression

Awesome Linear Regression , is a mathematics API written in Python.
It was developed with a focus on enabling fast experimentation.
*Being able to go from idea to result as fast as possible is key to doing good research.*

Awesome Linear Regression is:

-   **Simple** 
-   **Flexible** 
-   **Powerful** 

## First contact with Awesome Linear Regression

The core data structures of Awesome Linear Regression are __consign__ and __result__.

For installation run :

```
pip install Awesome-Linear-Regression

```

Here is an `exemple` :

```python
from Awesome_Linear_Regression import linearregression as LR
import pandas as pd
import numpy as np

# Sample training data set

x = np.matrix([[0,1],[1,4],[7,8],[50,23]])
y = np.matrix([[2],[9],[23],[96]])

# Train the model

Lr = linearregression(x,y)
Beta, rss = Lr.leastsquare()


```

Let make prediction

```python

 px = np.matrix([[4,7]])
 print(Lr.predict(px))

```

---
## Support

You can ask questions and join the development discussion:

- [Facebook page](https://www.facebook.com/globalanalysistech) .

---
