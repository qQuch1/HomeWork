cl_int = 1
cl_float = 1.1
cl_str = "Максим"
cl_tuple = ("a", "b")
cl_list = ["a", "b"]
cl_dict = {"name": "Максим", "city": "Krasnodar"}

all_list = [cl_int, cl_float, cl_str, cl_tuple, cl_list, cl_dict]
for i in all_list:
    print(f"{i}, {type(i)}")
