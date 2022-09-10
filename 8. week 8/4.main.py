from html_demo import Tag

tag = Tag('simple_tag', 'simple_content')

tag.temp1 = 10

print(tag.__dict__)  # pay attention to the _temp and temp values

tag.__temp2 = 50
print(tag.__dict__)  # pay attention to the _Tag__temp2
# mangling rule add _ClassName at the beginning of the instance attributes that started with __

# setter and Getter

# way1
tag.sample1Variable = 'test 1'
print(tag.sample1Variable)
print(tag.__dict__)


