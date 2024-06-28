# APICalpar
API Calpar

## Requisitos

- Python 3.x
- Django
- Django Rest Framework
- requests
- drf-yasg
  
## Acesso remoto
1. Execute o servidor:
   https://web-production-1789d.up.railway.app/api/
   https://apicalpar.onrender.com/api/

3. Consuma a API e armazene os dados:
   https://web-production-1789d.up.railway.app/api/fetch-users/
   https://apicalpar.onrender.com/api/fetch-users/

5. Acesse a documentação da API em:

   RAILWAY
    - Swagger: `https://web-production-1789d.up.railway.app/swagger/`
    - Redoc: `https://web-production-1789d.up.railway.app/redoc/`
   
   RENDER
    - Swagger: `https://apicalpar.onrender.com/swagger/`
    - Redoc: `https://apicalpar.onrender.com/redoc/`
    
## Instalação local

1. Clone o repositório:
    ```bash
    git clone https://github.com/edson-cpp/APICalpar.git
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
