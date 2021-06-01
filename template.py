import os

#directories pushed into list
dirs = [
	os.path.join("data","raw"),
	os.path.join("data","processed"),
	"notebooks",
	"saved_models",
	"src"
]

#Creating directories using the directory list
for dir_ in dirs:
	os.makedirs(dir_, exist_ok=True)
	with open(os.path.join(dir_, ".gitkeep"), "w") as f:
		pass

#files pushed into list
files = [
	"dvc.yaml",
	"params.yaml",
	".gitignore",
	os.path.join("src","__init__.py")
]

#Creating files using the files list
for file_ in files:
	with open(file_, "w") as f:
		pass



