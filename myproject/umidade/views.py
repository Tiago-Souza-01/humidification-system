import json
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from .models import Telemetria, Configuracao


def _get_current_setpoint():
    cfg = Configuracao.objects.first()
    return cfg.setpoint if cfg else 50.0


@csrf_exempt
def receber_telemetria(request):
    if request.method != 'POST':
        return HttpResponseBadRequest('Use POST')

    try:
        payload = json.loads(request.body)
    except Exception:
        return HttpResponseBadRequest('JSON inválido')

    try:
        nivel_agua_baixo = bool(payload.get('nivel_agua_baixo', False))
        umidade = float(payload.get('umidade'))
        violacao_geral = bool(payload.get('violacao_geral', False))
        sistema_ativo = bool(payload.get('sistema_ativo'))
        atuando = bool(payload.get('atuando'))
        alarme = bool(payload.get('alarme'))

    except Exception:
        return HttpResponseBadRequest('Campos faltando ou inválidos')

    setpoint = _get_current_setpoint()

    t = Telemetria.objects.create(
        umidade=umidade,
        setpoint=setpoint,
        sistema_ativo=sistema_ativo,
        atuando=atuando,
        nivel_agua_baixo=nivel_agua_baixo,
        violacao_geral=violacao_geral,
        alarme=alarme,
    )

    data = {
        'id': t.id,
        'timestamp': t.timestamp.isoformat(),
        'umidade': t.umidade,
        'setpoint': t.setpoint,
        'sistema_ativo': t.sistema_ativo,
        'atuando': t.atuando,
        'nivel_agua_baixo': t.nivel_agua_baixo,
        'violacao_geral': t.violacao_geral,
        'alarme': t.alarme,
    }

    return JsonResponse(data)
