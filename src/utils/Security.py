from decouple import config  # Función para traer variables de entorno
import datetime
import pytz  # para tener la zona horaria
import jwt


class Security:

    secret = config(
        "JWT_KEY"
    )  # Clave secreta asignada para los JWT en nuestra variable de entorno
    tz = pytz.timezone("America/Santiago")

    @classmethod
    def generate_token(cls, authenticated_user):
        payload = {
            "iat": datetime.datetime.now(tz=cls.tz),
            "exp": datetime.datetime.now(tz=cls.tz) + datetime.timedelta(minutes=10),
            "username": authenticated_user.username,
            "fullname": authenticated_user.fullname,
            "roles": ["Administrator", "Editor"],
            "variable_propia": "Puedo colocar aquí lo que quieras",
        }
        return jwt.encode(payload, cls.secret, algorithm="HS256")

    """
    En Python, cls es una convención utilizada para referirse a la clase 
    dentro de un método de clase. Similar a cómo self se refiere a la instancia 
    de la clase en los métodos de instancia, cls se refiere a la propia 
    clase en los métodos de clase.
    """

    @classmethod
    def verify_token(cls, headers):
        if "Authorization" in headers.keys():
            authorization = headers["Authorization"]
            encoded_token = authorization.split(" ")[1]

            try:
                payload = jwt.decode(encoded_token, cls.secret, algorithms=["HS256"])
                roles = list(payload["roles"])

                if "Administrator" in roles:
                    return True
                return False
            except (jwt.ExpiredSignatureError, jwt.InvalidSignatureError):
                return False

        return False






















# from decouple import config
# import datetime
# import jwt
# import pytz


# class Security():

#     secret = config('JWT_KEY')
#     tz = pytz.timezone("America/Lima")

#     @classmethod
#     def generate_token(cls, authenticated_user):
#         payload = {
#             'iat': datetime.datetime.now(tz=cls.tz),
#             'exp': datetime.datetime.now(tz=cls.tz) + datetime.timedelta(minutes=10),
#             'username': authenticated_user.username,
#             'fullname': authenticated_user.fullname,
#             'roles': ['Administrator', 'Editor']
#         }
#         return jwt.encode(payload, cls.secret, algorithm="HS256")

#     @classmethod
#     def verify_token(cls, headers):
#         if 'Authorization' in headers.keys():
#             authorization = headers['Authorization']
#             encoded_token = authorization.split(" ")[1]

#             if (len(encoded_token) > 0):
#                 try:
#                     payload = jwt.decode(encoded_token, cls.secret, algorithms=["HS256"])
#                     roles = list(payload['roles'])

#                     if 'Administrator' in roles:
#                         return True
#                     return False
#                 except (jwt.ExpiredSignatureError, jwt.InvalidSignatureError):
#                     return False

#         return False
