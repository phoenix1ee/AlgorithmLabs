# Markov Chain Implementation

## The basic implementation: markovChain.py

This version reduce matrix by 1 row/column each time and stop when reduced matrix become 1x1.

### Usage is as below:
```commandline
usage: markovChain.py [-h] [-o] n_file

Find Markov Chain state probability: input an csv file represeting input state matrix

positional arguments:
  n_file      Input File containing the matrix

options:
  -h, --help  show this help message and exit
  -o          Optional, print the operation result to file
```

## The enhanced implementation: markovChainEnhanced.py

This version reduce matrix by 2 row/columns each time and stop when reduced matrix become either 1x1 or 2x2.

### Usage is as below:
```commandline
usage: markovChainEnhanced.py [-h] [-o] n_file

Find Markov Chain state probability: input an csv file represeting input state matrix

positional arguments:
  n_file      Input File containing the matrix

options:
  -h, --help  show this help message and exit
  -o          Optional, print the operation result to file
```