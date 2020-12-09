#!/usr/bin/env python
# coding: utf-8

# # 3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
# # • Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.
# # • Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
# # • Print a second set of invitation messages, one for each person who is still in your list.

# In[1]:


guests = ["narayan hari", "pruthvi chhowala", "vishal jadav"]


# In[6]:


print("\nMessege From " + guests[2].title() + " : ")
print("\nI am So Sorry Bhavik, I have an urgent meeting today at Bengaluru.")


# In[7]:


guests[2] = "tarang chhowala"


# In[8]:


print("Good Morining, " + guests[0].title() + " you are invited for dinner at my home today.")
print("Good Morining, " + guests[1].title() + " you are invited for dinner at my home today.")
print("Good Morining, " + guests[2].title() + " you are invited for dinner at my home today.")

