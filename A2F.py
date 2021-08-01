#Dev by Chakal
import random
from colorama import Fore
import smtplib
import ssl
from os import system

def a2f():
    
# NE PAS TOUCHER :




    af = str(random.randint(100000, 999999))

    email = input("Veuillez renseignez votre email : ")

    smtp_address = 'smtp.gmail.com'
    smtp_port = 465
    
    
#   CE QUE TU PEUX EDIT
    
    
#   Email utilisé pour envoyé le code
    email_address = 'EMAIL'
    
    
#   Ton mot de passe d'application via ton email
    email_password = 'Mdp appli'
    email_receiver = email




# NE PAS TOUCHER :



    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_address, smtp_port, context=context) as server:
        server.login(email_address, email_password)
        server.sendmail(email_address, email_receiver, af)

    print()
    print()

    print(Fore.CYAN + "Un code vous a été envoyé a l'addresse suivante : " + email)

    print()

    reponse = input(Fore.WHITE + "Code reçu : ")
    print()

    if reponse == af:
        print(Fore.GREEN + "Code bon !")
    else:
        print(Fore.RED + "Code érroné !")
    print()
    back = input(Fore.WHITE + "Appuyez sur ENTRER pour retourner au menu.")
    
    if back == "":
        system("cls")
        main()



def main():
    mode = input(Fore.MAGENTA + """
    Dev by Chakal    
    
        
    #1 : Mon Github
    #2 : Ouvrir L'A2F
    #3 : Tuto pour config
    #4 : Quitter  
          
    [->] Choix : """)
    if mode == "1":
        system("start https://github.com/Chakal-1337")
        system("cls")
        main()
        
    if mode == "2":
        system("cls")
        a2f()
        
    if mode == "3":
        system("start https://youtu.be/fePMLuchNEY")
        system("cls")
        main()
    
    if mode == "4":
        quit()

main()
#Dev by Chakal