# MedicaApp
Aplicação desenvolvida em DjangoREST.

Para detalhes do Desafio Segue o link [link](https://github.com/Intmed-Software/desafio).

#### Requisitos

 - Python 3 
- Venv
 - Django
 - Django Rest Framework

#### Instruções para execução da aplicação
#### Instruções para executar via virtual env
Após clonar o projeto, entre na pasta  e execute os seguintes comandos:

      #cria o ambiente virtual
      python -m venv venv
	  
	  #ativa o ambinente (Windows - Powershell)
	  .\venv\Scripts\activate.ps1
	  
	  #caso o Powershell nao execute o script  abra o powershell com opções de admin e execute o seguinte comando 
	  set executionpolicy unrestricted

	  #seleciona 'S', aperte enter e execute o script activate novamente
	  
	  #instale as dependências (Windows - Powershell)
	  python -m pip install -r requirements.txt
	  
	  #Django - Rodando o projeto (Windows - Powershell)
	  python .\manage.py makemigrations
	  python .\manage.py migrate
	  python .\manage.py runserver
	   
## Backend - Django REST

### Estrutura 
O projeto foi dividido de forma que cada app seja uma etapa do gerenciamento das consultas, os app's são:

- doctor (Médico);
- patient (Usuário);
- diaryDoctor (Agenda);
- queryPatient (Consulta);

### Endpoints
Os endpoints estão de acordo com o proposto no desafio, sem authentication  e a interface administrativa com as funcionalidades definidas.
Tendo em vista que:
- As viewsets e serializers estão dentro da pasta api em seus respectivos App’s.
- No App ‘doctor’ (models) temos os atributos:
    * doctor (Indica o nome do médico)
    * crm (Indica o crm do médico)
    * mail (Indica o e-mail do médico)
	
- No App ‘diaryDoctor’ (models) temos os atributos:
    * doctor (Indica as informações do médico)
    * day (Indica a data da agenda do médico)
    * freeDay (Indica se aquela data está disponível ou não)
    * hour (Indica os horários da agenda do médico)
    * freeHour (Indica se aquele horário está disponível ou não)
	
- No App ‘queryPatient’ (models)  temos os atributos:
    * doctor (Indica as informações do médico)
    * diary (Indica as informações da agenda)
    * patient (Indica as informações do usuário)
    * hour (Indica os horário da consulta)
    * daySchedule (Indica a data que a consulta foi marcada)

### Ações da aplicação

A aplicação possui as seguintes Ações:
- Cadastrar médicos
- Criar agenda para médicos
- Listar agendas disponíveis
- Marcar consulta (Falta)
- Desmarcar consulta (Falta)

## OBS
