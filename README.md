## Intro



## Steps

### 1. Sign up for Cyfe and login

Go to `http://www.cyfe.com` and sign up and log in. It's free!

[hello](http://jeffsuderman.com/wp-content/uploads/2015/10/WOW.png)

### 2. Add a widget

Click on the Add a widget button in the toolbar at the top.

### 3. Select a Push API widget

Add a widget that can be pushed to via an API.

### 4. Configure the widget

Click on the `Configure widget` button

### 5. Take a note of the widget URL and save

You might want to copy and paste the URL into a text document somewhere for later.

### 6. Sign up to Cloud 9 IDE and sign in

Cloud 9 IDE is brilliant - it allows us to get started easily.

### 7. Create a new workspace

So that you have a sandbox to play around in.

### 8. Clone down this project

* Set the name of the workspace
* Set the workspace to be private so no-one else can see it
* Fill in the Github clone URL to be `git@github.com:johngallagher/learning-apis.git`
* Make sure to select a Python workspace

### 9. Setup

Type the lines below into the terminal.

It might be best to copy and paste them, then there's no chance of typos.

```
virtualenv --python=python3.5 env
source env/bin/activate
pip install -r requirements.txt
```

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

### 11. Look at Cyfe

Go back to your Cyfe dashboard. You should see a lovely graph of revenue. Woohoo!


