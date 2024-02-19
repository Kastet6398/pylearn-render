import traceback

from django.http import JsonResponse

from utils.calculator import calculate


def calculator(request):
    if request.method == 'POST':
        expression: str = request.POST.get('expression', '')

        result = "INTERNAL ERROR (500)"
        if 0 < len(expression) < 2048:
            try:
                result = calculate(expression)
            except (Exception,):
                traceback.print_exc()
        return JsonResponse({
            "result": result,
            "success": result != "INTERNAL ERROR (500)"
        })
    return JsonResponse({
        "error": "badRequestMethod",
        "success": False
    })
