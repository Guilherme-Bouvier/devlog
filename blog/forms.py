from django import forms
from .models import MensagemContato


class ContatoForm(forms.ModelForm):

    class Meta:
        model = MensagemContato

        fields = [
            'nome',
            'email',
            'mensagem'
        ]

        labels = {
            'nome': 'Nome completo',
            'email': 'E-mail',
            'mensagem': 'Mensagem'
        }

        widgets = {

            'nome': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Digite seu nome'
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Digite seu e-mail'
                }
            ),

            'mensagem': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Digite sua mensagem',
                    'rows': 5
                }
            ),
        }