### Install Requirements
`python3 -m pip install -p requirements.txt`

### Usage

#### Arguments
#### `-f <file-name>`
Use to give multiple RefSeq numbers listed in `<file-name>`. <br>
Example RefSeq list file: <br>
```
NP_040831.1
NP_000591.1
NP_003451.1
NP_103451.1
NP_003001.1
```

#### `-p <refseq-number>`
Use to give a single RefSeq number.


#### Optional Arguments
#### `--fasta-file <file-name>`
Use to specify stored .fasta file name. <br>
Stored .fasta file name will be the date-time of execution if a file name is not specified.

#### `--output-file <file-name>`
Use to specify an output file. <br>
Results will be written only to terminal if an output file name is not specified.
