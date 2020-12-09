#!/usr/bin/env python
# coding: utf-8

# # 3-10. Every Function: Think of something you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.

# In[33]:


languages = ["c", "python", "c++", "r", "ruby", "swift"]


# In[34]:


languages.append("kotlin")
print(languages)


# In[35]:


languages.pop()
print(languages)


# In[36]:


languages.insert(2, "c#")
print(languages)


# In[37]:


languages.remove("c#")
print(languages)


# In[38]:


sorted(languages)


# In[39]:


print(languages)
languages.sort()
print(languages)


# In[40]:


languages.reverse()
print(languages)


# In[41]:


len(languages)


# In[42]:


languages[2] = "scala"
print(languages)

