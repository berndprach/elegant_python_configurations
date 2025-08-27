
# Elegant Python Configuration
Code for our blog post [Elegant Python Configurations]().

## Description

This code allows defining configuration as `dataclasses` 
in a simple, readable way that also allows typing.
See [main.py](main.py).

It also allows creating instances based on command line arguments 
(and the help of argparse), by creating a parser based on the
dataclass. See [parsing.py](parsing.py).

## Usage 
We can use this configuration based on command line arguments,
but we can also initiate it directly. This is very helpful e.g.
for unit tests. 

Try it out:
```
>> python main.py --dataset_name="1." --optimizer_name ADAM
>> python unittest.py
```


