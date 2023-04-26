from django.db import connection,models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


class Grado(models.Model):
    nombre_grado = models.CharField(max_length = 45)
    class Meta:
        db_table = 'grado'        
        
# class Rol(models.Model):
#     nombre_rol = models.CharField(max_length = 45)
#     class Meta:
#         db_table = 'rol'

# class Estado(models.Model):
#     nombre_estado = models.CharField(max_length = 45)
#     class Meta:
#         db_table = 'estado'
        
class UsuarioManager(BaseUserManager):
    def create_user(self,email,username,nombres,apellidos,documento,password = None):
        if not email:
            raise ValueError("El usuario debe tener un email")
        
        usuario = self.model(
            username = username,
            email = self.normalize_email(email),
            nombres = nombres,
            apellidos = apellidos,
            documento = documento
        )
        
        usuario.set_password(password)
        usuario.save()
        return usuario
    
    def create_superuser(self,email,username,nombres,apellidos,documento,password):
        usuario = self.create_user(
            email,
            username = username,
            nombres = nombres,
            apellidos = apellidos,
            documento = documento , 
            password = password,
        )
        
        usuario.usuario_administrador =True
        usuario.save()
        return usuario
    
class Usuario(AbstractBaseUser):
    username = models.CharField('Nombre usuario', unique= True, max_length = 45)
    email = models.CharField('Correo',max_length = 45,unique= True) 
    nombres = models.CharField('Nombres',max_length = 45) 
    apellidos = models.CharField('Apellidos',max_length = 45) 
    documento = models.CharField('Numero de documento',max_length = 45)    
    usuario_activo = models.BooleanField(default=True)
    usuario_administrador = models.BooleanField(default=False)
    objects = UsuarioManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS =['email','nombres','apellidos','documento']
    
    def __str__(self):
        return f'{self.nombres},{self.apellidos},{self.email},{self.documento}'
    
    def has_perm(self,perm,obj = None):
        return True
    def has_module_perms(self,app,label):
        return True
    @property
    def is_staff(self):
        return self.usuario_administrador
    

class Grupo(models.Model):
    nombre_grupo = models.CharField(max_length = 45)
    codigo_grupo = models.CharField(max_length = 45)
    grado_id = models.ForeignKey(Grado, on_delete = models.CASCADE)
    usu_id = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    class Meta:
        db_table = 'grupo'