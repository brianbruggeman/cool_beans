# Cool Beans
AWS App for Elastic Beanstalk using Python

To get started, you'll need [Flask](http://flask.pocoo.org/) and [Amazon's Elastic Beanstalk Commandline Interface](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install.html):

    > pip install flask
    > pip install awsebcli

After installing the pre-requisites, you'll need an Amazon account setup.  Assuming that all goes well, you can then use some of the eb commands to setup and deploy the application.

    > virtualenv my_cool_beans
    > cd my_cool_beans
    > mkdir my_cool_beans
    > cd my_cool_beans    # yes, that's:  <root>/my_cool_beans/my_cool_beans

The first `my_cool_beans` folder is for your virtualenv environment.  The second is for your git repo, code and elastic beanstalk files.
    
Setup Git for this repo

    > git init
    > git flow init
    
Jump into the virtualenv environment to autogenerate `requirements.txt`.

    > . bin/activate
    > pip install Flask
    > pip install docopt  # This is for a commandline interface on your local folder
    > pip freeze > requirements.txt
    > deactivate
    
Now use the Elastic Beanstalk interface to generate a new instance.

    > eb init

And then you'll want to edit your `application.py` as you see fit.

    > vi application.py

Assuming you're happily done coding, you should probably test it...

    > python application.py --debug --host=127.0.0.1 --port=5000

And then go to your local instance:  [http://127.0.0.1:5000](http://127.0.0.1:5000)

Now you can deploy:

    > eb create

Assuming you got a successful launch, then try opening it up in your browser:

    > eb open
