# APICalpar
API Calpar

## Requisitos

- Python 3.x
- Django
- Django Rest Framework
- requests
- drf-yasg

## Instalação

1. Clone o repositório:
    ```bash
    git clone <repository-url>
    cd api_project
    ```

2. Crie um ambiente virtual e instale as dependências:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. Aplique as migrações do banco de dados:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4. Consuma a API e armazene os dados:
    ```bash
    python manage.py fetch_users
    ```

5. Execute o servidor:
    ```bash
    python manage.py runserver
    ```

6. Acesse a documentação da API em:
    - Swagger: `http://localhost:8000/swagger/`
    - Redoc: `http://localhost:8000/redoc/`
