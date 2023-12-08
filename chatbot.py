
def administrar_chatbot(text):
    global tutor
    global sesion_number
    global selected_option_details
    global selected_option_details_tutor
    global numero_opcion
    text = text.lower() #mensaje usuario
    list = []
    print("texto:",text)

    if "hola" in text:
        body = "Hola bienvenido a tutoria UC"
        footer='elige una de las siguienstes opciones'
        options=["Acceder cuenta", "FAQ","Dejar tu Opinión"]
        # list.append(replyReaction)
        # list.append(replyButtonData)

    elif "acceder cuenta" in text:
        body = "Tienes cuenta Wenet?"
        footer='Elegi la opcion correcta'
        options=["Si tengo cuenta", "No tengo cuenta"]

        # replyButtonData = buttonReply_Message(number, options, body, footer, "sed2", messageId)
        # replyReaction = replyReaction_Message(number, messageId, "😀")
        # list.append(replyReaction)
        # list.append(replyButtonData)
    elif "si tengo cuenta" in text:
        pass
        # textMessage = text_Message(number, "Ingrese su numero de telefono asociado a su cuenta de wenet \n ejemplo: 0981696969 o 0216161000")
        # replyReaction = replyReaction_Message(number, messageId, "😀")
        # list.append(replyReaction)
        # list.append(textMessage)

    elif "no tengo cuenta" in text:
        pass
        # textMessage = text_Message(number, "Necesitas una cuenta de Wenet para acceder a los servicios de la tutoria, puede crear una cuenta en el siguiente link:\n\n www.wenet.com/crearcuenta")
        # replyReaction = replyReaction_Message(number, messageId, "😀")
        # list.append(replyReaction)
        # list.append(textMessage)

    elif "any(number in text for number in numbers)":
        pass
        # # Encuentra el número de teléfono correspondiente
        # matching_number = next((number for number in numbers if number in text), None)
        # # Verifica que se haya encontrado un número correspondiente
        # if matching_number is not None:
        #     sesion_number = matching_number
        #     # Llama a la función para obtener los datos del alumno
        #     nombre, apellido = db.obtener_datos_alumno(matching_number)

        #     # Construye el mensaje de saludo
        #     if nombre and apellido:
        #         greeting_message = f"Hola {nombre} {apellido}"
        #     else:
        #         greeting_message = "Hola"

        #     body = greeting_message
        #     footer='selecciona como ingresar'
        #     options=["Soy Tutor", "Soy Alumno"]
        #     replyButtonData = buttonReply_Message(number, options, body, footer, "sed4", messageId)
        #     replyReaction = replyReaction_Message(number, messageId, "😀")
        #     list.append(replyReaction)
        #     list.append(replyButtonData)
    elif "":
        pass
        #     # Número no encontrado, manejar según sea necesario
        #     textMessage = text_Message(number, "Número de teléfono no reconocido. Por favor, inténtalo de nuevo.")
        #     list.append(textMessage)
    elif "tutoria disponible" in text:
        pass
    #     # Call the function to get tutorias disponibles
    #     tutorias_disponibles = db.vertutorias_disponibles()
    #     print(tutorias_disponibles)

    #     # Check if there are available tutorias
    #     if tutorias_disponibles:
    #         # Initialize a dictionary to store id_solicitud values
    #         id_solicitudes_dict = {}

    #         # Initialize the list to store options
    #         options = []

    #         # Assuming tutorias_disponibles is a list of dictionaries with keys 'id_solicitud', 'genero_alumno', 'puntaje_alumno', and 'nombre_materia'
    #         for i, tutoria in enumerate(tutorias_disponibles):
    #             id_solicitud = tutoria.get('id_solicitud', 'Id Solicitud No Disponible')
    #             genero_alumno = tutoria.get('genero_alumno', 'Genero No Disponible')
    #             puntaje_alumno = tutoria.get('puntaje_alumno', 'Puntaje No Disponible')
    #             nombre_materia = tutoria.get('nombre_materia', 'Materia No Disponible')

    #             # Store the id_solicitud in the dictionary
    #             id_solicitudes_dict[f"Alumno Opcion {i+1}"] = id_solicitud

    #             # Construct the text message for each tutoria
    #             text_message = f"Genero: {genero_alumno}\nPuntaje: {puntaje_alumno}\nMateria Solicitada: {nombre_materia}"

    #             # Create and append the text message
    #             textMessage = text_Message(number, text_message)
    #             list.append(textMessage)

    #             # Add the option for the current tutoria
    #             options.append(f"Alumno Opcion {i+1}")

    #         # Add the "No me gusta ninguna" option
    #         options.append("No me gusta ninguna")

    #         # Construct the body and footer
    #         body = "por favor seleccione una opción para continuar"
    #         footer = ""

    #         # Add the reply reaction
    #         replyReaction = replyReaction_Message(number, messageId, "😀")
    #         list.append(replyReaction)

    #         # Add the list reply data
    #         listReplyData = listReply_Message(number, options, body, footer, "sed2", messageId)
    #         list.append(listReplyData)

    #         # Add the sticker
    #         sticker = sticker_Message(number, get_media_id("perro_traje", "sticker"))
    #         list.append(sticker)

    #         # Add the reply reaction again
    #         list.append(replyReaction)

    #         # Save id_solicitudes_dict for later use (based on the user's selection)
    #         # You can access the selected id_solicitud using id_solicitudes_dict[selected_option]
    #         selected_option_details = id_solicitudes_dict

    # # Later in your code, when you need to retrieve the selected option details
    # # (e.g., after the user selects an option):
    # # selected_option = selected_option_details.get("selected_option", None)
    elif "alumno opcion" in text:
        pass
        # numero_opcion = int(text.split()[-1])
        # body = "estas seguro que quieres ser Tutor"
        # footer='selecciona '
        # options=["si quiero", "no quiero"]
        # replyButtonData = buttonReply_Message(number, options, body, footer, "sed12", messageId)
        # list.append(replyButtonData)
        # replyReaction = replyReaction_Message(number, messageId, "😀")
        # list.append(replyReaction)
    elif "si quiero" in text:
        pass
        # print(selected_option_details)
        # nombre_opcion = f"Alumno Opcion {numero_opcion}"
        # id_solicitud = selected_option_details.get(nombre_opcion)
        # print(id_solicitud)
        # # Call the function to get details of the accepted tutoria
        # tutoria_details = db.TutoriaAceptada(id_solicitud,sesion_number)
        # print(tutoria_details)
        # if tutoria_details:
        #     # Extract details from the tutoria_details
        #     alumno_nombre = tutoria_details.get('nombre', 'Nombre No Disponible')
        #     alumno_apellido = tutoria_details.get('apellido', 'Apellido No Disponible')
        #     alumno_numero_telefono = tutoria_details.get('numero_celular', 'Número de Teléfono No Disponible')

        #     # Construct the text message with the retrieved details
        #     text_message = f"Perfecto, el estudiante es {alumno_nombre} {alumno_apellido}. Número de Teléfono: {alumno_numero_telefono}. Por favor, ponerse en contacto con él alumno."

        #     # Create and append the text message
        #     textMessage = text_Message(number, text_message)
        #     list.append(textMessage)
        # else:
        #     # Handle the case where tutoria_details is not available
        #     textMessage = text_Message(number, "Lo siento, no se pudieron obtener los detalles de la tutoría aceptada.")
        #     list.append(textMessage)
    elif "no quiero" in text:
        pass
        # textMessage = text_Message(number,"Ok comprendible")
        # list.append(textMessage)
    elif "volver menu tutor" in text:
        pass
        # tutor = True
        # body = "porfavor selecione una opcion para continuar"
        # footer = "para volver cuando quieras escriba 'volver menu tutor'"
        # options = ["Ver Perfil", "Editar perfil", "Editar Materia Inscripta", "Ver historial", "Tutoria Disponible"]

        # replyReaction = replyReaction_Message(number, messageId, "😀")
        # list.append(replyReaction)
        # listReplyData = listReply_Message(number, options, body, footer, "sed2",messageId)
        # sticker = sticker_Message(number, get_media_id("perro_traje", "sticker"))
        # list.append(listReplyData)
        # list.append(sticker)
    elif "ver perfil" in text:
        pass
        # alumno_perfil = db.ver_perfil(sesion_number)
        # print(alumno_perfil)
        # if tutor:
        #   text_message = (
        #       f"Te presentamos los datos personales que tenemos registrados en tu perfil:\n\n"
        #       f"Nombre: {alumno_perfil['nombre']} {alumno_perfil['apellido']}\n"
        #       f"Correo: {alumno_perfil['email']}\n"
        #       f"Puntaje como tutor: {alumno_perfil['puntaje_tutor']}\n"
        #       f"Género: {alumno_perfil['genero']}"
        #       f"para volver atras escribe 'volver menu tutor'"
        #   )
        # else:
        #   text_message = (
        #       f"Te presentamos los datos personales que tenemos registrados en tu perfil:\n\n"
        #       f"Nombre: {alumno_perfil['nombre']} {alumno_perfil['apellido']}\n"
        #       f"Correo: {alumno_perfil['email']}\n"
        #       f"Puntaje como tutor: {alumno_perfil['puntaje_tutor']}\n"
        #       f"Género: {alumno_perfil['genero']}\n"
        #       f"para volver atras escribe 'volver menu alumno'"
        #   )
        # textMessage = text_Message(number, text_message)
        # list.append(textMessage)
    elif "editar perfil" in text:
        pass
        # student_id = db.editar_perfil(sesion_number)
        # print(tutor)
        # if student_id is not None:
        #   if tutor:
        #       textMessage = text_Message(number, f"Para editar tu cuenta haz clic en el siguiente enlace:\n\n www.wenet.com/tutoriaUC/editarcuenta/{student_id}\n\nEscribe 'volver al menu tutor' para regresar al menú principal.")
        #   else:
        #       textMessage = text_Message(number, f"Para editar tu cuenta haz clic en el siguiente enlace:\n\n www.wenet.com/tutoriaUC/editarcuenta/{student_id}\n\nEscribe 'volver al menu alumno' para regresar al menú principal.")
        #   list.append(textMessage)
        # else:
        #   # Handle the case where the student is not found
        #   textMessage = text_Message(number, "No se encontró el estudiante asociado al número de teléfono.")
        #   list.append(textMessage)
    elif "editar materia inscripta" in text:
        pass
        # student_id = db.editar_perfil(sesion_number)
        # if student_id is not None:
        #   textMessage = text_Message(number, f"Para Materias Inscritas como Tutor haz clic en el siguiente enlace: \n\n www.wenet.com/tutoriaUC/editarmaterias/{student_id}\n\nEscribe 'volver al menu tutor' para regresar al menú principal.")
        #   list.append(textMessage)
        # else:
        #   # Handle the case where the student is not found
        #   textMessage = text_Message(number, "No se encontró el estudiante asociado al número de teléfono.\n\nEscribe 'volver al menu tutor' para regresar al menú principal.")
        #   list.append(textMessage)
    elif "pedir una tutoria" in text:
        pass
        # textMessage = text_Message(number, "Por favor ingrese el nombre de la materia para continuar.\n ejemplo: Ingenieria de Software 1")
        # list.append(textMessage)
    elif "any(text == name.lower() for name in materias)":
        pass
        # name=text.lower()
        # # Call the function to get tutorias disponibles
        # tutorias_disponibles = db.buscarTutores(name)
        # print(tutorias_disponibles)

        # # Check if there are available tutorias
        # if tutorias_disponibles:
        #     # Initialize a dictionary to store id_solicitud values
        #     id_materias_dict = {}

        #     # Initialize the list to store options
        #     options = []

        #     # Assuming tutorias_disponibles is a list of dictionaries with keys 'id_solicitud', 'genero_alumno', 'puntaje_alumno', and 'nombre_materia'
        #     for i, tutoria in enumerate(tutorias_disponibles):
        #         id_materia = tutoria.get('id_materia', 'Id Materia No Disponible')
        #         genero_alumno = tutoria.get('genero_alumno', 'Genero No Disponible')
        #         puntaje_alumno = tutoria.get('puntaje_alumno', 'Puntaje No Disponible')

        #         # Store the id_solicitud in the dictionary
        #         id_materias_dict[f"Tutor Opcion {i+1}"] = id_materia

        #         # Construct the text message for each tutoria
        #         text_message = f"Genero: {genero_alumno}\nPuntaje: {puntaje_alumno}\n"

        #         # Create and append the text message
        #         textMessage = text_Message(number, text_message)
        #         list.append(textMessage)

        #         # Add the option for the current tutoria
        #         options.append(f"Tutor Opcion {i+1}")

        #     # Add the "No me gusta ninguna" option
        #     options.append("No me gusta ninguna")

        #     # Construct the body and footer
        #     body = "por favor seleccione una opción para continuar"
        #     footer = ""

        #     # Add the reply reaction
        #     replyReaction = replyReaction_Message(number, messageId, "😀")
        #     list.append(replyReaction)

        #     # Add the list reply data
        #     listReplyData = listReply_Message(number, options, body, footer, "sed2", messageId)
        #     list.append(listReplyData)

        #     # Add the sticker
        #     sticker = sticker_Message(number, get_media_id("perro_traje", "sticker"))
        #     list.append(sticker)

        #     # Add the reply reaction again
        #     list.append(replyReaction)

        #     # Save id_materias_dict for later use (based on the user's selection)
        #     # You can access the selected id_solicitud using id_materias_dict[selected_option]
        #     selected_option_details_tutor = id_materias_dict

    # Later in your code, when you need to retrieve the selected option details
    # (e.g., after the user selects an option):
    # selected_option = selected_option_details.get("selected_option", None)
    elif "tutor opcion" in text:
        pass
        # numero_opcion = int(text.split()[-1])
        # textMessage = text_Message(number, "Perfecto se le enviara una notificacion al Tutor")
        # list.append(textMessage)
    elif "no me gusta" in text:
        pass 
        # textMessage = text_Message(number, "Ok")
        # list.append(textMessage)
    elif "notificacion" in text:
        pass
        # textMessage = text_Message(number, "Hola Juanjo Bai, alguien solicito tu ayuda para la materia ingenieria de software")
        # list.append(textMessage)
        # body = "seleciona una de las opciones"
        # footer='selecciona '
        # options=["Si quiero ser Tutor", "No quiero ser Tutor"]
        # replyButtonData = buttonReply_Message(number, options, body, footer, "sed14", messageId)
        # list.append(replyButtonData)
        # replyReaction = replyReaction_Message(number, messageId, "😀")
        # list.append(replyReaction)
    elif "si quiero ser tutor" in text:
        pass
        # print(selected_option_details_tutor)
        # nombre_opcion = f"Alumno Opcion {numero_opcion}"
        # id_materia = selected_option_details.get(nombre_opcion)
        # print(id_materia)
        # # Call the function to get details of the accepted tutoria
        # tutoria_details = db.TutoriaAceptada(id_solicitud,sesion_number)
        # print(tutoria_details)
        # if tutoria_details:
        #     # Extract details from the tutoria_details
        #     alumno_nombre = tutoria_details.get('nombre', 'Nombre No Disponible')
        #     alumno_apellido = tutoria_details.get('apellido', 'Apellido No Disponible')
        #     alumno_numero_telefono = tutoria_details.get('numero_celular', 'Número de Teléfono No Disponible')

        #     # Construct the text message with the retrieved details
        #     text_message = f"Perfecto, el estudiante es {alumno_nombre} {alumno_apellido}. Número de Teléfono: {alumno_numero_telefono}. Por favor, ponerse en contacto con él alumno."

        #     # Create and append the text message
        #     textMessage = text_Message(number, text_message)
        #     list.append(textMessage)
        # else:
        #     # Handle the case where tutoria_details is not available
        #     textMessage = text_Message(number, "Lo siento, no se pudieron obtener los detalles de la tutoría aceptada.")
        #     list.append(textMessage)
    elif "no quiero ser tutor" in text:
        pass
        # textMessage = text_Message(number, "Ok se le notificara al alumno que no deseaste ser tutor, que tengas un buen dia")
        # list.append(textMessage)
    elif "soy tutor" in text:
        pass
        # tutor = True
        # body = "porfavor selecione una opcion para continuar"
        # footer = "para volver cuando quieras escriba 'volver menu tutor'"
        # options = ["Ver Perfil", "Editar perfil", "Editar Materia Inscripta", "Ver Historial", "Tutoria Disponible"]

        # replyReaction = replyReaction_Message(number, messageId, "😀")
        # list.append(replyReaction)
        # listReplyData = listReply_Message(number, options, body, footer, "sed2",messageId)
        # sticker = sticker_Message(number, get_media_id("perro_traje", "sticker"))
        # list.append(listReplyData)
        # list.append(sticker)

    elif "soy alumno" in text:
        pass
        # tutor= False
        # body = "porfavor selecione una opcion para continuar"
        # footer = "para volver cuando quieras escriba 'volver menu alumno'"
        # options = ["Ver Perfil", "Editar perfil", "Pedir una Tutoria", "Ver Historial"]

        # replyReaction = replyReaction_Message(number, messageId, "😀")
        # list.append(replyReaction)
        # listReplyData = listReply_Message(number, options, body, footer, "sed2",messageId)
        # sticker = sticker_Message(number, get_media_id("perro_traje", "sticker"))
        # list.append(listReplyData)
        # list.append(sticker)

    elif "volver menu alumno" in text:
        pass
        # tutor= False
        # body = "porfavor selecione una opcion para continuar"
        # footer = "para volver cuando quieras escriba 'volver menu alumno'"
        # options = ["Ver Perfil", "Editar perfil", "Pedir una Tutoria", "Historial de Solicitudes"]

        # replyReaction = replyReaction_Message(number, messageId, "😀")
        # list.append(replyReaction)
        # listReplyData = listReply_Message(number, options, body, footer, "sed2",messageId)
        # sticker = sticker_Message(number, get_media_id("perro_traje", "sticker"))
        # list.append(listReplyData)
        # list.append(sticker)
    elif "ver historial" in text:
        pass
        # print(tutor)
        # history= db.ver_historial(sesion_number)
        # print(history)
        # count = len(history)
        # text_message = f"Estos son los datos de las solicitudes que pediste ({count} solicitudes):\n\n"
        # for record in history:
        #   tutor_name = record.get('nombre_tutor', 'Nombre del Tutor No Disponible')
        #   alumno_name = record.get('nombre_tutorado', 'Nombre del Alumno No Disponible')
        #   estado = record.get('estado', 'Estado No Disponible')
        #   if estado == 'aceptado':
        #     fecha_aceptado = record.get('fecha', 'Fecha de Aceptación No Disponible')
        #     text_message += f"Tutor: {tutor_name}\nAlumno: {alumno_name}\nEstado: {estado}\nFecha de Aceptación: {fecha_aceptado}\n\n"
        #   elif estado == 'terminado':
        #     puntaje_tutor = record.get('puntaje_tutor')
        #     puntaje_alumno = record.get('puntaje_alumno')

        #     if puntaje_tutor is not None:
        #         text_message += f"Tutor: {tutor_name}\nAlumno: {alumno_name}\nEstado: {estado}\nPuntaje Tutor: {puntaje_tutor}\n\n"
        #     else:
        #         text_message += f"Tutor: {tutor_name}\nAlumno: {alumno_name}\nEstado: {estado}\nPuntaje Alumno: {puntaje_alumno}\n\n"
        # if tutor:
        #     text_message +=f"\n si deseas volver al menu anterior escribe 'volver menu tutor'\n"
        # else:
        #     text_message +=f"\n si deseas volver al menu anterior escribe 'volver menu alumno'\n"
        # textMessage = text_Message(number, text_message)
        # list.append(textMessage)

    elif "mes" in text:
        pass
        # print("hola mes")
        # nombre, apellido = db.obtener_datos_alumno(sesion_number)
        # text_message= f"Hola {nombre} {apellido},\n Han pasado 30 dias desde que aceptaron hacer tutoria para la materia ingenieria de software, podemos dar como concluida?\n\n"
        # body = "seleciona una de las opciones"
        # footer='selecciona '
        # options=["Si concluyo", "No concluyo"]
        # replyButtonData = buttonReply_Message(number, options, body, footer, "sed19", messageId)
        # list.append(replyButtonData)
        # replyReaction = replyReaction_Message(number, messageId, "😀")
        # list.append(replyReaction)

    elif "si concluyo" in text:
        pass
        # print("hola si")
        # if tutor:
        #   body = "Perfecto acuerdate que tienes que puntuar al alumno tutorado,\n por favor eliga una de las siguientes opciones:"
        #   footer = ""
        #   options = ["horrible: 1", "malo: 2", "meh: 3", " bueno: 4", "perfecto: 5"]
        #   replyReaction = replyReaction_Message(number, messageId, "😀")
        #   list.append(replyReaction)
        #   listReplyData = listReply_Message(number, options, body, footer, "sed20",messageId)
        #   sticker = sticker_Message(number, get_media_id("perro_traje", "sticker"))
        #   list.append(listReplyData)
        #   list.append(sticker)
        # else:
        #   body = "Perfecto acuerdate que tienes que puntuar al alumno tutor,\n por favor eliga una de las siguientes opciones:"
        #   footer = ""
        #   options = ["horrible: 1", "malo: 2", "meh: 3", " bueno: 4", "perfecto: 5"]
        #   replyReaction = replyReaction_Message(number, messageId, "😀")
        #   list.append(replyReaction)
        #   listReplyData = listReply_Message(number, options, body, footer, "sed20",messageId)
        #   sticker = sticker_Message(number, get_media_id("perro_traje", "sticker"))
        #   list.append(listReplyData)
        #   list.append(sticker)

    elif "horrible" or "malo" or "meh" or "bueno" or "perfecto" in text:
        pass
        # textMessage = text_Message(number,"Muchas gracias por su puntuacion")
        # list.append(textMessage)
    else :
        pass
        # data = text_Message(number,'no entendi lo que me quisiste decir, porfavor escribe denuevo')
        # list.append(data)

if __name__ == "__main__":
    # Puedes establecer un nombre de prueba o ingresar uno desde la terminal si es necesario

    while True:
        text = input("Ingresa el mensaje del usuario (o 'exit' para salir): ").lower()

        if text == 'exit':
            break  # Rompe el ciclo si se ingresa 'exit'

        administrar_chatbot(text)