#!/usr/bin/env python
# coding: utf-8

# In[1]:


import flask


# In[2]:


from flask import Flask, request


# In[3]:


from flask import render_template


# In[4]:


import joblib


# In[5]:


app = Flask(__name__)


# In[6]:


@app.route("/", methods = ["GET","POST"])
def index():
    if request.method == "POST":
        rates = request.form.get("rates")
        print(rates)
        model1 = joblib.load("Regression")
        r1 = model1.predict([[rates]])
        model2 = joblib.load("Tree")
        r2 = model2.predict([[rates]])
        return(render_template("index.html", result1 = r1,result2 = r2))
    else:
        return(render_template("index.html" , result1 ="WAITING",result2 = "WAITING"))


# In[ ]:


if __name__== "__main__":
    app.run()

