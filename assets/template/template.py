from os import rename
from pathlib import Path
from re import sub
from shutil import copyfile, rmtree

from python_template.utils.yaml_handler import YAMLHandler

TEMPLATE_CUSTOM_YAML_PATH = "assets/template/template_custom.yml"
TEMPLATE_ORIG_YAML_PATH = "assets/template/template_orig.yml"


custom_dict = YAMLHandler().load(TEMPLATE_CUSTOM_YAML_PATH)
orig_dict = YAMLHandler().load(TEMPLATE_ORIG_YAML_PATH)


# get orig and custom source code names
orig_src_name = orig_dict["GITHUB_REPO_NAME"].replace("-", "_")
custom_src_name = custom_dict["GITHUB_REPO_NAME"].replace("-", "_")


####################################################
filename = "README.rst"
####################################################

# Replace README.rst with assets/template/README.rst
# and add custom values
copyfile("assets/template/README.rst", filename)

# read text
with open(filename) as f:
    text = f.read()

# replace
text = (
    text.replace(
        "GITHUB_REPO_DESCRIPTION",
        custom_dict["GITHUB_REPO_DESCRIPTION"],
    )
    .replace(
        "GITHUB_REPO_DESCRIPTION_SHORT",
        custom_dict["GITHUB_REPO_DESCRIPTION_SHORT"],
    )
    .replace(
        "#" * len("GITHUB_REPO_DESCRIPTION_SHORT"),
        "#" * len(custom_dict["GITHUB_REPO_DESCRIPTION_SHORT"]),
    )
    .replace(
        orig_dict["GITHUB_ORG_NAME"],
        custom_dict["GITHUB_ORG_NAME"],
    )
    .replace(
        orig_dict["GITHUB_REPO_NAME"],
        custom_dict["GITHUB_REPO_NAME"],
    )
)

# write
with open(filename, "w") as f:
    f.write(text)


####################################################
filename = "pyproject.toml"
####################################################

# read text
with open(filename) as f:
    text = f.read()

# replace
text = (
    text.replace(
        orig_dict["GITHUB_REPO_DESCRIPTION_SHORT"],
        custom_dict["GITHUB_REPO_DESCRIPTION_SHORT"],
    )
    .replace(
        orig_dict["GITHUB_REPO_NAME"],
        custom_dict["GITHUB_REPO_NAME"],
    )
    .replace(
        orig_dict["GITHUB_ORG_NAME"],
        custom_dict["GITHUB_ORG_NAME"],
    )
    .replace(
        orig_dict["OWNER_FIRST_NAME"],
        custom_dict["OWNER_FIRST_NAME"],
    )
    .replace(
        orig_dict["OWNER_LAST_NAME"],
        custom_dict["OWNER_LAST_NAME"],
    )
    .replace(
        orig_dict["OWNER_EMAIL"],
        custom_dict["OWNER_EMAIL"],
    )
)

text = sub("version = .*", 'version = "0.0.0"', text)

# write
with open(filename, "w") as f:
    f.write(text)


####################################################
filename = "Makefile"
####################################################

# read text
with open(filename) as f:
    text = f.read()

# replace
text = text.replace(
    orig_dict["GITHUB_REPO_NAME"],
    custom_dict["GITHUB_REPO_NAME"],
)

# write
with open(filename, "w") as f:
    f.write(text)


####################################################
filename = "LICENSE.txt"
####################################################

# read text
with open(filename) as f:
    text = f.read()

# replace
text = text.replace(
    orig_dict["OWNER_FIRST_NAME"],
    custom_dict["OWNER_FIRST_NAME"],
).replace(
    orig_dict["OWNER_LAST_NAME"],
    custom_dict["OWNER_LAST_NAME"],
)

# write
with open(filename, "w") as f:
    f.write(text)


######################################################
# Loop over all files in src code and test directories
######################################################

# create a list of the src code and test directory names
dirname_list = ["tests", orig_src_name]

# loop
for dirname in dirname_list:
    # get a generator of all python-script PosixPaths in the directory
    posixpath_generator = Path(dirname).glob("**/*.py")

    # iterate over python script paths
    for posixpath in posixpath_generator:
        # skip empty init files
        if "__init__.py" in str(posixpath):
            continue

        # read text
        with open(posixpath) as f:
            text = f.read()

        # replace
        text = text.replace(
            orig_src_name,
            custom_src_name,
        )

        # write
        with open(posixpath, "w") as f:
            f.write(text)

# rename source code directory
rename(
    orig_src_name,
    custom_src_name,
)


####################################################
filepath = "docsrc/index.rst"
####################################################

# read text
with open(filepath) as f:
    text = f.read()

# replace
text = text.replace(
    orig_dict["GITHUB_REPO_DESCRIPTION_SHORT"],
    custom_dict["GITHUB_REPO_DESCRIPTION_SHORT"],
).replace(
    "#" * len(orig_dict["GITHUB_REPO_DESCRIPTION_SHORT"]),
    "#" * len(custom_dict["GITHUB_REPO_DESCRIPTION_SHORT"]),
)

text = sub("version = .*", 'version = "0.0.0"', text)

# write
with open(filepath, "w") as f:
    f.write(text)


####################################################
filepath = "docsrc/conf.py"
####################################################

# read text
with open(filepath) as f:
    text = f.read()

# replace
text = text.replace(
    orig_src_name,
    custom_src_name,
)

text = sub("version = .*", 'version = "0.0.0"', text)

# write
with open(filepath, "w") as f:
    f.write(text)


####################################################
filepath = "docsrc/api.rst"
####################################################

# read text
with open(filepath) as f:
    text = f.read()

# replace
text = text.replace(
    orig_src_name,
    custom_src_name,
)

# write
with open(filepath, "w") as f:
    f.write(text)


####################################################
filepath = ".github/CONTRIBUTING.md"
####################################################

# read text
with open(filepath) as f:
    text = f.read()

# replace
text = (
    text.replace(
        orig_dict["GITHUB_REPO_NAME"],
        custom_dict["GITHUB_REPO_NAME"],
    )
    .replace(
        orig_dict["GITHUB_ORG_NAME"],
        custom_dict["GITHUB_ORG_NAME"],
    )
    .replace(
        orig_dict["OWNER_EMAIL"],
        custom_dict["OWNER_EMAIL"],
    )
)

# write
with open(filepath, "w") as f:
    f.write(text)


######################################################
# Remove assests/template folder
######################################################

rmtree("assets/template")
