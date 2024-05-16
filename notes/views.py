from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Note
from .serializers import NoteSerializer

class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        
        if check := self.request.query_params.get('check'):
            if check.lower() == 'true':
                return Note.objects.filter(user=self.request.user, checked=True).order_by('date')
            else:
                return Note.objects.filter(user=self.request.user, checked=False).order_by('date')
        else:
            return Note.objects.filter(user=self.request.user).order_by('date')
        
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
