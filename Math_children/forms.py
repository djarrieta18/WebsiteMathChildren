from django import forms
from Math_children.models import Usuario    


class formularioUsuario(forms.ModelForm):
    """Formulario de registro de un usuario en el sistema
    
    variables:
       - password1: contraseña
       - password2: verificacion de la contraseña
        
    """
    password1 = forms.CharField(label='Contraseña', widget= forms.PasswordInput(
        attrs={
            'class':'controls',
            'placeholder':'Ingrese su contraseña',
            'id': 'password1',
            'required': 'required',
        }
    ))
    password2 = forms.CharField(label='Contraseña de confirmacion', widget= forms.PasswordInput(
        attrs={
            'class':'controls',
            'placeholder':'ingrese nuevamente su contraseña...',
            'id': 'password2',
            'required': 'required',
        }
    ))
       
    class Meta:
        model = Usuario
        fields = ('username','email','nombres','apellidos','documento')
        widgets ={
            
            'username': forms.TextInput(
                attrs={
                    'class': 'controls',
                    'placeholder':'Ingrese su nombre de usuario',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'controls',
                    'placeholder':'Correo electronico',
                }
            ),
            'nombres': forms.TextInput(
                attrs={
                    'class': 'controls',
                    'placeholder':'Ingrese sus nombres',
                }
            ),
            'apellidos': forms.TextInput(
                attrs={
                    'class': 'controls',
                    'placeholder':'Ingrese sus apellidos',
                }
            )
            ,
            'documento': forms.TextInput(
                attrs={
                    'class': 'controls',
                    'placeholder':'Ingrese su numero de documento',
                }
            )
        }