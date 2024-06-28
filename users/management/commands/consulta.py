import requests
from django.core.management.base import BaseCommand
from users.models import User

class Command(BaseCommand):
    help = 'Busca usuários da API'

    def handle(self, *args, **kwargs):
        response = requests.get('https://09441c3d-9208-4fa9-a576-ba237af6b17c.mock.pstmn.io/')
        
        if response.json().get('Msg') != 'Sucesso ao Encontrar usuário.':
            self.stdout.write(self.style.ERROR('Erro ao consultar usuários'))
            return
        
        users_data = response.json().get('Dados', [])
        
        for user_data in users_data:
            User.objects.update_or_create(
                nome=user_data['Nome'],
                defaults={'disponivel': user_data['Disponivel']},
            )
        
        self.stdout.write(self.style.SUCCESS('Consulta executada com sucesso'))
