from django.db import models

# Create your models here.

class usuario(models.Model):
	Id_usuario = models.CharField(primary_key=True,max_length=12,unique=True)
	password = models.CharField(max_length=25)	

class paciente(models.Model):
	id_paciente = models.CharField(primary_key=True, max_length=12, unique = True)
	Nombre = models.CharField(max_length = 35)
	Apellido = models.CharField(max_length = 35)
	EPS = models.CharField(max_length = 35)
	Genero = models.CharField(max_length = 35)
	Email = models.EmailField(max_length = 35)
	Municipio = models.CharField(max_length = 35)
	Edad = models.CharField (max_length =12)
	Estado_civil = models.CharField(max_length = 25)
	Telefono = models.CharField(max_length = 25)
	Direccion = models.CharField(max_length = 25)
	Religion = models.CharField(max_length = 25)
	Ocupacion = models.CharField(max_length = 25)
	Dia = models.CharField(max_length = 2)
	Mes = models.CharField(max_length = 2)
	Ano = models.CharField(max_length = 4)

	def __str__(self):
		return self.id_paciente + self.Nombre + self.Apellido + self.EPS + self.Genero + self.Municipio + self.Edad


class Motivo_consulta(models.Model):
	Id_Motivo = models.AutoField(primary_key = True, max_length = 35, unique = True)
	id_paciente = models.ForeignKey(paciente, null = False, blank = False)
	Motivo_consulta = models.CharField(max_length = 800)

class Enfermedad_Actual(models.Model):
	Id_Enfermedad = models.AutoField(primary_key = True, max_length = 35, unique = True)
	id_paciente = models.ForeignKey(paciente, null = False, blank = False)
	Enf_actual = models.CharField(max_length = 800)

class Gustos_preferencias(models.Model):
	Id_Gustos = models.AutoField(primary_key = True, max_length = 35, unique = True)
	id_paciente = models.ForeignKey(paciente, null = False, blank = False)
	Clima = models.CharField(max_length = 50)
	Temperatura = models.CharField(max_length = 50)
	Colores = models.CharField(max_length = 50)
	Numeros = models.CharField(max_length = 50)

class Examen_Fisico(models.Model):
	Id_examen = models.AutoField(primary_key = True, max_length = 35, unique = True)
	id_paciente = models.ForeignKey(paciente, null = False, blank = False)
	TA = models.CharField(max_length=50)
	FC = models.CharField(max_length=50)
	FR = models.CharField(max_length=50)
	Peso = models.CharField(max_length=50)
	Estatura = models.CharField(max_length=50)
	IMC = models.CharField(max_length=50)
	Perimetro_cintura = models.CharField(max_length=50)
	Pulso = models.CharField(max_length=50)
	Aspecto_general = models.CharField(max_length=50)
	Cabeza = models.CharField(max_length=50)
	Cavidad_oral = models.CharField(max_length=50)
	Cuello = models.CharField(max_length=50)
	Cardiopulmonar = models.CharField(max_length=50)
	Abdomen = models.CharField(max_length=50)
	Genitourinario = models.CharField(max_length=50)
	Osteomuscular = models.CharField(max_length=50)
	Piel = models.CharField(max_length=50)
	Neurologico = models.CharField(max_length=50)
	Extremidades = models.CharField(max_length=50)



class medidas_antropometricas(models.Model):
	Id_medidas = models.AutoField(primary_key = True, max_length = 35, unique = True)
	Id_examen = models.ForeignKey(Examen_Fisico, null = False, blank = False)
	Organo = models.CharField(max_length=50)
	Clasificacion = models.CharField(max_length=50)
	Especificacion = models.CharField(max_length=50)

class Diagnostico(models.Model):
	Id_diag_CIE10 = models.AutoField(primary_key = True, max_length = 35, unique = True)
	id_paciente = models.ForeignKey(paciente, null = False, blank = False)
	codigo= models.CharField(max_length=50)
	Nombre= models.CharField(max_length=50)
	Tipo= models.CharField(max_length=50)

class Resultado_Examen(models.Model):
	Id_resultado = models.AutoField(primary_key = True, max_length = 35, unique = True)
	id_paciente = models.ForeignKey(paciente, null = False, blank = False)
	Resultado= models.CharField(max_length=50)

class Terapias(models.Model):
	Id_terapia = models.AutoField(primary_key = True, max_length = 35, unique = True)
	id_paciente = models.ForeignKey(paciente, null = False, blank = False)
	Terapia= models.CharField(max_length=50)
	Estado= models.CharField(max_length=50)
	Especificaciones = models.CharField(max_length=50)

class Diagnosticos_propios(models.Model):
	Id_diagnostico = models.AutoField(primary_key = True, max_length = 35, unique = True)
	id_paciente = models.ForeignKey(paciente, null = False, blank = False)
	Nombre_diag= models.CharField(max_length=50)

class Antecedentes(models.Model):
	Id_antecedentes = models.AutoField(primary_key = True, max_length = 35, unique = True)
	id_paciente = models.ForeignKey(paciente, null = False, blank = False)
	Patologicos_medicamentos= models.CharField(max_length=50)
	Toxicos_alergicos= models.CharField(max_length=50)
	Quirurgicos= models.CharField(max_length=50)
	Trau_fisicos= models.CharField(max_length=50)
	Trau_emocionales= models.CharField(max_length=50)
	Habitos_saludables= models.CharField(max_length=50)
	Habitos_riesgo= models.CharField(max_length=50)
	Familiares= models.CharField(max_length=50)

class Plan_manejo(models.Model):
	Id_plan = models.AutoField(primary_key = True, max_length = 35, unique = True)
	id_paciente = models.ForeignKey(paciente, null = False, blank = False)
	Plan= models.CharField(max_length=50)
	Control= models.CharField(max_length=50)

class Rev_sistemas(models.Model):
	Id_revision = models.AutoField(primary_key = True, max_length = 35, unique = True)
	id_paciente = models.ForeignKey(paciente, null = False, blank = False)
	Rev_consulta= models.CharField(max_length=50)


class Paraclinicos(models.Model):
	id_paciente = models.ForeignKey(paciente, null = False, blank = False)
	Id_paraclinico = models.AutoField(primary_key = True, max_length = 35, unique = True)
	Diagnostico= models.CharField(max_length=500)
	Medicamentos= models.CharField(max_length=500)
	Incapacidad= models.CharField(max_length=500)
