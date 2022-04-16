from menucard.models import Hotel


def is_admingroup(user):
     return user.groups.filter(name='admingroup').exists()

class FilterSet:
    """class for filtering the foreign key in admin site """
    def __init__(self,name,qs,user,db_field):
        self.name=name
        self.qs=qs
        self.user=user
        self.db_field=db_field
        
    def userfilter(self):
        #filtering based on username of the requested user
        return self.qs.filter(username=self.user)
    def hotelfilter(self):
        #filtering based on userid of the foreign key of hotel 
        return self.qs.filter(user_id=self.user.id)
    def categoryfilter(self):
        #filtering based on userid of the foreign key of category 
        return self.qs.filter(hotel_id=Hotel.objects.get(user_id=self.user.id).id) 
    def feildselection(self,filterfunc):
        if self.db_field.name == self.name:
            if self.user.is_superuser or is_admingroup(self.user) :
                    queryset = self.qs                 
            else:
                # calling the based on the filter methods as above (user/hotel/category)
                    queryset =filterfunc()
        return queryset   

