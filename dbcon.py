import configparser
import os

#Writing the ini
conf = configparser.ConfigParser()

conf['credentials'] = {'user1':'matt', 'pass1':'easy','user2':'joe','pass2':'hard'}
conf['connectionstring'] = {'servername':'server', 'port':'23'}

with open('C:\\code\\dbt\\two.ini', 'w') as configfile:
	conf.write(configfile)


#Importing the ini

conf = configparser.ConfigParser()
conf.read('C:\\code\\dbt\\two.ini')
#print(conf.sections())
un1 = conf['credentials']['user1']
p1 = conf['credentials']['pass1']
print(un1, 'has password', p1)

