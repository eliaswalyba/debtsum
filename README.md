# debtsum
**debtsum** is a command line utility for summarizing a debt file. The debt file must be in CSV format.

The input CSV should look like this:
```
Alex,Beatrice,101.32
Beatrice,Alex,1.20
Carl,Alex,45
Carl,Beatrice,12.50
Alex,Beatrice,19.22
Beatrice,Carl,67.90
Carl,Beatrice,12.80
Carl,Alex,15.88
Beatrice,Carl,71.42
Beatrice,Alex,4.54
Beatrice,Carl,28.76
```
The first line states that Alex owes Beatrice $101.32.

debtsum will output the following file as a result.
```
Alex,Beatrice,120.54
Beatrice,Alex,5.74
Beatrice,Carl,168.08
Carl,Alex,60.88
Carl,Beatrice,25.30
```

## Installation
To install this tool, you must have a version of [Python 3](https://docs.python.org/3/) installed with the associated package manager [pip](https://pip.pypa.io/en/stable/).
 Use pip to install **debtsum**.

```bash
pip install debtsum
```

## Usage
```bash
# summarize and output result to the default stdio
$ debtsum path/to/input.csv

# summarize and write the results to a csv file
$ debtsum path/to/input.csv -o path/to/output.csv
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Credit
debtsum is made with :heart: by [@eliaswalyba](https://twitter.com/eliaswalyba)
## License
[MIT](https://choosealicense.com/licenses/mit/)