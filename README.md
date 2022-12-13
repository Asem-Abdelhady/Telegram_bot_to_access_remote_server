# Remote server access

The remote access server using telegram bot is a project that basically let you access your own remote server using telegram API as a telegram bot with some extra utilities. This is done by mounting your home directory in a running docker container for the telegram bot server with which you can use the telegram API.

## Installation

Make sure you have Ansible installed in your machine, preferably using pip:


```bash
python3 -m pip install --user ansible
ansible-galaxy collection install community.docker
```

After that you need to export the .local/bin to you **~/.bashrc** file using:

```bash
export PATH=$PATH:/home/$USER/.local/bin
```

Clone this repository and under [/app](https://github.com/Asem-Abdelhady/Telegram_bot_to_access_remote_server/tree/master/app) add your ***.env*** file. The .env file should hold the data for your telegram bot. Make sure the naming and data is similar to [.env.sample](https://github.com/Asem-Abdelhady/Telegram_bot_to_access_remote_server/blob/master/app/.env.sample) .

Before running the the ansible-playbook make sure that the following ports are free in your localhost:

```text
localhost:3000
localhost:9100
localhost:9090
```

If you do not have docker and docker-compose run the following:

```bash
sudo apt install docker.io
sudo apt install docker-compose
```

Now you can go to under [/ansible](https://github.com/Asem-Abdelhady/Telegram_bot_to_access_remote_server/tree/master/ansible) directory and run:

```bash
ansible-playbook main.yaml
```



## Usage

Your grafana container is running on **port 3000** go to your local host, sign in using **admin** for both user and password, and add the data source similar to the following image

<p align="center"><img src= "images/Grafana3" ></p>

The next step is adding your monitoring dashboards. I have provided 2 JSON files one for node-export and the other using Prometheus. You can find them under [/monitoring/dashboards](https://github.com/Asem-Abdelhady/Telegram_bot_to_access_remote_server/tree/master/monitoring/dashboards). Import both dashboards then configure your alerts by adding alert that will be sent to the telegram bot. For example, i added the alert that allows me to get notified when the temperature of the first CPU is above 40. Add alerts that suit you and preferably make the check every 1m for 5m. 

<p align="center"><img src= "images/Grafana1" ></p>

 



Now you need to add the the contact point which is telegram in our case. It should be something similar to this image.

<p align="center"><img src= "images/Grafana2" ></p>



And you can always press Test to see if the checkpoint works fine.

<p align="center"><img src= "images/Telegram1" ></p>

## Visuals

This part is where I show how the bot works.

The following image is the notification from Grafana.

 <p align="center"><img src= "images/Telegram2" ></p>

 

Some functionalities in accessing the remote server:

 <p align="center"><img src= "images/Telegram4" ></p>

 <p align="center"><img src= "images/Telegram3" ></p>



## Customizations

- You can always add extra features or edit the existing ones from the [main.py] (https://github.com/Asem-Abdelhady/Telegram_bot_to_access_remote_server/blob/master/app/main.py) file.

- If you want instead of making the Ansible playbook running on your local machine only you should add SSH configuration to the machine you want to connect to. Such configuration should be added manually under the [/ansible](https://github.com/Asem-Abdelhady/Telegram_bot_to_access_remote_server/tree/master/ansible) directory.

- For Grafana notifications you can use better templates that integrate with telegram messages so it is more readable.

- You can add your github action to deal with the docker image of the telegram server. You can also use the one I made here is the one I use to build and deploy docker image to docker-hub with every commit:

  ```yaml
  name: Docker Image CI
  
  on:
    push:
      branches: [ "master" ]
    pull_request:
      branches: [ "master" ]
  
  jobs:
    build:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v3
        - name: Build the Docker image
          run: docker build ./app --tag <USERNAME>/tg_remote_server
        - name: Login to DockerHub
          run: docker login -u <USERNAME> -p ${{ secrets.DOCKER_HUB_TOKEN }}
        - name: Push the Docker image
          run: docker push <USERNAME>/tg_remote_server
    
  
  ```

  

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
