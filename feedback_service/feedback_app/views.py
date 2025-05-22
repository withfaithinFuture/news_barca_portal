import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings


@csrf_exempt
def feedback_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            message = data.get('message')

            if not all([name, email, message]):
                return JsonResponse({'success': False, 'error': 'Все поля обязательны для заполнения'})

            telegram_message = (
                f"Новое сообщение с сайта FC Barcelona!\n\n"
                f"Имя: {name}\n"
                f"Email: {email}\n"
                f"Сообщение: {message}"
            )

            url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"
            payload = {
                'chat_id': settings.TELEGRAM_CHAT_ID,
                'text': telegram_message,
                'parse_mode': 'HTML'
            }

            response = requests.post(url, data=payload)
            response.raise_for_status()

            return JsonResponse({'success': True})

        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Неверный формат данных'})
        except requests.exceptions.RequestException as e:
            return JsonResponse({'success': False, 'error': f'Ошибка Telegram API: {str(e)}'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': f'Внутренняя ошибка сервера: {str(e)}'})
    return JsonResponse({'success': False, 'error': 'Метод не разрешен'}, status=405)
