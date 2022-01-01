from images import query
from mosiac import constructMural

# get our query
name = "tyra banks"

# download images
print(f'Downloading images for {name}')
query(name)

# construct mural
print(f'Constructing mural for {name}')
constructMural()

# output success message
print(f'Program succesfully exited')