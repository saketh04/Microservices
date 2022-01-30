
     
In general there are many microservices which has its own process and they communicate with each other to form an application. To create a microservice using python we use nameko which is a python microservice framework. First of all we should create a virtual environment and install nameko using pip install nameko and to run this we use RabbitMQ as a broker for communication between these nameko services, we can use this rabbitmq by running it in docker and after that we create a python file containing the above code which imports nameko and sleep, here sleep is used to delay the output for given time in seconds. Now run that in the folder which we created by using nameko run <filename>.
After this we will get a message that connection is established successfully at the port.Coming to testing we test our code in an nameko shell by giving the following command n.rpc.intro_service.biodata(name='Tallam Saketh',branch='ECE') 


The output is shown in the screenshot below.
  
![Screenshot 2022-01-22 030036](https://user-images.githubusercontent.com/59107977/150605654-32ffdb2b-bd16-4180-bd5b-9853d979f45f.png)

