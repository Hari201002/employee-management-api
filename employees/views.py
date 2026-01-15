from rest_framework import generics, status
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeListCreateView(generics.ListCreateAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        qs = Employee.objects.all()
        department = self.request.query_params.get('department')
        role = self.request.query_params.get('role')
        if department:
            qs = qs.filter(department=department)
        if role:
            qs = qs.filter(role=role)
        return qs

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class EmployeeRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT)
