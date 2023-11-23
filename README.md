# Atividade avaliativa grafo e analise de algoritimo
Código usados para a atividade avaliativa da materia de grafos e analise de algoritimos do IESB

## install dependencies:
to install the dependencies, run:
```bash
poetry install
```
## Analise de algoritimo:
To check the implementation of the buble sort and the quick sort methods, please check the directory [./SortMethods](./SortMethods).

After run the container, install the dependencies and activate the poetry venv, run the comparation between this two methods whith:
```bash
python compare_sort.py
```
### Results:
After the code finish, the graph will be saved on the folder [./results](./results)

## Test:
To test if the implementation is write, check the [./tests/test_sorted.py](./tests/test_sorted.py). To run the tests, run:
```bash
pytest -v ./tests
```

