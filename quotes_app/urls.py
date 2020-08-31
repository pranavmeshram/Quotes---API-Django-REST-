from django.urls import path
from quotes_app.views import *


urlpatterns = [
    path('quotes', CreateAndListQuotes.as_view(), name="Create_&_List_Quotes"),

    path('quotes/lang/<str:lang>', GetQuoteByLanguage.as_view(), name="Get_quotes_by_language"),
    path('quote/random', GetRandomQuote.as_view(), name="Get_Random_Quote"),
    path('quote/random/lang/<str:lang>', GetRandomQuoteByLanguage.as_view(), name="Get_Random_Quote_By_Language"),

    path('quote/<int:id>', UpdateQuote.as_view(), name="Update_Quote"),
    
]
