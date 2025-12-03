# humidification-system

Este repositório contém o Projeto de CPC.

Este README descreve os passos mínimos para configurar, executar e testar o projeto em Windows (PowerShell), usando o ambiente virtual fornecido em `.venv`.

Pré-requisitos
- Python 3.11 instalado (ou use o ambiente virtual incluído `.venv`).
- Git (opcional)

Rápido (se já houver `.venv` configurado)

1. Entre na pasta do projeto Django:

```powershell
cd C:\git_tiago_eletrotecnico\humidification-system\myproject
```

2. Ative o virtualenv (se não estiver ativado):

```powershell
. .venv\Scripts\Activate.ps1
```

3. Instale dependências (se não houver `requirements.txt`, instale Django):

```powershell
pip install -r ..\requirements.txt
# ou, se não existir requirements.txt:
pip install Django==5.2.9
```

4. Defina variáveis de ambiente (opcional):

Crie um arquivo `.env` ou exporte as variáveis no seu ambiente. Exemplo de `.env` (coloque em `myproject/`):

```
SECRET_KEY=uma_chave_secreta_aqui
DEBUG=True
```

O `settings.py` usa `os.getenv()` e tem valores padrão seguros para desenvolvimento, portanto você pode pular esse passo em ambiente local se preferir.

5. Criar e aplicar migrations:

```powershell
python manage.py makemigrations
python manage.py migrate
```

6. Criar superuser para acessar o admin:

```powershell
python manage.py createsuperuser
```

7. Rodar o servidor de desenvolvimento (porta 9000 neste guia):

```powershell
python manage.py runserver 9000
```

Pontos de acesso úteis
- Admin: `http://127.0.0.1:9000/admin/` (faça login com o superuser criado)
- Endpoint da app `umidade` para receber telemetria (POST JSON):
	- `http://127.0.0.1:9000/api/umidade/receber/`

Exemplo de payload (curl / PowerShell):

- curl (Linux/macOS/curl.exe):

```bash
curl -X POST -H "Content-Type: application/json" \
 -d '{"nivel_agua_baixo": false, "umidade": 42.5, "violacao_geral": false}' \
 http://127.0.0.1:9000/api/umidade/receber/
```


O que a API retorna
- Ao enviar um POST válido, o endpoint cria um objeto `Telemetria` e retorna um JSON com os campos:
	- `id`, `timestamp`, `umidade`, `setpoint`, `sistema_ativo`, `atuando`, `nivel_agua_baixo`, `violacao_geral`, `alarme`.

Como configurar o setpoint
- O setpoint é gerenciado via modelo `Configuracao` acessível pelo Django Admin. Após criar o superuser, abra `/admin/` e edite/crie uma `Configuração` para ajustar o `setpoint` usado quando a telemetria é recebida.

Estrutura importante do projeto
- `myproject/` — pasta do projeto Django (contém `manage.py`)
- `myproject/myproject/settings.py` — configurações do Django (leitura de `SECRET_KEY` via `os.getenv`)
- `myproject/umidade/` — app com `models.py`, `views.py`, `urls.py` e `admin.py`