from rest_framework.views import APIView
import json
from rest_framework.response import Response
from .models import Contact, ContactSerializer

class ContactView(APIView):
    def get(self, request):

        all_entries = Contact.objects.all()
        #serialize de contact
        serializer = ContactSerializer(all_entries, many=True)
        #include it on the response
        return Response(serializer.data)
    def put(self, request):
        
        body_unicode = request.body.decode('utf-8')
        c = json.loads(body_unicode)
        # create the new contact
        p = Contact(full_name=c['full_name'], email=c['email'],phone=c['phone'],address=c['address'])
        #save the contact
        p.save()
        
        #serialize de contact
        serializer = ContactSerializer(p, many=False)
        
        #include it on the response
        return Response(serializer.data)
        
class SingleContactView(APIView):
    def get(self, request, contact_id):
        try:
            contact = Contact.objects.get(id=contact_id)
        except Contact.DoesNotExist:
            return Response({ msg: "Contact not found"}, status=404)
        #serialize de contact
        serializer = ContactSerializer(contact, many=False)
        #include it on the response
        return Response(serializer.data)