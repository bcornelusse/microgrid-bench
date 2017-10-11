Anaconda
========

1. Download and install [Anaconda](https://www.anaconda.com/download/) for Python 2.7 and your specific OS.
2. Create one environement for this assignement

```
conda create --name microgrid --file conda-{platform}.txt
```

where "{platform}" must matches your OS. Checkout [this reference](https://conda.io/docs/user-guide/tasks/manage-environments.html) for more information about how to manage Anaconda environments.

3. Activate the environement.

For Windows:
```
activate micrgrid # windows
```

For OSX and linux,
```
source activate micrgrid
```

4. Check if installation was done properly

```
python main.py
```
