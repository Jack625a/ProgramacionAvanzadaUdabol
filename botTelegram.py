#apiTelegramBot: 7722075493:AAENUxlfRsc0z_a7ST6NqEqZQWgmMHks0DQ
#apiGemini: AIzaSyCiCnccEOQQZK_l8de7oeqcaVQBWQCnh-E

#PASO 1. IMPORTAR LAS LIBRERIAS
from dotenv import load_dotenv
import os 
import google.generativeai as genai
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler,ContextTypes,filters
import logging
from telegram import Update

#PASO 2. CONFIGURAR LAS VARIABLES DE ENTORNO
load_dotenv()
telegramToken="7722075493:AAENUxlfRsc0z_a7ST6NqEqZQWgmMHks0DQ"
geminiApi="AIzaSyCiCnccEOQQZK_l8de7oeqcaVQBWQCnh-E"
 
#PASO 3. CARGAR EL ENTRENAMIENTO 
with open("entrenamiento.txt","r",encoding="utf-8") as archivo: entrenamiento=archivo.read()

#PASO 4. CONFIGURAR EL MODELO
genai.configure(api_key=geminiApi)
modelo=genai.GenerativeModel("gemini-2.5-flash-preview-05-20")

#PASO 5. CARGADO DE LOS DATOS
logging.basicConfig(level=logging.INFO)

#PASO 6. CREAR LA FUNCION PARA OBTENER LOS MENSAJES
async def obtenerMensajes(update:Update, context:ContextTypes.DEFAULT_TYPE):
    mensajeUsuario=update.message.text
    indicacion=f""" Eres un asistente de atencion al cliente de la
      Universidad UDABOL sede Oruro tu nombre será UDABOT, Solo deberas usar la 
        informacion para responder a los usuarios: {entrenamiento}  
        Deberas ser lo mas coordial posible para responder las 
        preguntas del cliente: {mensajeUsuario}, deberas responder de forma
        profesional y breve.
        """
    try:
        respuesta=modelo.generate_content(indicacion)
        await update.message.reply_text(respuesta.text)
    except Exception as e:
        update.message.reply_text("Ocurrio un error al procesar su mensaje...")

#PASO 7. CONFIGURAR LOS COMANDOS /start
async def comandos(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hola bievenido a UDABOT en que puedo ayudarte!")

#PASO 8. INICIAR EL BOT
if __name__=="__main__":
    app=ApplicationBuilder().token(telegramToken).build()
    #congigurar el comando
    app.add_handler(CommandHandler("start",comandos))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, obtenerMensajes))
    print("Bot iniciado...-")
    app.run_polling()