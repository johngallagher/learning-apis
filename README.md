Technical marketing, growth hacking, call it what you want. There's a demand on digital marketers to become more technically savvy.

But where on earth do you start? Python, APIs, web development, scripting... it's all pretty confusing and complex. You can waste hours on useless tutorials, banging your head against a brick wall.

I'm a programmer who loves teaching. I want to help digital marketers understand this stuff.

This is my first tutorial, just to test the waters. 

I've heard a few folk talk about dashboards and APIs so I thought that'd be a good place to start.

I'd love to hear [your feedback on what challenges you have](http://goo.gl/forms/82oj2ypKeU) and what you'd like to learn.

## Goal

Let's imagine we've got a Google Analytics account containing all our sales data.

We want to make a dashboard to see revenue alongside Twitter followers, customer support tickets and Facebook likes.

As a first step, we want to see a widget with revenue in it, a bit like so:

![](https://dl.dropboxusercontent.com/u/136780/0_dashboard.png)

## Background

We're going to be using:

* A dummy Google Analytics account with data already populated
* Cyfe for the dashboards
* Python for the script
* APIs to export and import the data
* Cloud 9 IDE to get you up and running quickly
* A healthy dose of optimism

Stuff I've already done:

* Setup a Google Analytics account with dummy data in it
* Built a Python script that can extract the data and push it into Cyfe

What you need to do:

* Create Cloud 9 IDE and Cyfe accounts
* Setup the script on Cloud 9
* Run the script

**Let's get going!**

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


## But I want more!

If you enjoyed this, you might want to know:

* How on earth does this all work?
* What is Python?
* Why use APIs?
* How can I change this to show clicks instead of revenue?
* Why was Ricky Martin ever popular?

## Tell me what you want

I want to create a series of courses to help you learn the bits of programming you care about.

But before I plough loads of time into it, I need to understand what you want.

I've put together a 6 question survey. It should take you about 3 minutes to fill in.

[Take the survey here](http://goo.gl/forms/82oj2ypKeU)

I'd love to learn all about your challenges!

## All feedback is welcome

* Did you hate this?
* Did you find it boring?
* Would you rather I showed you how to do something a bit more interesting to you?
* Was it too long?
* Did you dream about Ricky Martin again last night?

Please leave me a comment below or hit me up on Twitter - http://twitter.com/synapticmishap

Thanks for reading!
