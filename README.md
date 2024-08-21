# simple chatbot

> Este é um chatbot simples feito em python

- Faça cópia do arquivo .env.example para .env
  troque 'the_api_key_value_her' pela sua API KEY

```sh
sed 's/my_api_key/the_api_key_value_here/g .env.example > .env
```

- Criar o ambiente virtual

```sh
python -m venv env
```

- Ativar o ambiente (após ativar o ambiente, verá o nome do ambiente entre parênteses no início da linha de comando)

```sh
source env/bin/activate
```

- Desativar o ambiente

```sh
deactivate
```

- Registrar as dependências do projeto

```sh
pip freeze > requirements.txt
```

- Instalar as dependências

```sh
pip install -r requirements.txt
```

- Criar gitignore

```sh
npx gitignore python
```

[**Diorgenes Morais**](https://github.com/diorgenesmorais)
