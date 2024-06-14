# TASKY

**A simple project/task management system, built with Flask. You can view the demo here[Tasky](http://100.27.10.232:8000/) I wrote an article on my blog here[Tasky](https://open.substack.com/pub/gabrielhilarion/p/what-i-have-learned-while-creating?r=1mp4kx&utm_campaign=post&utm_medium=web) I am on [LinkedIn](https://www.linkedin.com/in/gabrielhilarion/)**


### INSTALLATION AND USAGE

1. Setup Virtual Environment

``` Bash

    python3 -m venv tasky-env
    source tasky-env/bin/activate
    pip install -r requirements.txt

```

2. Run the Application

``` Bash

   python run.py


```

### CONTRIBUTING
```Feel free to contribute to this application```

### LICENSE

```MIT```


### A SHORT STORY
```Before I began to work on this project I was playing a lot with the server. I created several configuration files, tried to create sub-domains and so on. I had the server in a bad shape. So even though Gunicorn was running, if I visited my application IP address, with the corect port  I saw a different application- one of the applications I deployed earlier. 
Bear in mind that I had disabled and removed every unsed configuration in the ‘sites-enabled’ and  ‘sites-available’ folders. The error was: a file I could not locate was still  referencing a configuration file I had delete from the sites-enabled folder. After several hour of frustration I uninstalled NGINX and reinstalled it, and boom, my site was live.``