import EmployeeApp
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Departments, Employees
from EmployeeApp.serializers import DepartmentSerializer, EmployeeSerializer

from django.core.files.storage import default_storage

# Create your views here.
@csrf_exempt
def departmentApi(request, id=0):
    if request.method == "GET":
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)

    elif request.method == "POST":
        departments_data = JSONParser().parse(request)
        departments_serializer = DepartmentSerializer(data=departments_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Agregado exitosamente", safe=False)
        return JsonResponse("Error en agregarlo", safe=False)

    elif request.method == "PUT":
        departments_data = JSONParser().parse(request)
        department = Departments.objects.get(
            DepartmentId=departments_data["DepartmentId"]
        )
        departments_serializer = DepartmentSerializer(department, data=departments_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Actualizado exitosamente", safe=False)
        return JsonResponse("Fallo al actualizar", safe=False)

    elif request.method == "DELETE":
        department = Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Departamento eliminado exitosamente", safe=False)


@csrf_exempt
def EmployeeApi(request, id=0):
    if request.method == "GET":
        employee = Employees.objects.all()
        employee_serializer = EmployeeSerializer(employee, many=True)
        return JsonResponse(employee_serializer.data, safe=False)

    elif request.method == "POST":
        employee_data = JSONParser().parse(request)
        employee_serializer = EmployeeSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Agregado exitosamente", safe=False)
        return JsonResponse("Error en agregarlo", safe=False)

    elif request.method == "PUT":
        employee_data = JSONParser().parse(request)
        employee = Employees.objects.get(EmployeeId=employee_data["EmployeeId"])
        employee_serializer = EmployeeSerializer(employee, data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Actualizado exitosamente", safe=False)
        return JsonResponse("Fallo al actualizar", safe=False)

    elif request.method == "DELETE":
        employee = Employees.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Departamento eliminado exitosamente", safe=False)


@csrf_exempt
def saveFile(request):
    file = request.FILES["uploadedFile"]
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)
