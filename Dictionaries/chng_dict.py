# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964}
# thisdict.update({"year":2000})
# print(thisdict)

# for x ,y in thisdict.items():
#     print(x,y)

# mydict = thisdict.copy()
# print(mydict)

# #nested dictionaries
# myfamily = {
#     "child1":{
#          "name" : "Emil",
#          "year" : 2004
#     },
#     "child2":{
#            "name" : "Tobias",
#            "year" : 2007
#     },
#     "child3":{
#             "name" : "Linus",
#             "year" : 2011
#     }
# }
# print(myfamily.items())
# print(myfamily["child2"]["year"])

# thisdict = {"name":"jaspreet","age": 23,}
# for x ,y in thisdict.items():
#   print(x,y)

# dict = {
#   "name":"mohit",
#   "topics":["english","hindi","science"],
#   "year": (2022,2023,2026)
# }
# print(type(dict))
# dict["marks"] = (54,56,76)
# print(dict)

dict = {
  "name":"mohit",
  "sub":{
      "Maths":80,
      "science":70,
      "English":90
  },
  "Year":2025
}
print(dict["sub"]["Maths"])
print(dict.keys())
print(len(list(dict.values())))