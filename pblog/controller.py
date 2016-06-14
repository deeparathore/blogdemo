from .models import Post
from django.contrib import auth

class Post_detail():
  
    def shrot_description_post(self):
        list1 = []
        tempdata = Post.objects.raw(""" select p.*,au.username from pblog_post as p join auth_user as au
                                    on p.user_id = au.id where p.status = 1 order by p.id desc""")
        for i in tempdata:
            tempdict = {}
            short = i.message
            if len(short) > 230:
                 msg =  short[:250]
                 msg = msg + ' ...'
                
            else: 
                msg = short
           
            tempdict['title'] = i.title
            tempdict['message'] = msg
            tempdict['date'] = i.date
            tempdict['post_id'] = i.id
            tempdict['username'] = i.username
            list1.append(tempdict)
        
        return list1
    
    def single_post_detail(self,post_id):
        data = Post.objects.raw(""" select p.*,au.username from pblog_post as p join auth_user as au
                                    on p.user_id = au.id where p.status = 1 and  p.id = %s """%post_id)
        return data
