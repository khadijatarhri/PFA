from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer , NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note


# myapp/views.py
from django.shortcuts import render
from django.http import JsonResponse

"""def detect_sensitive_info(request):
    if request.method == "POST":
        user_input = request.POST.get("user_input", "")  # Récupère le texte soumis par l'utilisateur
        results = detect_sensitive_data(user_input)  # Analyser le texte avec Presidio

        # Créer une réponse JSON avec les résultats
        return JsonResponse({"sensitive_data": [res.to_dict() for res in results]})


    return render(request, "detect_input.html")"""

# Create your views here.
# views.py
from .presidio_service import detect_sensitive_data, anonymize_text

def detect_sensitive_info(request):
    if request.method == "POST":
        user_input = request.POST.get("user_input", "")
        step = request.POST.get("step", "detect")  # Par défaut on est dans l'étape d'analyse

        if step == "detect":
            results = detect_sensitive_data(user_input)
            entity_types = list(set([res.entity_type for res in results]))
            return render(request, "detect_input.html", {
                "user_input": user_input,
                "step": "select_entities",
                "entities": entity_types
            })

        elif step == "anonymize":
            selected_entities = request.POST.getlist("selected_entities")
            anonymized_text = anonymize_text(user_input, selected_entities)
            return render(request, "detect_input.html", {
                "anonymized_text": anonymized_text,
                "user_input": user_input,
                "selected_entities": selected_entities,
                "step": "result"
            })

    return render(request, "detect_input.html")


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]