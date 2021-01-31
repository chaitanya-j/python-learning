from configparser import ConfigParser

#Get the configparser object
config_object = ConfigParser()

#Assume we need 2 sections in the config file, let's call them USERINFO and SERVERCONFIG
config_object["USERINFO"] = {
    "logging": "Chaitanya Jaipurkar",
    "rollno": 34,
    "password": "shreeram@123"
}


#Write the above sections to config.ini file
with open('config.ini', 'w') as conf:
    config_object.write(conf)

#Read config.ini file
config_object = ConfigParser()
config_object.read("config.ini")

#Get the password
userinfo = config_object["USERINFO"]
userinfo["nam"] = "Vishrut Vaishampayan"
print(userinfo["name"])