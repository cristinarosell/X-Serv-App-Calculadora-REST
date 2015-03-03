#!/usr/bin/python
# -*- coding: utf-8 -*-
#Calculador Rest


import webapp
import random


class Servidor (webapp.webApp):
    def parse(self, request):
        # verb= put o get
        verb = request.split()[0]
        #nombre del recurso
        recurso = request.split()[1].split("/")[1]
        #body es el cuerpo del put
        body = request.split()[-1]

        return (verb, recurso, body)

    def process(self, parseRequest):

        (verb, recurso, body) = parseRequest

        if (verb == "PUT"):
            self.operacion = body
            return ("200 OK",
                    "<html><body>" + "La opercion es: " +
                    body + "</body></html>")
        elif (verb == "GET"):
            try:
                if (len(self.operacion.split('+')) == 2):
                    cadena = self.operacion.split('+')
                    op1 = cadena[0]
                    op2 = cadena[1]
                    result = float(op1) + float(op2)
                elif (len(self.operacion.split('-')) == 2):
                    cadena = self.operacion.split('-')
                    op1 = cadena[0]
                    op2 = cadena[1]
                    result = float(op1) - float(op2)
                elif (len(self.operacion.split('/')) == 2):
                    cadena = self.operacion.split('/')
                    op1 = cadena[0]
                    op2 = cadena[1]
                    result = float(op1) / float(op2)
                elif (len(self.operacion.split('x')) == 2):
                    cadena = self.operacion.split('x')
                    op1 = cadena[0]
                    op2 = cadena[1]
                    result = float(op1) * float(op2)
                else:
                    result = "La operacion no es correcta (+-/x)"

                return ("200 OK", "<html><body>" + "el resultado es: " 
                        + str(result) + "</body></html>")
            except AttributeError:
                return ("404 Not Found",
                        "<html><body>No hay operacion</body></html>")
            except ValueError:
                return ("404 Not Found",
                        "<html><body>Operacion incorrecta</body></html>")
            except ZeroDivisionError:
                return ("404 Not Found",
                        "<html><body>Error: Division entre 0 </body></html>")

        else:
            return ("404 Not Found",
			        "<html><body>" + "Error: Realizar PUT o GET" + 
                    "</body></html>")


if __name__ == "__main__":
    serv = Servidor("localhost", 1234)
