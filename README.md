## Intro



## Steps

### 1. Sign up for Cyfe and login

[Go to Cyfe](http://www.cyfe.com) and sign up and log in. It's free!

![](https://dl.dropboxusercontent.com/u/136780/1_signup_for_cyfe.png)

### 2. Add a widget

Click on the Add a widget button in the toolbar at the top.

![](https://dl.dropboxusercontent.com/u/136780/2_add_a_widget.png)

### 3. Select a Push API widget

Add a widget that can be pushed to via an API.

![](https://dl.dropboxusercontent.com/u/136780/3_select_push_widget.png)

### 4. Configure the widget

Click on the `Configure widget` button

![](https://dl.dropboxusercontent.com/u/136780/4_configure_the_widget.png)

### 5. Take a note of the widget URL and save

You might want to copy and paste the URL into a text document somewhere for later.

![](https://dl.dropboxusercontent.com/u/136780/5_take_note_of_widget_url_and_save.png)

### 6. Sign up to Cloud 9 IDE and sign in

Cloud 9 IDE is brilliant - it allows us to get started easily.

[Go to their homepage](http://c9.io) and sign up and sign in.

![](https://dl.dropboxusercontent.com/u/136780/6_sign_up_and_sign_in.png)

### 7. Create a new workspace

So that you have a sandbox to play around in.

![](https://dl.dropboxusercontent.com/u/136780/7_create_workspace.png)


### 8. Setup the workspace with the code from Github

* Set the name of the workspace
* Set the workspace to be private so no-one else can see it
* Fill in the Github clone URL to be `git@github.com:johngallagher/learning-apis.git`
* Make sure to select a Python workspace

![](https://dl.dropboxusercontent.com/u/136780/8_clone_into_workspace.png)

### 9. Setup

Type the lines below into the terminal.

It might be best to copy and paste them, then there's no chance of typos.

```
virtualenv --python=python3.5 env
source env/bin/activate
pip install -r requirements.txt
```

![](https://dl.dropboxusercontent.com/u/136780/9_setup.png)

### 10. Run!

Now for the exciting bit - let's run a Python script to push data from Analytics into Cyfe.

Type the line below into the terminal tab.

```
python graph_revenue.py your-cyfe-widget-url
```

For example, if your widget URL was

```
https://app.cyfe.com/api/push/56f7a767cbd212158125742061285`
```

you'd type

```
python graph_revenue.py https://app.cyfe.com/api/push/56f7a767cbd212158125742061285
```
If all has gone well, you should see:

```
Getting data from analytics...
Pushing data to Cyfe dashboard...
Data pushed successfully!
```

![](https://dl.dropboxusercontent.com/u/136780/10_run.png)

### 11. Look at Cyfe

Go back to your Cyfe dashboard. You should see a lovely graph of revenue. Woohoo!


![](https://dl.dropboxusercontent.com/u/136780/11_look_at_cyfe.png)