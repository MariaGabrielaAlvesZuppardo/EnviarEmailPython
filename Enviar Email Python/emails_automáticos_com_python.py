# -*- coding: utf-8 -*-
"""Emails Automáticos com Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18UxeaLdUFFZ3NoGMp7D8AxNDR4BqviYT

# **Email Automático com Python**

Este é um documento que mostra aplicações para enviar e-mails automáticamente usando a biblioteca '**smptlib'**. Este primeiro mostra uma aplicação para o envio de email automático via python. A biblioteca '**smptlib'** já é instalada no Python, só precisamos importa-lá não baixada.
"""

import smtplib
import email.message

def enviar_email():
  corpo_email="""
  <p>Prezados, </p>
  <p>The code is running</p>
  """

  msg=email.message.Message()
  msg['Subject']="Assunto"
  msg['From']="Email do Remetente"
  msg['To'] = "Email do Destinatário"
  password = "Senha gerada pelo Gmail através do email do remetente"  # senha do email do remetente / gerada pelo google
  msg.add_header('Content-Type', 'text/html')
  msg.set_payload(corpo_email)

  s=smtplib.SMTP('smtp.gmail.com:587')
  s.starttls()
  #Login Credentials for send mail
  s.login(msg['From'],password)
  s.sendmail(msg['From'],[msg['To']],msg.as_string().encode('utf-8'))
  print('Email enviado')

enviar_email()

"""## *Gerando a senha para Apps do Google*





*   Acesse a página de segurança da sua conta do Google: https://myaccount.google.com/security
*   Role para baixo até encontrar a seção "Acesso a apps menos seguros".
*   Ative a opção "Permitir o acesso a apps menos seguros".
*   Escolha "Outro (Personalizado)" como o tipo de aplicativo.
*   Dê um nome ao seu aplicativo (por exemplo, "Enviador de E-mails Python").
*   O Google gerará uma senha de aplicativo para você. Anote essa senha.






"""