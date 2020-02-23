import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="JournalHub", # Replace with your own username
    version="0.0.1",
    author="JournalHub. Project Team at The Lycaeum",
    author_email="csimm3330@gmail.com",
    description="JournalHub is a static blog generator.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RepoZTrees/JournalHub",
    packages = setuptools.find_packages(),
    package_data = {
        'journal':['assets/templates/*.html','assets/config.ini','assets/blog_posts/example.md']
    },
    include_package_data = True,
    entry_points ={
        'console_scripts':['journal = journal.commands:main']},
    python_requires='>=3.6',
)
