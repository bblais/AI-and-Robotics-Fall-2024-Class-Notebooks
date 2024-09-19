#!/usr/bin/env python
# coding: utf-8

# In[ ]:


names="""
David
Thomas
Andrew
Anoushka
Todd
Hayley
Jason
Theodore
Colby
Ryan
Emily
Ganesh
Duc
Ro
Benjamin
""".strip().split()


# In[ ]:


names


# In[ ]:


from random import choice


# In[ ]:


names_orig=names.copy()


# In[ ]:


names=names_orig.copy()
pairs=[]
extra=None
while names:
    name1=choice(names)
    names.remove(name1)
    
    try:
        name2=choice(names)
        names.remove(name2)
    except IndexError:
        extra=name1
        continue
    
    pairs.append( [name1,name2])


# In[ ]:


pairs


# In[ ]:


extra


# found_duplicate=True
# while found_duplicate:
#     print("# Demo Pairs")
#     extra=None
#     found_duplicate=False
#     all_pairs=[]
#     for i in range(3):
#         names=names_orig.copy()
#         pairs=[]
# 
#         while names:
#             
#             if extra:
#                 name1=extra
#                 extra=None
#             else:
#                 name1=choice(names)
#                 
#             names.remove(name1)
# 
#             try:
#                 name2=choice(names)
#                 names.remove(name2)
#             except IndexError:
#                 extra=name1
#                 continue
# 
#             if name2<name1:
#                 name1,name2=name2,name1
#                 
#             pairs.append( (name1,name2) )
#             
#         for p in pairs:
#             print("- ",p[0]," - ",p[1])
#             if all_pairs:
#                 if p in all_pairs[-1]:
#                     print(p,"duplicate")
#                     found_duplicate=True
#         print("Extra",extra)
# 
#         print("\n------\n")
#         all_pairs.append(pairs)
#                         
#                         
# 

# # Demo Pairs
# -  Jeff  -  Rubin
# -  Alyssa  -  Trevor_C
# -  Aiden  -  Jared
# -  Jacob  -  Trevor_F
# -  Andrew  -  Danny
# -  Marcus  -  Timothy
# -  Bobby  -  Patrick
# 
# ------
# 
# -  Andrew  -  Jared
# -  Bobby  -  Trevor_C
# -  Jeff  -  Marcus
# -  Patrick  -  Rubin
# -  Timothy  -  Trevor_F
# -  Alyssa  -  Danny
# -  Aiden  -  Jacob
# 
# ------
# 
# -  Bobby  -  Rubin
# -  Jared  -  Trevor_C
# -  Jacob  -  Marcus
# -  Aiden  -  Jeff
# -  Danny  -  Trevor_F
# -  Andrew  -  Patrick
# -  Alyssa  -  Timothy

# In[ ]:


name1


# In[ ]:


name2


# In[ ]:




