from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from quotes_app.models import Quotes
from quotes_app.serializers import QuotesSerializers
import random

# Create your views here.



class CreateAndListQuotes(APIView):

    #Getting all Quotes
    def get(self, request):
        quotes_obj = Quotes.objects.all()
        qoutes_ser_obj = QuotesSerializers(quotes_obj, many=True)
        return Response(qoutes_ser_obj.data)

    #Creating a Quote
    def post(self, request):
        quotes_obj = QuotesSerializers(data=request.data)
        
        if quotes_obj.is_valid():
            quotes_obj.save()
            return Response(quotes_obj.validated_data, status=status.HTTP_201_CREATED)

        else:
            return Response(cat_ser_obj.errors, status=status.HTTP_400_BAD_REQUEST)

        


class GetQuoteByLanguage(APIView):

    #Getting Quotes filtered by language
    def get(self, request, lang):
        if lang == 'en':
            quotes_obj = Quotes.objects.filter(sr_lang__exact = '')
            qoutes_ser_obj = QuotesSerializers(quotes_obj, many=True)
            return Response(qoutes_ser_obj.data, status=status.HTTP_200_OK)

        elif lang == 'sr':
            quotes_obj = Quotes.objects.filter(en_lang__exact = '')
            qoutes_ser_obj = QuotesSerializers(quotes_obj, many=True)
            return Response(qoutes_ser_obj.data, status=status.HTTP_200_OK)

        else:
            return Response('Language quote does not exists. YET !',status=status.HTTP_404_NOT_FOUND)


class GetRandomQuote(APIView):

    ##Getting a random Quote
    def get(self, request):
        while True:
            quotes_ids_list = [1,2,3,4,5,100]  #IDs of all the quotes
            random_id = random.choice(quotes_ids_list)
            try:
                quote_obj = Quotes.objects.get(id=random_id)
                break
            except:
                continue

        qoute_ser_obj = QuotesSerializers(quote_obj)
        return Response(qoute_ser_obj.data, status=status.HTTP_200_OK)
    


class GetRandomQuoteByLanguage(APIView):

    def get(self, request, lang):

        if lang == 'en':
            while True:
                quotes_ids_list = [1,2,3,4,5,100]  #IDs of all the quotes
                random_id = random.choice(quotes_ids_list)
                try:
                    quote_obj = Quotes.objects.get(id = random_id, sr_lang__exact = '')
                    break
                except:
                    continue

            qoute_ser_obj = QuotesSerializers(quote_obj)
            return Response(qoute_ser_obj.data, status=status.HTTP_200_OK)



        elif lang == 'sr':
            while True:
                quotes_ids_list = [1,2,3,4,5,100]  #IDs of all the quotes
                random_id = random.choice(quotes_ids_list)
                try:
                    quote_obj = Quotes.objects.get(id = random_id, en_lang__exact = '')
                    break
                except:
                    continue

            qoute_ser_obj = QuotesSerializers(quote_obj)
            return Response(qoute_ser_obj.data, status=status.HTTP_200_OK)

        else:
            return Response('Language quote does not exists. YET !',status=status.HTTP_404_NOT_FOUND)




class UpdateQuote(APIView):

    #Updating a Quote
    def put(self, request, id):
        try:
            quote_obj = Quotes.objects.get(id=id)
            quote_ser_obj = QuotesSerializers(instance=quote_obj, data=request.data, partial=True)

            if quote_ser_obj.is_valid():
                updated_obj = quote_ser_obj.save()
                obj = QuotesSerializers(updated_obj)
                return Response(obj.data, status=status.HTTP_200_OK)
            else:
                return Response(obj.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response("Quote Not Found",status=status.HTTP_404_NOT_FOUND)


    #Getting a Quote
    def get(self, request, id):
        try:
            quote_obj = Quotes.objects.get(id=id)
            quote_ser_obj = QuotesSerializers(quote_obj)
            return Response(quote_ser_obj.data, status=status.HTTP_200_OK)
        except:
            return Response("Object Not Found",status=status.HTTP_404_NOT_FOUND)
