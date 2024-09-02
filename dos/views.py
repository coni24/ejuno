from django.shortcuts import render
from django.http import HttpResponse


def display(request):
 return HttpResponse("""
            <form>
                <h1>Formulario</h1>
                <label for='nombre'>Nombre:</label>
                <input type='text' id='nombre' name='nombre'><br><br>
                <label for='apellido'>Apellido:</label>
                <input type='text' id='apellido' name='apellido'><br><br>
                <label for='correo'>Correo:</label>
                <input type='text' id='correo' name='correo'><br><br>
                <input type='submit' value='Enviar'>
            </form>
        """)