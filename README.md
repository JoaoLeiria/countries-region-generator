# countries-region-generator
Python script that generates a JSON with a list of countries and it's regions.
To generate the JSON the script uses as input the countries.json file and combines it with the info in [rescountries.eu](https://restcountries.eu/rest/v2/alpha/) API

### Installation

Tested using [Python](https://www.python.org/) 2.7.12.
Please refer [restcountries api](https://restcountries.eu/) if you wish to change the script to add/remove fields in the script.

```sh
$ git clone https://github.com/JoaoLeiria/countries-region-generator
$ cd countries-region-generator
$ python run.py
```
The generated data will be saved in the generated_data.json file.

### Add/Remove fields (e.g: adding the languages field)
```javascript
country['languages'] = auxInfo['languages']
```
The example object of the available fields is in: https://restcountries.eu/#api-endpoints-response-example


### Todos

 - Add more flexibility to the script (dynamic fields and output file through the command line)

License
----

MIT
