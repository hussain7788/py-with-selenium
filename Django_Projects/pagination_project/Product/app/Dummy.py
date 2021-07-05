
from django.core.paginator import Paginator


name = ["Ravi","Kumar","Mohan","Prasad","Krishna","Murali","Naveen","Bhanu","Kapil","Vijay","Sam","Myke","Sunitha"]

p1 = Paginator(name,3)

print(p1.count)
print(p1.object_list)
print(p1.num_pages) # 5

print("----------------------")
ref = p1.page(2)
print(ref.object_list)
print(ref.has_next())
print(ref.has_previous())
print(ref.previous_page_number())
print(ref.next_page_number())
print(ref.number)
print(ref.paginator)


# from app.models import ProductModel
#
# queryset = ProductModel.objects.all()
#
# p2 = Paginator(queryset,2)
#
# print(p2.count)
# print(p2.object_list)

print("--------------------------------")
d1 = {"idno":101,"name":"Ravi"}

res = d1.get("names","Naveen")

print(res)




