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
        
    def clean_password2(self):
        """ Validacion de contrasena
        Este es el metodo que valida que ambas contrasenas sean correctas, esto antes de ser encriptadas
        y guardadas en la base de datos, Retorna la contrasena valida.
        
        Excepciones:
        -ValidationError --cuando las contraseñas no son iguales muestra un error
        """
        print(self.cleaned_data)
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Contraseñas no coinciden!')
        return password2

    def save(self,commit = True):
        user = super().save(commit = False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
        
    

