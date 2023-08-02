#########################################################
# Author : Atharva Pingale ( FOSSEE Summer Fellow '23 ) #
#########################################################

# DRF imports 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated

# email imports
from osdag_web import mailing

# simpleJWT imports 
from rest_framework_simplejwt.tokens import RefreshToken

# importing Django models 
from osdag.models import UserAccount

# django imports 
from django.conf import settings

# importing serializers
from osdag.serializers import UserAccount_Serializer

# other imports 
from django.contrib.auth.models import User
import string
import os
import random


# obtain the attributes 
SECRET_ROOT = getattr(settings, 'SECRET_ROOT' , "")


def convert_to_32_bytes(input_string) : 
    input_bytes = input_string.encode('utf-8')
    padded_bytes = input_bytes.ljust(32, b'\x00')

    return padded_bytes

class SignupView(APIView) :
    def post(self , request) : 
        print('inside the signup post')
        
        # obtain the useranme and password 
        temp = request.data
        print('temp : ' , temp)
        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get('email')
        isGuest = request.data.get('isGuest')
        print('username : ' , username)
        print('email : ' , email)
        print('password : ' , password)
        print('isGuest : ' , isGuest)
        print('type isGuest : ' , type(isGuest))

        tempData = {
            'username' : username,
            'password_hash' : password,
            'email' : email,
            'allReports' : ['']
        }

        # append the username in the User table ( in the username array )
        # create a JSON object that maps the username to the password and add it to the User table ( passsword column )
        serializer = UserAccount_Serializer(data = tempData)
        if(serializer.is_valid()) : 
            # save the serializer 
            serializer.save()

            # create a user in the Django.contrib.auth 
            user = User.objects.create_user(username , email , password)
            user.save()

            # return 201 
            return Response({'message' : 'The credentials have been created'} , status = status.HTTP_201_CREATED ) 
        else : 
            print('serializer is invalid ')
            print('error : ' , serializer.errors)
            return Response({'message' : 'user with this username already exists' , 'code' : 'unique'} , status = status.HTTP_400_BAD_REQUEST)



class ForgetPasswordView(APIView) : 
    def post(self , request) : 
        print('sindie teh forget password post')
        
        # obtain the new passwrod 
        password = request.data.get('password')

        # PARTIAL WORK, WORK IN PROGRESS 
        return Response({'message' , 'Something goes here'} , status = status.HTTP_201_CREATED)
    

    def get(self , request) : 
        print('inside the forget password get')
        
        # 1. Send the current username to the browser 
        # 2. send the email attached to the username
        # 3. In the browser, the user then types the email, the email is verified against the one which is sent from the Server 
        # 4. If it is matched, then the user enters a new pasword
        
        # this API view just sends the current username and password 
        
        # PARTIAL WORK, WORK IN PROGRESS

        return Response({'message' , 'Something goes here'} , status = status.HTTP_200_OK)
        
class LogoutView(APIView) : 
    permission_classes = (IsAuthenticated,)

    def post(self, request): 
        try : 
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status = status.HTTP_205_RESET_CONTENT)
        
        except Exception as e : 
            return Response(status = status.HTTP_400_BAD_REQUEST)
        

class CheckEmailView(APIView): 
    def post(self , request) : 
        print('inside check email get')

        # obtain teh email 
        email = request.data.get('email')

        # check if the email exists in the database or not 
        # database query for checking if the email is present in the database or not 
        try : 
            pass 
        except : 
            # the email is not present in the the database 
            print('email is not present in the database')

            return Response({'message' , "Email is not registered"} , status = status.HTTP_400_BAD_REQUEST)

        # GENERATE AN OTP
        # K -> is the number of digits in the OTP
        OTP = ''.join(random.choices(string.digits, k = 6))   
        print('OTP : ' , OTP)
        
        # save the OTP somewhere in the FS
        # generate a file with the same name as teh email and store the OTP in the FILE 
        fileName = email.split('@')[0]
        print('fileName : ' ,fileName)
        fileName = fileName + ".txt"
        currentDirectory = os.getcwd()
        print('currentDirectory : ' , currentDirectory)

        # create the file 
        try :       
            with open(currentDirectory+"/file_storage/emails/"+fileName , 'w') as fp : 
                pass 
        except : 
            print('Error in creating the image file')

        # send a mail to this email
        # generate a random OTP and verify if the OTP generated is valid or not 
        try : 
            mailing.send_mail(OTP)
            return Response({'message' : 'OTP Sent'} , status = status.HTTP_200_OK)
        except : 
            return Response({'message' : 'Failed to send the mail'} , status = status.HTTP_400_BAD_REQUEST)
        

    def get(self , request) : 
        print('inside check email post')

        return Response({'message' : 'Under development'} , status = status.HTTP_201_CREATED)



class LoginView(APIView) : 
    def get(self , request) :
        print('inside login get')

        return Response({'message' : 'Fucntion under developement'} , status = status.HTTP_200_OK)
    

    def post(self , request) : 
        print('inside login post')

        # obtain the encrypted username and password 
        username = request.data.get('username')
        password = request.data.get('password')
        isGuest = request.data.get('password')
        print('username : ' , username)
        print('password : ' , password)
        print('isGuest : ' , isGuest)

        if(not isGuest) : 
            print('is a guest user')
            # create a dummy user
            user = User.objects.create_user(username = 'default123' , email = 'default@123.com' , password = 'defualt123' )
            # provide no permissions to the user and just save
            user.save()

        else : 
            print('is not a guest user')
            # find the useranme and password from the UserAccount model 
            result = UserAccount.objects.get(username = username , password = password)
            if(result) : 
                print('the user has been found')

                # grant the login access to the user 
                return Response({'message' : 'Login suvvessfuly'} , status = status.HTTP_200_OK)
            else : 
                print('Login failed')
                return Response({'message' : 'Login failed'} , status = status.HTTP_400_BAD_REQUEST)
            
        # authenticate the user 

        
        # return a sucess message 
        return Response({'message' : 'User logged in'} , status = status.HTTP_200_OK)


class ObtainAllReportsView(APIView) : 
    def get(self , request) : 
        print('inside obtain all reports view get')

        return Response({'message' : 'Inside obtain all report view'} , status = status.HTTP_200_OK)
    
    def post(self , request) : 
        print('inside obtain all report view post')

        return Response({'message' : 'Inside obtain all report view'}, status = status.HTTP_200_OK)