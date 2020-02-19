# JournalHub

JournalHub is a static site generator application. It's a command-line tool which converts the contents of your blogs from markdown file format (filename.md), applies it to templates, and generates a purely static HTML files.

## Step by step instructions

### Installation
To install JournalHub, please perform the following steps

1. `$ git clone https://github.com/RepoZTrees/JournalHub.git`
2. `$ cd JournalHub`
3. `$ pip install -r requirements.txt`
4. `$ python3 setup.py install`

### Usage

1. Create an empty folder (e.g. `my_blogs`) and `cd` into it. 
1. `$ journal init` - This will setup your new blog
1. A sample blog entry file will be inside `blog_posts` named `example.md`
1. `$ journal generate` will create your blog
1. `$ journal serve` will make it available with a local webserver
1. Add new entries similar to `example.md` in the `blog_posts` directory and run generate again to create new blog entries.


## Command-line commands

- `$ journal -h`  *or*  `$ journal --help`
- `$ journal init`
- `$ journal generate`
- `$ journal serve`

## Authors

Shireen Sharaf,
Zuhara Sharin,
Roshna,
Majid KM,
Shahinshah Ummer,
Thenveer,
Vik Shah.

## Special Thanks

Noufal Ibrahim for his guidance and mentorship.


