# CertAdmin
A tool to create and maintain a certificate authority

## This tool can:

* create a self-signed openssl authority certificate (if you do not have one)
* form this CA: create a certificate you can use for your webserver 
* form this CA: create client PKC12 certificates and passwords you can distribute to the users of your webservice
* be used purely as acommand line tool, but it also provides a gui (written in PySide6 and QML)

## This tool does not:

* guarantee to create secure certificates
* install or configure your webserver
* depend on your openssl.conf file
* use certificates that do not end with "crt"
* use keys that do not end with "key"

## What you need

* a computer with python3
* to install the dependencies you need pip installed
* not tested on windws!

## Setup

 * clone this repository
 * if you are missing dependencies while running certadmin exeute the setup.sh script

## Execute the script

* run ```certadmin``` from a command line without any commands
    
    * you will see a help text telling you what commands are available

* if you run ```certadmin``` with any of the commands for the first time, a file called ```certadmin.json``` will be generated and the program will stop
    
    * you need to edit this file with an editor of your choice. contents are:
        * __certdir__: where you want to save your certificates
        * __names/server__: the name of your webserver (e.g. www.example.com)
        * __names/ca__: the name of your certificate authority file
    
    * the following subdirectories and files will be created in __certdir__:
        * __passwd__: a file that contains the users and the passwords matching the created client certificates (user this file a as the authorization file for your webserver) 
        * __private__: a directory containing the certificate and private key for both the CA and the server
        * __public__: a directory containing the p12 certificates and password files for the clients
            * keep these files secure. zou can for exampe use gpg to distributes the certificates and passwords to your users
    
    * if you provide your own ca file, copy it into the private folder and change the __names/ca__ entry in the ```certadmin.json``` file accordingly 

* after you have edited your JSON file and run certadmin (with a command)
    * the command will execute if you already have a ca file
    * if not, a ca file will be generated (follow the onscreen instruction) and then your command will be executed
